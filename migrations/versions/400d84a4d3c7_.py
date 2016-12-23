"""empty message

Revision ID: 400d84a4d3c7
Revises: 5cf83ba59cf6
Create Date: 2016-12-19 22:40:19.579313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '400d84a4d3c7'
down_revision = '5cf83ba59cf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###