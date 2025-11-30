import unittest
from src.widget import mask_account_card, get_date


class TestWidgetFunctions(unittest.TestCase):

    def test_mask_account_card(self):
        # Тестируем обработку номеров карт
        self.assertEqual(mask_account_card('Visa Platinum 7000792289606361'), 'Visa Platinum 7000 79** **** 6361')
        self.assertEqual(mask_account_card('Maestro 1596837868705199'), 'Maestro 1596 83** **** 5199')

        # Тестируем обработку счетов
        self.assertEqual(mask_account_card('Счет 73654108430135874305'), 'Счет **4305')
        self.assertEqual(mask_account_card('Счет 64686473678894779589'), 'Счет **9589')

        # Неправильный ввод должен вызывать исключение
        with self.assertRaises(ValueError):
            mask_account_card('Неправильная_строка')  # Некорректный формат строки

        with self.assertRaises(ValueError):
            mask_account_card('Счет abcde')  # Нецифровой номер счета

    def test_get_date(self):
        # Проверяем преобразование даты
        self.assertEqual(get_date('2024-03-11T02:26:18.671407'), '11.03.2024')
        self.assertEqual(get_date('2025-07-23T14:30:00'), '23.07.2025')

        # Проверьте поведение с некорректной датой
        with self.assertRaises(ValueError):
            get_date('incorrect_format')


if __name__ == '__main__':
    unittest.main()