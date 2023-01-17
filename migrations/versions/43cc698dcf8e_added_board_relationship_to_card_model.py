"""added board relationship to card model

Revision ID: 43cc698dcf8e
Revises: a399451add94
Create Date: 2023-01-04 09:54:56.976238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43cc698dcf8e'
down_revision = 'a399451add94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('board_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'card', 'board', ['board_id'], ['board_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'card', type_='foreignkey')
    op.drop_column('card', 'board_id')
    # ### end Alembic commands ###