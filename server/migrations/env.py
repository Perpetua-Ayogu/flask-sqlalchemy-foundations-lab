from alembic import context
from flask import current_app

migrate = current_app.extensions['migrate']
engine = migrate.db.engine
metadata = migrate.db.metadata

if context.is_offline_mode():
    context.configure(
        url=engine.url.render_as_string(hide_password=False),
        target_metadata=metadata,
        literal_binds=True,
        dialect_opts={'paramstyle': 'named'},
        **migrate.configure_args,
    )
    with context.begin_transaction():
        context.run_migrations()
else:
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=metadata,
            **migrate.configure_args,
        )
        with context.begin_transaction():
            context.run_migrations()
