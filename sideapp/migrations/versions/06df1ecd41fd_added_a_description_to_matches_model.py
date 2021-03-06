"""added a description to matches model

Revision ID: 06df1ecd41fd
Revises: 0c66f50ef38d
Create Date: 2021-11-18 11:57:50.517717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06df1ecd41fd'
down_revision = '0c66f50ef38d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matches', sa.Column('description', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('matches', 'description')
    # ### end Alembic commands ###
