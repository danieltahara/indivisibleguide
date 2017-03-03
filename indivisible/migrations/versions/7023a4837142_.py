"""empty message

Revision ID: 7023a4837142
Revises: d39b6ac64338
Create Date: 2017-03-03 09:43:02.595241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7023a4837142'
down_revision = 'd39b6ac64338'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('office',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cp_id', sa.String(length=10), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('info_json', sa.String(length=1000), nullable=True),
    sa.ForeignKeyConstraint(['cp_id'], ['congressperson.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cp_id', 'city')
    )
    op.create_foreign_key(None, 'congressperson', 'congress', ['congress'], ['congress'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'congressperson', type_='foreignkey')
    op.drop_table('office')
    # ### end Alembic commands ###