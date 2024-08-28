import unittest
from kapsel.kapsel import Zeitkapsel
from datetime import datetime, timedelta

class TestZeitkapsel(unittest.TestCase):

    def test_versiegeln_und_oeffnen(self):
        date_to_open = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        kapsel_name = 'test.kapsel'
        data = {'message': 'Hallo, Zukunft!'}

        kapsel = Zeitkapsel(date_to_open, kapsel_name)
        kapsel.versiegeln(data)

        self.assertRaises(ValueError, kapsel.oeffnen)

        kapsel.date_to_open = datetime.now()
        opened_data = kapsel.oeffnen()
        self.assertEqual(opened_data, data)

if __name__ == '__main__':
    unittest.main()
