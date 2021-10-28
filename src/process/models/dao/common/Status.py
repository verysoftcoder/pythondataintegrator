from typing import List

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base.common.StatusBase import StatusBase
from pdip.data import Entity
from models.dao.base import Base
from models.dao.operation import DataOperationJobExecution
from models.dao.operation.DataOperationJobExecutionIntegration import DataOperationJobExecutionIntegration


class Status(StatusBase, Entity, Base):
    __tablename__ = "Status"
    __table_args__ = {"schema": "Common"}
    Name = Column(String(100), index=False, unique=False, nullable=False)
    Description = Column(String(250), index=False, unique=False, nullable=False)
    DataOperationJobExecutions: List[DataOperationJobExecution] = relationship("DataOperationJobExecution",
                                                                               back_populates="Status")
    DataOperationJobExecutionIntegrations: List[DataOperationJobExecutionIntegration] = relationship(
        "DataOperationJobExecutionIntegration",
        back_populates="Status")
