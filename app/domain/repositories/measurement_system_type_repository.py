from abc import ABC, abstractmethod
from typing import List
import attr
from app.domain.exception import MSTNotFound
from app.domain.entity.measurement_system_type import (MeasurementSystemType, ExtraMST, BasicMST)


@attr.s(auto_attribs=True)
class MSTRepository(ABC):
    _mstList:List[MeasurementSystemType]

    @abstractmethod
    def get_mst(self, id: int) -> MeasurementSystemType:
        mst = next((x for x in self._mstList 
                        if x.id == id),None)
        return mst
    
    
    @abstractmethod
    def create_mst(self, mst: MeasurementSystemType) -> None:
        self._mstList.append(mst)
    

    @abstractmethod
    def update_mst(self, id: int, mst: MeasurementSystemType) -> None:
        mst = next((x for x in self._mstList 
                        if x.id == id), None)
        if mst:
            mst.mst = mst
        else:
            raise MSTNotFound()