from typing import List
from infrastructure.cqrs.decorators.responseclass import responseclass
from domain.dashboard.GetDataOperationJobExecutionWidget.GetDataOperationJobExecutionWidgetDto import GetDataOperationJobExecutionWidgetDto


@responseclass
class GetDataOperationJobExecutionWidgetResponse:
	Data: List[GetDataOperationJobExecutionWidgetDto] = None
