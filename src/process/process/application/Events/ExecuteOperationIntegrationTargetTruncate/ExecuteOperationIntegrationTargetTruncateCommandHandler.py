from injector import inject
from pdip.cqrs import ICommandHandler, Dispatcher
from pdip.data.repository import RepositoryProvider
from pdip.logging.loggers.sql import SqlLogger

from process.application.Events.ExecuteOperationIntegrationTargetTruncate.ExecuteOperationIntegrationTargetTruncateCommand import \
    ExecuteOperationIntegrationTargetTruncateCommand


class ExecuteOperationIntegrationTargetTruncateCommandHandler(
    ICommandHandler[ExecuteOperationIntegrationTargetTruncateCommand]):
    @inject
    def __init__(self,
                 dispatcher: Dispatcher,
                 logger: SqlLogger,
                 repository_provider: RepositoryProvider,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logger
        self.repository_provider = repository_provider
        self.dispatcher = dispatcher

    def handle(self, command: ExecuteOperationIntegrationTargetTruncateCommand):
        try:
            message = f'{command.request.OperationIntegration.Id}-{command.request.OperationIntegration.Order}-{command.request.OperationIntegration.Name}-Target truncate finished. (Affected Row Count:{command.request.RowCount}'
            self.logger.info(message)

        except Exception as ex:
            self.logger.exception(ex, str(ex))
            raise Exception(str(ex))
