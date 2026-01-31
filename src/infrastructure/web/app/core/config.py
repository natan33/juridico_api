import os
from dotenv import load_dotenv

# Caminho até a raiz do projeto (onde está .env)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..",".."))
ENV_PATH = os.path.join(ROOT_DIR, ".env")

if os.path.exists(ENV_PATH):
    load_dotenv(ENV_PATH)
else:
    print(f"[WARNING] .env não encontrado em {ENV_PATH}. Variáveis devem vir do ambiente.")

def get_env_or_fail(key: str, default=None):
    value = os.getenv(key, default)
    if value is None:
        raise RuntimeError(f"Variável de ambiente obrigatória não encontrada: {key}")
    return value

class Config:
    SQLALCHEMY_DATABASE_URI = get_env_or_fail("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET = get_env_or_fail("JWT_SECRET")
    FLASK_APP = get_env_or_fail("FLASK_APP")
    FLASK_ENV = get_env_or_fail("FLASK_ENV")