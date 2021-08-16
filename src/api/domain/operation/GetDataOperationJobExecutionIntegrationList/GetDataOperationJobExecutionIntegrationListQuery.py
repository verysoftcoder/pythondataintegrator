from dataclasses import dataclass
from infrastructure.cqrs.IQuery import IQuery
from domain.operation.GetDataOperationJobExecutionIntegrationList.GetDataOperationJobExecutionIntegrationListRequest import GetDataOperationJobExecutionIntegrationListRequest
from domain.operation.GetDataOperationJobExecutionIntegrationList.GetDataOperationJobExecutionIntegrationListResponse import GetDataOperationJobExecutionIntegrationListResponse


@dataclass
class GetDataOperationJobExecutionIntegrationListQuery(IQuery[GetDataOperationJobExecutionIntegrationListResponse]):
    request: GetDataOperationJobExecutionIntegrationListRequest = None
