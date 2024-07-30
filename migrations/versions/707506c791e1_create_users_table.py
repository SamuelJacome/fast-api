"""create users table

Revision ID: 707506c791e1
Revises: 6f49cb372252
Create Date: 2024-07-29 17:24:15.406530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '707506c791e1'
down_revision: Union[str, None] = '6f49cb372252'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
