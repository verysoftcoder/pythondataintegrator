import json
from injector import inject

from domain.notification.SendNotification.SendNotificationCommand import SendNotificationCommand
from domain.notification.SendNotification.SendNotificationRequest import NotificationAdditionalData, \
    SendNotificationRequest
from infrastructure.cqrs.Dispatcher import Dispatcher
from infrastructure.data.RepositoryProvider import RepositoryProvider
from infrastructure.dependency.scopes import IScoped
from infrastructure.json.DateTimeEncoder import DateTimeEncoder
from domain.operation.CreateDataOperation.CreateDataOperationCommand import CreateDataOperationCommand
from domain.operation.services.DataOperationService import DataOperationService
from infrastructure.cqrs.ICommandHandler import ICommandHandler


class CreateDataOperationCommandHandler(ICommandHandler[CreateDataOperationCommand], IScoped):
    @inject
    def __init__(self,
                 dispatcher: Dispatcher,
                 repository_provider: RepositoryProvider,
                 data_operation_service: DataOperationService,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dispatcher = dispatcher
        self.repository_provider = repository_provider
        self.data_operation_service = data_operation_service

    def handle(self, command: CreateDataOperationCommand):
        definition_json = json.dumps(command.request.to_dict(), cls=DateTimeEncoder, indent=4)
        check_existing = self.data_operation_service.check_by_name(name=command.request.Name)
        data_operation = self.data_operation_service.post_data_operation(
            data_operation_model=command.request,
            definition_json=definition_json)

        self.repository_provider.commit()
        self.notify(id=data_operation.Id, name=data_operation.Name, check_existing=check_existing)

    def notify(self, id: int, name: str, check_existing: bool):
        data_list = []
        data = NotificationAdditionalData(Key="Type", Value="DataOperation")
        data_list.append(data)
        data = NotificationAdditionalData(Key="Id", Value=id)
        data_list.append(data)
        data = NotificationAdditionalData(Key="Name", Value=name)
        data_list.append(data)
        if check_existing:
            action = 2
            message = f"{name} Data Operation Updated"
        else:
            action = 1
            message = f"{name} Data Operation Created"

        send_notification_request = SendNotificationRequest(Message=message, Type=1, Action=action,
                                                            AdditionalData=data_list)
        self.dispatcher.dispatch(SendNotificationCommand(request=send_notification_request))
