import json
import pytest
from pathlib import Path
from src.utils import load_json, logger_utils


# ТЕСТИРОВАНИЕ load_json()

@pytest.mark.parametrize(
    "content,expected",
    [
        ('[]', []),
        ('[{"id": 1}]', [{"id": 1}]),
        ('{"id": 1}', []),  # Некорректный формат JSON (не массив)
        ('', []),  # Пустой файл
    ],
)
def test_load_json_correct_cases(tmp_path, content, expected):
    # Создаем временный файл с контентом
    temp_file = tmp_path / "data.json"
    temp_file.write_text(content)

    # Читаем файл
    result = load_json(str(temp_file))
    assert result == expected


def test_load_json_nonexistent_file():
    # Проверяем обработку несуществующего файла
    result = load_json('/path/to/nonexistent/file.json')
    assert result == [], "Результат должен быть пустым списком."


def test_load_json_invalid_json(tmp_path):
    # Создаем временный файл с недействительным JSON
    temp_file = tmp_path / "invalid_data.json"
    temp_file.write_text('{"id": 1}')  # Неверный формат (недостающая закрывающая }

    # Читаем файл
    result = load_json(str(temp_file))
    assert result == [], "Результат должен быть пустым списком."


def test_load_json_permission_denied(tmp_path):
    # Создаем временный файл с ограниченными правами
    temp_file = tmp_path / "restricted.json"
    temp_file.write_text('[{"id": 1}]')
    temp_file.chmod(0o000)  # Заблокируем права доступа

    # Читаем файл
    result = load_json(str(temp_file))
    assert result == [], "Результат должен быть пустым списком."


# ТЕСТИРОВАНИЕ ЛОГГЕРА

def test_logger_configuration():
    # Проверяем директорию логов
    log_dir = Path(logger_utils.handlers[0].baseFilename).parent
    assert log_dir.is_dir(), "Директория логов должна существовать."

    # Проверяем имя лог-файла
    log_filename = Path(logger_utils.handlers[0].baseFilename).name
    assert log_filename == "utils.log", "Имя лог-файла должно быть utils.log."

    # Проверяем уровень логирования
    assert logger_utils.level == logging.DEBUG, "Уровень логирования должен быть DEBUG."



