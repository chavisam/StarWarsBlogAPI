"""empty message

Revision ID: 717b763de287
Revises: 6581d50eed11
Create Date: 2021-11-09 14:27:29.821694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '717b763de287'
down_revision = '6581d50eed11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=200), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('Orbital_period', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.String(length=200), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=200), nullable=True),
    sa.Column('terrain', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(length=400), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('planet_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
