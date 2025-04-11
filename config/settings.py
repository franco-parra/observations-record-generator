import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Configuration files
CONFIG_DIR = BASE_DIR / "config"
TEMPLATE_PATH = CONFIG_DIR / "template.xlsx"
CELL_MAPPING_PATH = CONFIG_DIR / "cell_mapping.json"

# Flask configuration
class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    TEMPLATE_PATH = str(TEMPLATE_PATH)
    CELL_MAPPING_PATH = str(CELL_MAPPING_PATH)
    SHEET_NAME = os.environ.get('SHEET_NAME', 'Hoja1')  # Default to 'Hoja1' if not set

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

# Select configuration based on environment
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': ProductionConfig
} 