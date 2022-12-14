"""task_color

Revision ID: 7e9f683efb4f
Revises: c300f840f0e2
Create Date: 2022-11-12 18:37:53.442438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e9f683efb4f'
down_revision = 'c300f840f0e2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('color', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'color')
    # ### end Alembic commands ###
