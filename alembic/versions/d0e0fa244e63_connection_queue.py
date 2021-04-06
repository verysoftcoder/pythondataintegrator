"""connection_queue

Revision ID: d0e0fa244e63
Revises: a0968e52f6b3
Create Date: 2021-03-19 20:50:10.323965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0e0fa244e63'
down_revision = 'a0968e52f6b3'
branch_labels = None
depends_on = None

def insert_connection_types():
    from models.dao.connection.ConnectionType import ConnectionType
    from models.dao.connection.ConnectorType import ConnectorType
    bind = op.get_bind()
    from sqlalchemy import orm
    session = orm.Session(bind=bind)
    connection_type_list = [
        {
            "Name": "Queue",
        }
    ]
    connector_type_list = [
        {
            "ConnectionType": "Queue",
            "Name": "Kafka",
        }
    ]
    connection_types = []
    for connection_type_json in connection_type_list:
        connection_type = ConnectionType(Name=connection_type_json["Name"])
        connection_types.append(connection_type)
    session.bulk_save_objects(connection_types)
    session.commit()
    connector_types = []
    for connector_type_json in connector_type_list:
        connection_type = session.query(ConnectionType).filter_by(Name=connector_type_json["ConnectionType"]).first()
        connector_type = ConnectorType(Name=connector_type_json["Name"], ConnectionTypeId=connection_type.Id)
        connector_types.append(connector_type)
    session.bulk_save_objects(connector_types)
    session.commit()
def insert_connection_server():
    from models.dao.connection import Connection,ConnectionServer
    bind = op.get_bind()
    from sqlalchemy import orm
    session = orm.Session(bind=bind)
    query = bind.execute('select dic."ConnectionId", dic."Host",dic."Port" from "Connection"."ConnectionDatabase"  as dic')
    results = query.fetchall()
    for connection_database in results:
        connection = session.query(Connection).filter_by(Id=connection_database[0]).first()
        connection_server = ConnectionServer(Connection=connection,
        Host=connection_database[1],
        Port=connection_database[2])
        session.add(connection_server)

    session.commit()

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ConnectionQueue',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('ConnectionId', sa.Integer(), nullable=True),
    sa.Column('ConnectorTypeId', sa.Integer(), nullable=True),
    sa.Column('Protocol', sa.String(length=100), nullable=True),
    sa.Column('Mechanism', sa.String(length=100), nullable=True),
    sa.Column('CreatedByUserId', sa.Integer(), nullable=False),
    sa.Column('CreationDate', sa.DateTime(), nullable=False),
    sa.Column('LastUpdatedUserId', sa.Integer(), nullable=True),
    sa.Column('LastUpdatedDate', sa.DateTime(), nullable=True),
    sa.Column('IsDeleted', sa.Integer(), nullable=False),
    sa.Column('Comments', sa.String(length=1000), nullable=True),
    sa.Column('RowVersion', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['ConnectionId'], ['Connection.Connection.Id'], ),
    sa.ForeignKeyConstraint(['ConnectorTypeId'], ['Connection.ConnectorType.Id'], ),
    sa.PrimaryKeyConstraint('Id'),
    schema='Connection'
    )
    op.create_table('ConnectionServer',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('ConnectionId', sa.Integer(), nullable=True),
    sa.Column('Host', sa.String(length=100), nullable=True),
    sa.Column('Port', sa.Integer(), nullable=True),
    sa.Column('CreatedByUserId', sa.Integer(), nullable=False),
    sa.Column('CreationDate', sa.DateTime(), nullable=False),
    sa.Column('LastUpdatedUserId', sa.Integer(), nullable=True),
    sa.Column('LastUpdatedDate', sa.DateTime(), nullable=True),
    sa.Column('IsDeleted', sa.Integer(), nullable=False),
    sa.Column('Comments', sa.String(length=1000), nullable=True),
    sa.Column('RowVersion', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['ConnectionId'], ['Connection.Connection.Id'], ),
    sa.PrimaryKeyConstraint('Id'),
    schema='Connection'
    )
    insert_connection_server()
    op.drop_column('ConnectionDatabase', 'Host', schema='Connection')
    op.drop_column('ConnectionDatabase', 'Port', schema='Connection')
    op.drop_column('ConnectionFile', 'Host', schema='Connection')
    op.drop_column('ConnectionFile', 'Port', schema='Connection')

    insert_connection_types()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ConnectionFile', sa.Column('Port', sa.INTEGER(), autoincrement=False, nullable=True), schema='Connection')
    op.add_column('ConnectionFile', sa.Column('Host', sa.VARCHAR(length=100), autoincrement=False, nullable=True), schema='Connection')
    op.add_column('ConnectionDatabase', sa.Column('Port', sa.INTEGER(), autoincrement=False, nullable=True), schema='Connection')
    op.add_column('ConnectionDatabase', sa.Column('Host', sa.VARCHAR(length=100), autoincrement=False, nullable=True), schema='Connection')
    op.drop_table('ConnectionServer', schema='Connection')
    op.drop_table('ConnectionQueue', schema='Connection')
    # ### end Alembic commands ###
