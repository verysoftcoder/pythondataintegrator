from typing import List

from pdip.cqrs.decorators import responseclass

from pdi.application.connection.LookupConnectionType.LookupConnectionTypeDto import LookupConnectionTypeDto


@responseclass
class LookupConnectionTypeResponse:
    Data: List[LookupConnectionTypeDto] = None
