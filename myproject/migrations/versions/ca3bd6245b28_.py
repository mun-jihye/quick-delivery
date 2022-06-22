"""empty message

Revision ID: ca3bd6245b28
Revises: 39f6c920bed6
Create Date: 2022-06-22 22:53:22.824916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca3bd6245b28'
down_revision = '39f6c920bed6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
