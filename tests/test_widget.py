# tests/test_widget.py

from unittest import TestCase

from src.widget import get_date, mask_account


class WidgetTests(TestCase):
    def test_mask_account(self):
        self.assertEqual(
            mask_account("Visa Platinum 7000792289606361"),
            "Visa Platinum 7000 79** **** 6361",
        )
        self.assertEqual(
            mask_account("Счет 73654108430135874305"),
            "Счет **4305",
        )

        # Тестируем недопустимую строку
        with self.assertRaises(ValueError):
            mask_account("")

        # Тестируем недействительную карточку
        with self.assertRaises(ValueError):
            mask_account("OnlyCard")

    def test_get_date(self):
        self.assertEqual(get_date("2023-10-26T12:34:56Z"), "26.10.2023")
        self.assertEqual(get_date("2025-01-01T00:00:00Z"), "01.01.2025")

        # Тестируем недопустимую дату
        with self.assertRaises(ValueError):
            get_date("InvalidDateFormat")

            import unittest
            from src.widget import get_date, get_mask_account

            class WidgetTests(unittest.TestCase):
                def test_mask_account(self) -> None:
                    masked = get_mask_account('some_data')
                    self.assertTrue(masked.startswith('*'))

                def test_get_date(self) -> None:
                    iso_date = "2023-10-15"
                    result = get_date(iso_date)
                    self.assertIsInstance(result, str)

