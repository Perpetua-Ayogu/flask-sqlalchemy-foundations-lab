"""Create the earthquakes table."""

from alembic import op
import sqlalchemy as sa

revision = '001_earthquakes'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'earthquakes',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('magnitude', sa.Float()),
        sa.Column('location', sa.String()),
        sa.Column('year', sa.Integer()),
    )
    op.create_index('ix_earthquakes_magnitude', 'earthquakes', ['magnitude'])


def downgrade():
    op.drop_index('ix_earthquakes_magnitude', table_name='earthquakes')
    op.drop_table('earthquakes')
