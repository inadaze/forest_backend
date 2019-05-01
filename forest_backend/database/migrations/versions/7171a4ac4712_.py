"""empty message

Revision ID: 7171a4ac4712
Revises: 8a1ba339d34c
Create Date: 2019-05-01 16:10:26.265837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7171a4ac4712'
down_revision = '8a1ba339d34c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('seeds', sa.Column('location', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('seeds', 'location')
    # ### end Alembic commands ###
