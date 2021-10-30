from dataclasses import dataclass
from pdip.cqrs import IQuery

from pdi.application.operation.GetDataOperationJobExecutionIntegrationList.GetDataOperationJobExecutionIntegrationListRequest import \
    GetDataOperationJobExecutionIntegrationListRequest
from pdi.application.operation.GetDataOperationJobExecutionIntegrationList.GetDataOperationJobExecutionIntegrationListResponse import \
    GetDataOperationJobExecutionIntegrationListResponse


@dataclass
class GetDataOperationJobExecutionIntegrationListQuery(IQuery[GetDataOperationJobExecutionIntegrationListResponse]):
    request: GetDataOperationJobExecutionIntegrationListRequest = None
