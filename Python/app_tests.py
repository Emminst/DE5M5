import unittest
import pandas as pd
from pandas.api.types import is_integer_dtype
from Final_script import enrich_dateDuration

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'start_date': ['01/01/2025','02/01/2025', '03/01/2025', '01/02/2025', '15/03/2025'], 
            'end_date': [ '08/01/2025', '10/01/2025','10/01/2025','05/02/2025','20/03/2025' ]
        })

        self.df['start_date'] = pd.to_datetime(self.df['start_date'], format='%d/%m/%Y')
        self.df['end_date'] = pd.to_datetime(self.df['end_date'], format='%d/%m/%Y')

        self.df['date_delta'] = (self.df['end_date'] - self.df['start_date']).dt.days
               
    def test_duration_integer(self):
        self.assertTrue(is_integer_dtype(self.df['date_delta']), "Non-integer values found")
        
    def test_duration_abovezero(self):
        self.assertTrue((self.df['date_delta'] > 0).all(),"Values below zero found")
        
if __name__ == '__main__':
    unittest.main()



