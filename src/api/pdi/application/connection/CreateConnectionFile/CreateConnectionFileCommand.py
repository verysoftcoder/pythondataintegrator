from dataclasses import dataclass
from pdip.cqrs import ICommand

from pdi.application.connection.CreateConnectionFile.CreateConnectionFileRequest import CreateConnectionFileRequest


@dataclass
class CreateConnectionFileCommand(ICommand):
    request: CreateConnectionFileRequest = None
