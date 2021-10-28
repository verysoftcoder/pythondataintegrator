from models.base.aps.ApSchedulerJobEventBase import ApSchedulerJobEventBase
from pdip.data import Entity
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.dao.base import Base


class ApSchedulerJobEvent(ApSchedulerJobEventBase, Entity, Base):
    __tablename__ = "ApSchedulerJobEvent"
    __table_args__ = {"schema": "Aps"}
    ApSchedulerJobId = Column(Integer, ForeignKey('Aps.ApSchedulerJob.Id'))
    EventId = Column(Integer, ForeignKey('Aps.ApSchedulerEvent.Id'))
    ApSchedulerJob = relationship("ApSchedulerJob", back_populates="JobEvents")
    ApSchedulerEvent = relationship("ApSchedulerEvent", back_populates="JobEvents")
