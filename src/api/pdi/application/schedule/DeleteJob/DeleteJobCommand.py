from dataclasses import dataclass
from pdip.cqrs import ICommand

from pdi.application.schedule.DeleteJob.DeleteJobRequest import DeleteJobRequest


@dataclass
class DeleteJobCommand(ICommand):
    request: DeleteJobRequest = None
