"""mastodon acct username

Revision ID: 70a87c0a844c
Revises: 92f907c96e8b
Create Date: 2023-11-24 16:43:25.253837

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '70a87c0a844c'
down_revision: Union[str, None] = '92f907c96e8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mastodon_accounts', schema=None) as batch_op:
        # FIXME I think this is not necessary as the table will be created from scratch without migration
        pass
        # batch_op.add_column(sa.Column('username', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mastodon_accounts', schema=None) as batch_op:
        # FIXME I think this is not necessary as the table will be created from scratch without migration
        pass
        # batch_op.drop_column('username')

    # ### end Alembic commands ###
