import unittest
import pandas as pd
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.preprocess import clean_data, feature_engineering

class TestPreprocess(unittest.TestCase):

    def setUp(self):
        # Create dummy data
        self.data = pd.DataFrame({
            'signup_time': ['2025-01-01 10:00:00', '2025-01-01 10:00:00'],
            'purchase_time': ['2025-01-01 10:05:00', '2025-01-01 10:05:00'],
            'purchase_value': [10, 10],
            'ip_address': [12345.0, 12345.0] 
        })

    def test_clean_data_removes_duplicates(self):
        cleaned = clean_data(self.data)
        self.assertEqual(len(cleaned), 1)

    def test_feature_engineering_creates_columns(self):
        cleaned = clean_data(self.data)
        processed = feature_engineering(cleaned)
        self.assertIn('time_since_signup', processed.columns)
        self.assertIn('hour_of_day', processed.columns)
        self.assertIn('ip_address_int', processed.columns)

if __name__ == '__main__':
    unittest.main()