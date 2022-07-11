"""empty message

Revision ID: 1eedcd0865b9
Revises: d3668c98722f
Create Date: 2022-07-11 10:26:57.880423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1eedcd0865b9'
down_revision = 'd3668c98722f'
branch_labels = None
depends_on = None


def upgrade():
     op.execute("INSERT INTO users (password, email, is_admin, name, last_name) VALUES ('12345', 'superuser@gmail.com', True, 'super', 'user')")
    


def downgrade():
    op.execute("DELETE FROM users WHERE email='superuser@gmail.com'")
