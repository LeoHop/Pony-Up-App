"""creating my databases again

Revision ID: 410ea6e02ac2
Revises: 
Create Date: 2020-05-11 12:50:40.168924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '410ea6e02ac2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('moola', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('sport', sa.String(length=30), nullable=True),
    sa.Column('location', sa.String(length=120), nullable=True),
    sa.Column('watchSpot', sa.String(length=60), nullable=True),
    sa.Column('eventName', sa.String(length=90), nullable=True),
    sa.Column('openingBetA', sa.Integer(), nullable=True),
    sa.Column('openingBetB', sa.Integer(), nullable=True),
    sa.Column('currentBetA', sa.Integer(), nullable=True),
    sa.Column('currentBetB', sa.Integer(), nullable=True),
    sa.Column('teamA', sa.String(length=30), nullable=True),
    sa.Column('teamB', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('amountBetting', sa.Integer(), nullable=True),
    sa.Column('teamBetting', sa.String(length=30), nullable=True),
    sa.Column('gameId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gameId'], ['game.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bet')
    op.drop_table('game')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
