"""empty message

Revision ID: 405a813da58a
Revises: 270391752a00
Create Date: 2018-06-10 12:33:05.893850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '405a813da58a'
down_revision = '270391752a00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('board')
    # ### end Alembic commands ###
