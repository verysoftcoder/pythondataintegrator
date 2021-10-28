from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.dao.base import Base
from models.base.connection.ConnectionDatabaseBase import ConnectionDatabaseBase
from pdip.data import Entity


class ConnectionDatabase(ConnectionDatabaseBase, Entity, Base):
    __tablename__ = "ConnectionDatabase"
    __table_args__ = {"schema": "Connection"}
    ConnectionId = Column(Integer, ForeignKey('Connection.Connection.Id'))
    ConnectorTypeId = Column(Integer, ForeignKey('Connection.ConnectorType.Id'))
    Sid = Column(String(100), index=False, unique=False, nullable=True)
    ServiceName = Column(String(100), index=False, unique=False, nullable=True)
    DatabaseName = Column(String(100), index=False, unique=False, nullable=True)
    ConnectorType = relationship("ConnectorType", back_populates="Databases")