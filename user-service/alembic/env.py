import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

DATABASE_URL = os.getenv("DATABASE_URL")

# Alembic Config
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Logging
if config.config_file_name:
    fileConfig(config.config_file_name)

# Models and Metadata
from app.db.base import Base
from app.db.models.user import User  # 👈 Correct path here

target_metadata = Base.metadata

# Migration Logic
def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
