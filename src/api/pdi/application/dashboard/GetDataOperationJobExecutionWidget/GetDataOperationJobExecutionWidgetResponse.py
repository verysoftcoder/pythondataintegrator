from typing import List

from pdip.cqrs.decorators import responseclass

from pdi.application.dashboard.GetDataOperationJobExecutionWidget.GetDataOperationJobExecutionWidgetDto import \
    GetDataOperationJobExecutionWidgetDto


@responseclass
class GetDataOperationJobExecutionWidgetResponse:
    Data: List[GetDataOperationJobExecutionWidgetDto] = None
