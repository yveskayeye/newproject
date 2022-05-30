"""empty message

Revision ID: fff231172d8d
Revises: 669d0a09598b
Create Date: 2022-05-30 06:02:53.714993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fff231172d8d'
down_revision = '669d0a09598b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('blood_type', sa.String(length=120), nullable=False),
    sa.Column('age', sa.String(length=120), nullable=False),
    sa.Column('allergies', sa.String(length=120), nullable=False),
    sa.Column('number_children', sa.String(length=120), nullable=False),
    sa.Column('last_birth', sa.String(length=120), nullable=False),
    sa.Column('medical_condition', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('records')
    # ### end Alembic commands ###