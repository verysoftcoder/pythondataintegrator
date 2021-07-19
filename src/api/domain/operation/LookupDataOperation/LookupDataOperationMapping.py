from typing import List
from domain.operation.LookupDataOperation.LookupDataOperationDto import LookupDataOperationDto
from models.dao.operation.DataOperation import DataOperation


class LookupDataOperationMapping:
    @staticmethod
    def to_dto(entity: DataOperation) -> LookupDataOperationDto:
        dto = LookupDataOperationDto()
        dto.Id=entity.Id
        dto.Name=entity.Name
        return dto

    @staticmethod
    def to_dtos(entities: List[DataOperation]) -> List[LookupDataOperationDto]:
        result: List[LookupDataOperationDto] = []
        for entity in entities:
            dto = LookupDataOperationMapping.to_dto(entity=entity)
            result.append(dto)
        return result
