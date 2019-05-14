"""empty message

Revision ID: 2a361e37f8cf
Revises: 8c80aa9470fb
Create Date: 2019-05-13 19:21:42.840601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a361e37f8cf'
down_revision = '8c80aa9470fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seeds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('word', sa.String(length=250), nullable=False),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seed_id', sa.Integer(), nullable=True),
    sa.Column('level_id', sa.Integer(), nullable=True),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('last_modified_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['level_id'], ['tree_levels.id'], ),
    sa.ForeignKeyConstraint(['seed_id'], ['seeds.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('branches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tree_id', sa.Integer(), nullable=True),
    sa.Column('idea', sa.String(length=250), nullable=False),
    sa.Column('branch_level', sa.Integer(), nullable=True),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('last_modified_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['tree_id'], ['trees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('branches')
    op.drop_table('trees')
    op.drop_table('seeds')
    # ### end Alembic commands ###
