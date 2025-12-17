from pathlib import Path

# абсолютный путь к корневой папке
BASE_DIR = Path(__file__).resolve().parent
# абсолютный путь к папке с базовым файлом-источником
DATA_PATH = BASE_DIR / "data.json"
