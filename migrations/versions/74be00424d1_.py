"""empty message

Revision ID: 74be00424d1
Revises: None
Create Date: 2015-05-17 16:21:39.235114

"""

# revision identifiers, used by Alembic.
revision = '74be00424d1'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    pass
    ### commands auto generated by Alembic - please adjust! ###
    # op.add_column(u'user_words', sa.Column('example', sa.String(length=500), nullable=True))
    # op.add_column(u'user_words', sa.Column('list', sa.String(length=80), nullable=True))
    # op.add_column(u'user_words', sa.Column('mob_flags', sa.String(length=100), nullable=True))
    # op.add_column(u'user_words', sa.Column('mob_incorrect', sa.Integer(), nullable=True))
    # op.add_column(u'user_words', sa.Column('mob_keyword', sa.String(length=100), nullable=True))
    # op.add_column(u'user_words', sa.Column('mob_marked', sa.Integer(), nullable=True))
    # op.add_column(u'user_words', sa.Column('mob_retention', sa.Integer(), nullable=True))
    # op.add_column(u'user_words', sa.Column('mob_retention_max', sa.Integer(), nullable=True))
    # op.add_column(u'user_words', sa.Column('transcription', sa.String(length=100), nullable=True))
    # op.add_column(u'user_words', sa.Column('updated_date', sa.DateTime(), nullable=True))
    # op.alter_column(u'user_words', 'user_id',
    #            existing_type=mysql.INTEGER(display_width=11),
    #            nullable=True)
    #
    # op.drop_index('id_UNIQUE', table_name='user_words')
    # op.create_foreign_key(None, 'user_words', 'users', ['user_id'], ['uid'])
    #
    # op.add_column(u'users', sa.Column('created_date', sa.DateTime(), nullable=True))
    # op.add_column(u'users', sa.Column('prefered_from_lang', sa.String(length=45), nullable=True))
    # op.add_column(u'users', sa.Column('prefered_to_lang', sa.String(length=45), nullable=True))
    ### end Alembic commands ###


def downgrade():
    pass
    ### commands auto generated by Alembic - please adjust! ###
    # op.drop_column(u'users', 'prefered_to_lang')
    # op.drop_column(u'users', 'prefered_from_lang')
    # op.drop_column(u'users', 'created_date')
    # op.drop_constraint(None, 'user_words', type_='foreignkey')
    # op.create_index('id_UNIQUE', 'user_words', ['id'], unique=True)
    # op.alter_column(u'user_words', 'user_id',
    #            existing_type=mysql.INTEGER(display_width=11),
    #            nullable=False)
    # op.drop_column(u'user_words', 'udate')
    # op.drop_column(u'user_words', 'transcription')
    # op.drop_column(u'user_words', 'mob_retention_max')
    # op.drop_column(u'user_words', 'mob_retention')
    # op.drop_column(u'user_words', 'mob_marked')
    # op.drop_column(u'user_words', 'mob_keyword')
    # op.drop_column(u'user_words', 'mob_incorrect')
    # op.drop_column(u'user_words', 'mob_flags')
    # op.drop_column(u'user_words', 'list')
    # op.drop_column(u'user_words', 'example')
    ### end Alembic commands ###
