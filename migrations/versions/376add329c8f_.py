"""empty message

Revision ID: 376add329c8f
Revises: 
Create Date: 2019-05-11 16:30:53.614380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '376add329c8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
