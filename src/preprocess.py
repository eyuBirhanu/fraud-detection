import pandas as pd
import numpy as np
import logging

# Configure Logging (Professional Standard)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(path: str) -> pd.DataFrame:
    """Loads CSV data with error handling."""
    try:
        df = pd.read_csv(path)
        logging.info(f"Data loaded successfully from {path}. Shape: {df.shape}")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning: duplicates and data types."""
    df = df.copy()
    
    # Remove duplicates
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    if len(df) < initial_count:
        logging.info(f"Removed {initial_count - len(df)} duplicate rows.")

    # Convert Timestamps
    if 'signup_time' in df.columns:
        df['signup_time'] = pd.to_datetime(df['signup_time'])
    if 'purchase_time' in df.columns:
        df['purchase_time'] = pd.to_datetime(df['purchase_time'])
        
    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Creates new features from raw data."""
    df = df.copy()
    
    # 1. Time-based features
    if 'purchase_time' in df.columns and 'signup_time' in df.columns:
        # Time since signup (in seconds) - Fraudsters often buy immediately
        df['time_since_signup'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds()
        
        # Hour of day (Fraud might happen at night)
        df['hour_of_day'] = df['purchase_time'].dt.hour
        df['day_of_week'] = df['purchase_time'].dt.dayofweek

    # 2. IP Address Integer Conversion
    if 'ip_address' in df.columns:
        # Check if it's already numeric or needs conversion
        df['ip_address_int'] = df['ip_address'].astype(float).astype(int)

    return df

def merge_geolocation(fraud_df: pd.DataFrame, ip_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merges fraud data with Country data using IP ranges.
    Uses efficient merge_asof algorithm.
    """
    logging.info("Starting Geolocation Merge...")
    
    # Ensure IP data is sorted for merge_asof (Required)
    ip_df['lower_bound_ip_address'] = ip_df['lower_bound_ip_address'].astype(float).astype(int)
    ip_df = ip_df.sort_values('lower_bound_ip_address')
    
    fraud_df = fraud_df.sort_values('ip_address_int')
    
    # Perform Merge
    merged_df = pd.merge_asof(
        fraud_df,
        ip_df,
        left_on='ip_address_int',
        right_on='lower_bound_ip_address',
        direction='backward'
    )
    
    # Logical Check: Ensure the IP is actually within the upper bound
    mask = merged_df['ip_address_int'] > merged_df['upper_bound_ip_address']
    merged_df.loc[mask, 'country'] = 'Unknown'
    
    merged_df['country'] = merged_df['country'].fillna('Unknown')
    
    logging.info("Geolocation Merge Completed.")
    return merged_df