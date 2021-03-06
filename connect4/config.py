import os

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "5000"))

DEBUG = bool(os.getenv("DEBUG", "True"))
TESTING = bool(os.getenv("TESTING", "True"))

DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "postgres")
DATABASE_NAME = os.getenv("DATABASE_NAME", "connect-four-server")
DATABASE_HOST = os.getenv("DATABASE_HOST", "connect-four-server-db")
DATABASE_PORT = int(os.getenv("DATABASE_PORT", "5432"))

CSRF_ENABLED = bool(os.getenv("CSRF_ENABLED", "False"))
SECRET_KEY = os.getenv("SECRET_KEY", "this-really-needs-to-be-changed")
