from abc import ABC, abstractmethod
from typing import List
import attr
from app.domain.exception import KppNotFound
from app.domain.entity.kpp import (Kpp, ExtraKpp, BasicKpp)


@attr.s(auto_attribs=True)
class KppRepository(ABC):
    _kpps:List[Kpp]

    @abstractmethod
    def get_kpp(self, id: int) -> Kpp:
        kpp = next((x for x in self._kpps 
                        if x.id == id),None)
        return kpp
    
    
    @abstractmethod
    def create_kpp(self, kpp: Kpp) -> None:
        self._kpps.append(kpp)
    

    @abstractmethod
    def update_kpp(self, id: int, kpp: Kpp) -> None:
        kpp = next((x for x in self._kpps 
                        if x.id == id), None)
        if kpp:
            kpp.kpp = kpp
        else:
            raise KppNotFound()