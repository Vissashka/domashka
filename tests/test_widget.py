import unittest
from src.widget import get_date, mask_account_card as mask_account


class WidgetTests(unittest.TestCase):
    def test_get_date(self):
        self.assertEqual(get_date("2023-10-26T12:34:56Z"), "26.10.2023")

    def test_mask_account(self):
        self.assertEqual(mask_account("Visa Platinum 7000792289606361"), "Visa Platinum 7000 79** **** 6361")
