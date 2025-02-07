from injector import inject
from pdip.integrator.connection.domain.authentication.mechanism import MechanismTypes
from pdip.integrator.connection.domain.authentication.type import AuthenticationTypes
from pdip.integrator.connection.domain.bigdata import BigDataConnectionConfiguration
from pdip.integrator.connection.domain.enums import ConnectionTypes, ConnectorTypes
from pdip.integrator.connection.domain.server.base import Server
from pdip.integrator.connection.domain.sql import SqlConnectionConfiguration

from src.application.integrator.OperationCacheService import OperationCacheService
from src.domain.base.connection import ConnectionBase


class ConnectionConverter:
    @inject
    def __init__(self, operation_cache_service: OperationCacheService):
        self.operation_cache_service = operation_cache_service

    def convert_connection_sql(self, connection: ConnectionBase) -> SqlConnectionConfiguration:
        basic_authentication = self.operation_cache_service.get_connection_basic_authentication_by_connection_id(
            connection_id=connection.Id)
        connection_server = self.operation_cache_service.get_connection_server_by_connection_id(
            connection_id=connection.Id)
        connection_sql = SqlConnectionConfiguration(
            Name=connection.Name,
            ConnectionType=ConnectionTypes.Sql,
            ConnectorType=ConnectorTypes(connection.Database.ConnectorTypeId),
            Server=Server(
                Host=connection_server.Host,
                Port=connection_server.Port
            ),
            BasicAuthentication=basic_authentication,
            Database=connection.Database.DatabaseName,
            ServiceName=connection.Database.ServiceName,
            Sid=connection.Database.Sid,
        )
        return connection_sql

    def convert_connection_big_data(self, connection: ConnectionBase) -> SqlConnectionConfiguration:
        basic_authentication = None
        kerberos_authentication = None
        authentication_mechanism_type = MechanismTypes.NoAuthentication
        authentication_type = self.operation_cache_service.get_connection_authentication_type(
            connection_id=connection.Id)
        if authentication_type == AuthenticationTypes.BasicAuthentication:
            basic_authentication = self.operation_cache_service.get_connection_basic_authentication_by_connection_id(
                connection_id=connection.Id)
            if basic_authentication.Password is None:
                authentication_mechanism_type = MechanismTypes.UserName
            elif basic_authentication.Password is not None:
                authentication_mechanism_type = MechanismTypes.UserNamePassword

        elif authentication_type == AuthenticationTypes.Kerberos:
            kerberos_authentication = self.operation_cache_service.get_connection_kerberos_authentication_by_connection_id(
                connection_id=connection.Id)
            authentication_mechanism_type = MechanismTypes.Kerberos
        connection_server = self.operation_cache_service.get_connection_server_by_connection_id(
            connection_id=connection.Id)
        connection_sql = BigDataConnectionConfiguration(
            Name=connection.Name,
            ConnectionType=ConnectionTypes.BigData,
            ConnectorType=ConnectorTypes(connection.BigData.ConnectorTypeId),
            Server=Server(
                Host=connection_server.Host,
                Port=connection_server.Port
            ),
            BasicAuthentication=basic_authentication,
            KerberosAuthentication=kerberos_authentication,
            AuthenticationMechanismType=authentication_mechanism_type,
            Database=connection.BigData.DatabaseName,
            Ssl=connection.BigData.Ssl,
            UseOnlySspi=connection.BigData.UseOnlySspi,
        )
        return connection_sql
