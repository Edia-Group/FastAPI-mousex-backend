"""Domande / Varianti generation

Revision ID: be088d3e1453
Revises: 
Create Date: 2025-03-10 19:27:42.973141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be088d3e1453'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('domande',
    sa.Column('idDomanda', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('corpo', sa.String(length=500), nullable=False),
    sa.Column('data_ora_inserimento', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('tipo', sa.String(length=50), nullable=False),
    sa.Column('numeroPagine', sa.Integer(), nullable=True),
    sa.Column('attivo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('idDomanda')
    )
    op.create_index(op.f('ix_domande_idDomanda'), 'domande', ['idDomanda'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('last_login', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('testsgroup',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nr_test', sa.Integer(), nullable=False),
    sa.Column('nr_gruppo', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=50), nullable=False),
    sa.Column('in_sequenza', sa.Boolean(), nullable=False),
    sa.Column('secondi_ritardo', sa.Integer(), nullable=False),
    sa.Column('data_ora_inizio', sa.DateTime(timezone=True), nullable=True),
    sa.Column('data_ora_inserimento', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('utente_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['utente_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_testsgroup_id'), 'testsgroup', ['id'], unique=False)
    op.create_table('varianti',
    sa.Column('idVariante', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('corpo', sa.String(length=500), nullable=False),
    sa.Column('data_ora_inserimento', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('tipo', sa.String(length=50), nullable=True),
    sa.Column('numeroPagine', sa.Integer(), nullable=True),
    sa.Column('attivo', sa.Boolean(), nullable=True),
    sa.Column('domanda_id', sa.Integer(), nullable=False),
    sa.Column('rispostaEsatta', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['domanda_id'], ['domande.idDomanda'], ),
    sa.PrimaryKeyConstraint('idVariante')
    )
    op.create_index(op.f('ix_varianti_idVariante'), 'varianti', ['idVariante'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_varianti_idVariante'), table_name='varianti')
    op.drop_table('varianti')
    op.drop_index(op.f('ix_testsgroup_id'), table_name='testsgroup')
    op.drop_table('testsgroup')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_domande_idDomanda'), table_name='domande')
    op.drop_table('domande')
    # ### end Alembic commands ###
