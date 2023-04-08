from abc import ABC, abstractmethod
from typing import List
import uuid, attr
from app.domain.exception import Registered_drivers_kppNotFound
from app.domain.entity.registered_drivers_kpp import (Registered_drivers_kpp)


@attr.s(auto_attribs=True)
class Registered_drivers_kppRepository(ABC):
    _Registered_drivers_kpps:List[Registered_drivers_kpp]

    @abstractmethod
    def get_all_registered_drivers_kpps(self,
                    Registered_drivers_kpp_type: str,
                    Registered_drivers_kpp_id: uuid) -> Registered_drivers_kpp:
        registered_drivers_kpp = next((x for x in self._Registered_drivers_kpps
                        if x.id == Registered_drivers_kpp_id
                        and x.Registered_drivers_kpp_type == Registered_drivers_kpp_type
                        ),None)
        return registered_drivers_kpp
    
    
    # @abstractmethod
    # def create_Registered_drivers_kpp(self, Registered_drivers_kpp: Registered_drivers_kpp) -> None:
    #     self._Registered_drivers_kpps.append(Registered_drivers_kpp)
    

    # @abstractmethod
    # def update_Registered_drivers_kpp_basic(self, 
    #                          Registered_drivers_kpp_type: str, 
    #                          Registered_drivers_kpp_id: uuid, 
    #                          basic_Registered_drivers_kpp: BasicRegistered_drivers_kpp) -> None:
    #     Registered_drivers_kpp = next((x for x in self._Registered_drivers_kpps 
    #                     if x.id == Registered_drivers_kpp_id 
    #                     and x.Registered_drivers_kpp_type == Registered_drivers_kpp_type
    #                     ), None)
    #     if Registered_drivers_kpp:
    #         Registered_drivers_kpp.basic_Registered_drivers_kpp = basic_Registered_drivers_kpp
    #     else:
    #         raise Registered_drivers_kppNotFound()
    

    # @abstractmethod
    # def update_Registered_drivers_kpp_extra(self, 
    #                          Registered_drivers_kpp_type, 
    #                          Registered_drivers_kpp_id: uuid, 
    #                          extra_Registered_drivers_kpps: List[ExtraRegistered_drivers_kpp]) -> None:
    #     Registered_drivers_kpp = next((x for x in self._Registered_drivers_kpps 
    #                     if x.id == Registered_drivers_kpp_id 
    #                     and x.Registered_drivers_kpp_type == Registered_drivers_kpp_type
    #                     ), None)
    #     if Registered_drivers_kpp:
    #         Registered_drivers_kpp.extra_Registered_drivers_kpp = extra_Registered_drivers_kpps
    #     else:
    #         raise Registered_drivers_kppNotFound()