"""шÑinitial

Revision ID: 6a7192d90509
Revises:
Create Date: 2025-03-04 15:07:51.197514

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6a7192d90509"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_user")),
        sa.UniqueConstraint("email", name=op.f("uq_user_email")),
        sa.UniqueConstraint("username", name=op.f("uq_user_username")),
    )
    op.create_table(
        "transport",
        sa.Column(
            "brand", sa.Enum("Audi", "BMW", name="brand"), nullable=False
        ),
        sa.Column("model", sa.String(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name=op.f("fk_transport_user_id_user"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_transport")),
    )
    op.create_table(
        "fuel_loss",
        sa.Column(
            "fuel_type",
            sa.Enum(
                "Petrol_80",
                "Petrol_92",
                "Petrol_95",
                "Petrol_100",
                "Diesel",
                name="fueltype",
            ),
            nullable=False,
        ),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("transport_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["transport_id"],
            ["transport.id"],
            name=op.f("fk_fuel_loss_transport_id_transport"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_fuel_loss")),
    )
    op.create_table(
        "repair_loss",
        sa.Column(
            "repair_type",
            sa.Enum(
                "Unplanned_repairs", "Technical_maintenance", name="repairtype"
            ),
            nullable=False,
        ),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("transport_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["transport_id"],
            ["transport.id"],
            name=op.f("fk_repair_loss_transport_id_transport"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_repair_loss")),
    )
    op.create_table(
        "spare_loss",
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("transport_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["transport_id"],
            ["transport.id"],
            name=op.f("fk_spare_loss_transport_id_transport"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_spare_loss")),
    )
    op.create_table(
        "supplie_loss",
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("transport_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["transport_id"],
            ["transport.id"],
            name=op.f("fk_supplie_loss_transport_id_transport"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_supplie_loss")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("supplie_loss")
    op.drop_table("spare_loss")
    op.drop_table("repair_loss")
    op.drop_table("fuel_loss")
    op.drop_table("transport")
    op.drop_table("user")
    # ### end Alembic commands ###
