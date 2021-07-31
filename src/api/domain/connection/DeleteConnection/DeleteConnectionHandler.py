from injector import inject

from domain.connection.DeleteConnection.DeleteConnectionCommand import DeleteConnectionCommand
from domain.connection.services.ConnectionService import ConnectionService
from domain.notification.SendNotification.SendNotificationCommand import SendNotificationCommand
from domain.notification.SendNotification.SendNotificationRequest import SendNotificationRequest, \
    NotificationAdditionalData
from infrastructure.cqrs.Dispatcher import Dispatcher
from infrastructure.cqrs.ICommandHandler import ICommandHandler
from infrastructure.data.RepositoryProvider import RepositoryProvider


class DeleteConnectionHandler(ICommandHandler[DeleteConnectionCommand]):
    @inject
    def __init__(self,
                 dispatcher: Dispatcher,
                 connection_service: ConnectionService,
                 repository_provider: RepositoryProvider,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository_provider = repository_provider
        self.dispatcher = dispatcher
        self.connection_service = connection_service

    def handle(self, command: DeleteConnectionCommand):
        result = self.connection_service.delete_connection(id=command.request.Id)
        self.repository_provider.commit()
        self.notify(message=result, id=command.request.Id)

    def notify(self, message: str, id: int):
        data_list = []
        data = NotificationAdditionalData(Key="Type", Value="Connection")
        data_list.append(data)
        data = NotificationAdditionalData(Key="Id", Value=id)
        data_list.append(data)
        send_notification_request = SendNotificationRequest(Message=message, Type=1, Action=3, AdditionalData=data_list)
        self.dispatcher.dispatch(SendNotificationCommand(request=send_notification_request))
