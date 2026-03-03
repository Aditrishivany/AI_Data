"""create initial tables

Revision ID: 20260302_0001
Revises:
Create Date: 2026-03-02
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "20260302_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "participants",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=150), nullable=False),
        sa.Column("phone", sa.String(length=20), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_participants_email"), "participants", ["email"], unique=True)
    op.create_index(op.f("ix_participants_id"), "participants", ["id"], unique=False)

    op.create_table(
        "trainers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=150), nullable=False),
        sa.Column("expertise", sa.String(length=150), nullable=True),
        sa.Column("bio", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_trainers_email"), "trainers", ["email"], unique=True)
    op.create_index(op.f("ix_trainers_id"), "trainers", ["id"], unique=False)

    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=150), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("capacity", sa.Integer(), nullable=False),
        sa.Column("trainer_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["trainer_id"], ["trainers.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_events_id"), "events", ["id"], unique=False)

    op.create_table(
        "registrations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("participant_id", sa.Integer(), nullable=False),
        sa.Column("event_id", sa.Integer(), nullable=False),
        sa.Column("registered_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["event_id"], ["events.id"]),
        sa.ForeignKeyConstraint(["participant_id"], ["participants.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("participant_id", "event_id", name="uq_participant_event"),
    )
    op.create_index(op.f("ix_registrations_id"), "registrations", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_registrations_id"), table_name="registrations")
    op.drop_table("registrations")
    op.drop_index(op.f("ix_events_id"), table_name="events")
    op.drop_table("events")
    op.drop_index(op.f("ix_trainers_id"), table_name="trainers")
    op.drop_index(op.f("ix_trainers_email"), table_name="trainers")
    op.drop_table("trainers")
    op.drop_index(op.f("ix_participants_id"), table_name="participants")
    op.drop_index(op.f("ix_participants_email"), table_name="participants")
    op.drop_table("participants")

