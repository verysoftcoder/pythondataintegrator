from typing import List

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from models.base.aps.ApSchedulerEventBase import ApSchedulerEventBase
from pdip.data import Entity
from models.dao.aps.ApSchedulerJobEvent import ApSchedulerJobEvent
from models.dao.base import Base


class ApSchedulerEvent(ApSchedulerEventBase, Entity, Base):
    __tablename__ = "ApSchedulerEvent"
    __table_args__ = {"schema": "Aps"}

    Code = Column(Integer, nullable=False)
    Name = Column(String(255), nullable=False)
    Description = Column(String(1000), nullable=False)
    Class = Column(String(255), nullable=False)
    JobEvents: List[ApSchedulerJobEvent] = relationship("ApSchedulerJobEvent", back_populates="ApSchedulerEvent")
