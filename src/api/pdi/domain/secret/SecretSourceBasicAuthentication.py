from pdip.data import Entity
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from pdi.domain.base import Base
from pdi.domain.base.secret.SecretSourceBasicAuthenticationBase import SecretSourceBasicAuthenticationBase


class SecretSourceBasicAuthentication(SecretSourceBasicAuthenticationBase, Entity, Base):
    __tablename__ = "SecretSourceBasicAuthentication"
    __table_args__ = {"schema": "Secret"}
    SecretSourceId = Column(Integer, ForeignKey('Secret.SecretSource.Id'))
    User = Column(String(100), index=False, unique=False, nullable=False)
    Password = Column(String(100), index=False, unique=False, nullable=False)
    SecretSource = relationship("SecretSource", back_populates="SecretSourceBasicAuthentications")
