"""empty message

Revision ID: 5d4710bda574
Revises: 30140461b814
Create Date: 2022-05-28 12:13:41.922934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d4710bda574'
down_revision = '30140461b814'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("INSERT INTO users (password, email, is_admin, name, last_name) VALUES ('1234', 'yveskayeye30@gmail.com', True, 'yves', 'kayeye')")
    


def downgrade():
    op.execute("DELETE FROM users WHERE email='yveskayeye30@gmail.com'")
