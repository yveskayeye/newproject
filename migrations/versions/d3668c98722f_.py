"""empty message

Revision ID: d3668c98722f
Revises: fff231172d8d
Create Date: 2022-07-05 09:54:06.831424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3668c98722f'
down_revision = 'fff231172d8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recordsTwo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('blood_type', sa.String(length=120), nullable=False),
    sa.Column('age', sa.String(length=120), nullable=False),
    sa.Column('systolic_BP', sa.String(length=120), nullable=False),
    sa.Column('diastolic_BP', sa.String(length=120), nullable=False),
    sa.Column('blood_sugar', sa.String(length=120), nullable=False),
    sa.Column('body_temp', sa.String(length=120), nullable=False),
    sa.Column('heart_rate', sa.String(length=120), nullable=False),
    sa.Column('risk_level', sa.String(length=120), nullable=False),
    sa.Column('allergies', sa.String(length=120), nullable=False),
    sa.Column('number_children', sa.String(length=120), nullable=False),
    sa.Column('last_birth', sa.String(length=120), nullable=False),
    sa.Column('medical_condition', sa.String(length=120), nullable=False),
    sa.Column('miscarriage', sa.String(length=80), nullable=False),
    sa.Column('still_birth', sa.String(length=120), nullable=False),
    sa.Column('premature_birth', sa.String(length=120), nullable=False),
    sa.Column('pre_clamsia', sa.String(length=120), nullable=False),
    sa.Column('gestation_diabetes', sa.String(length=120), nullable=False),
    sa.Column('hiv_status', sa.String(length=120), nullable=False),
    sa.Column('sugar_levels', sa.String(length=120), nullable=False),
    sa.Column('weight', sa.String(length=120), nullable=False),
    sa.Column('prev_dev', sa.String(length=120), nullable=False),
    sa.Column('id_number', sa.String(length=120), nullable=False),
    sa.Column('marital_status', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recordsTwo')
    # ### end Alembic commands ###
