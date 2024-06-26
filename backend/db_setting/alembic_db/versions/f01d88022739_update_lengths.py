"""update lengths

Revision ID: f01d88022739
Revises: 
Create Date: 2024-06-16 10:51:57.833749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f01d88022739'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Restaurant',
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('restaurant_id')
    )
    op.create_index(op.f('ix_Restaurant_name'), 'Restaurant', ['name'], unique=False)
    op.create_index(op.f('ix_Restaurant_restaurant_id'), 'Restaurant', ['restaurant_id'], unique=False)
    op.create_table('User',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('mail', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_User_mail'), 'User', ['mail'], unique=True)
    op.create_index(op.f('ix_User_user_id'), 'User', ['user_id'], unique=False)
    op.create_table('Bookmark',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('column_id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('memo', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.user_id'], ),
    sa.PrimaryKeyConstraint('user_id', 'column_id')
    )
    op.create_index(op.f('ix_Bookmark_column_id'), 'Bookmark', ['column_id'], unique=False)
    op.create_index(op.f('ix_Bookmark_restaurant_id'), 'Bookmark', ['restaurant_id'], unique=True)
    op.create_index(op.f('ix_Bookmark_user_id'), 'Bookmark', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Bookmark_user_id'), table_name='Bookmark')
    op.drop_index(op.f('ix_Bookmark_restaurant_id'), table_name='Bookmark')
    op.drop_index(op.f('ix_Bookmark_column_id'), table_name='Bookmark')
    op.drop_table('Bookmark')
    op.drop_index(op.f('ix_User_user_id'), table_name='User')
    op.drop_index(op.f('ix_User_mail'), table_name='User')
    op.drop_table('User')
    op.drop_index(op.f('ix_Restaurant_restaurant_id'), table_name='Restaurant')
    op.drop_index(op.f('ix_Restaurant_name'), table_name='Restaurant')
    op.drop_table('Restaurant')
    # ### end Alembic commands ###
