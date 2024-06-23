from alembic import op
import sqlalchemy as sa
from typing import Sequence, Union


revision: str = "8e6c55fbac1b"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
