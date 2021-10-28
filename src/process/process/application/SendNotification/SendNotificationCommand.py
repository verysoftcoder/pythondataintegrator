from dataclasses import dataclass
from pdip.cqrs import ICommand

from process.application.SendNotification.SendNotificationRequest import SendNotificationRequest


@dataclass
class SendNotificationCommand(ICommand):
    request: SendNotificationRequest = None
