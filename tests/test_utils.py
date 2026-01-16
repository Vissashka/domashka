import json
import pytest
from src.utils import load_json

# Тест 1: Загрузка валидных JSON-данных
def test_load_valid_json(tmp_path):
    # Создаём временный файл с правильным JSON
    temp_file = tmp_path / "valid_data.json"
    content = '[{"id": 1, "amount": 100}]'
    temp_file.write_text(content)

    # Читаем файл
    result = load_json(str(temp_file))
    assert len(result) == 1
    assert result[0]['id'] == 1
    assert result[0]['amount'] == 100

# Тест 2: Обработка несуществующего файла
def test_load_nonexistent_file():
    result = load_json('/path/to/nonexistent/file.json')
    assert result == [], "Результат должен быть пустым списком."

# Тест 3: Обработка неверного формата JSON
def test_load_invalid_json_format(tmp_path):
    # Создаём временный файл с неверным JSON
    temp_file = tmp_path / "invalid_data.json"
    content = '{"id": 1}'  # Недостаточно закрывающей скобки
    temp_file.write_text(content)

    # Читаем файл
    result = load_json(str(temp_file))
    assert result == [], "Результат должен быть пустым списком."

# Тест 4: Обработка общего IOErrors
def test_io_errors(tmp_path):
    # Создаём временно защищённый файл, доступ к которому запрещён
    temp_file = tmp_path / "protected.json"
    temp_file.touch(mode=0o000)  # Защищаем файл от чтения

    # Проверяем, что чтение невозможно
    result = load_json(str(temp_file))
    assert result == [], "Результат должен быть пустым списком."

# Тест 5: Чтение пустого файла
def test_load_empty_file(tmp_path):
    # Создаём временный пустой файл
    temp_file = tmp_path / "empty.json"
    temp_file.write_text('')

    # Читаем файл
    result = load_json(str(temp_file))
    assert result == [], "Результат должен быть пустым списком."
import json
import os
import tempfile
import shutil
import pytest
from pathlib import Path
from src.utils import load_json, logger_utils

# Тестирование функции load_json

def test_load_valid_json(tmp_path):
    # Создаём временный файл с правильным JSON
    temp_file = tmp_path / "valid_data.json"
    content = '[{"id": 1, "amount": 100}]'
    temp_file.write_text(content)

    # Читаем файл
    result = load_json(str(temp_file))
    assert len(result) == 1
    assert result[0]['id'] == 1
    assert result[0]['amount'] == 100

def test_load_nonexistent_file():
    # Проверяем обработку несуществующего файла
    result = load_json('/path/to/nonexistent/file.json')
    assert result == [], "Результат должен быть пустым списком."

def test_load_invalid_json_format(tmp_path):
    # Создаём временный файл с неверным JSON
    temp_file = tmp_path / "invalid_data.json"
    content = '{"id": 1}'  # Отсутствие закрывающей фигурной скобки
    temp_file.write_text(content)

    # Читаем файл
    result = load_json(str(temp_file))
    assert result == [], "Результат должен быть пустым списком."

def test_load_empty_file(tmp_path):
    # Создаём временный пустой файл
    temp_file = tmp_path / "empty.json"
    temp_file.write_text('')

    # Читаем файл
    result = load_json(str(temp_file))
    assert result == [], "Результат должен быть пустым списком."

def test_load_permission_denied(tmp_path):
    # Создаём временный файл с ограниченным доступом
    temp_file = tmp_path / "restricted.json"
    temp_file.write_text('[{"id": 1}]')
    temp_file.chmod(0o000)  # Ограничиваем права доступа

    # Читаем файл
    result = load_json(str(temp_file))
    assert result == [], "Результат должен быть пустым списком."

# Тестирование логгирования

def test_logger_setup():
    # Проверяем существование лог-файла
    log_dir = Path(logger_utils.handlers[0].baseFilename).parent
    assert log_dir.is_dir(), "Директория логов должна существовать."

    # Проверяем правильность имени лог-файла
    log_filename = Path(logger_utils.handlers[0].baseFilename).name
    assert log_filename == "utils.log", "Имя лог-файла должно быть utils.log."

    # Проверяем уровень логирования
    assert logger_utils.level == logging.DEBUG, "Уровень логирования должен быть DEBUG."

    # Проверяем наличие и корректность хэндлера
    handler = logger_utils.handlers[0]
    assert isinstance(handler, logging.FileHandler), "Хэндлером должен быть FileHandler."

    # Проверяем наличие Formatter
    formatter = handler.formatter
    assert isinstance(formatter, logging.Formatter), "Форматировщик должен быть экземпляром класса Formatter."

    # Проверяем корректность паттерна форматирования
    format_pattern = "%(asctime)s | %(levelname)-8s | %(module)-10s | %(message)s"
    assert formatter._fmt == format_pattern, "Паттерн форматирования должен быть корректным."

# Дополнительно: Тест на очистку лог-файла
def test_clear_log_file():
    # Сначала проверим, что файл журнала существует
    log_file = Path(logger_utils.handlers[0].baseFilename)
    assert log_file.exists(), "Файл журнала должен существовать."

    # Удалим файл
    log_file.unlink(missing_ok=True)

    # Проверим, что файл удалён
    assert not log_file.exists(), "Файл журнала должен быть удалён."

    # Пытаемся восстановить журнал, проверяя восстановление пути
    log_file.touch()
    assert log_file.exists(), "Файл журнала должен быть восстановлен."


