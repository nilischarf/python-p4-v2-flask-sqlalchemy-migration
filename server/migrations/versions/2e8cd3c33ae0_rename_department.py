"""rename department

Revision ID: 2e8cd3c33ae0
Revises: 79acc815ea7d
Create Date: 2025-03-30 09:25:59.953587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e8cd3c33ae0'
down_revision = '79acc815ea7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
    # ### end Alembic commands ###
