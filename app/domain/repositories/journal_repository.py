from abc import ABC, abstractmethod
from typing import List
import uuid, attr
from app.domain.exception import JournalNotFound
from app.domain.entity.journal import (Journal, ExtraJournal, BasicJournal)


@attr.s(auto_attribs=True)
class JournalRepository(ABC):
    _Journals:List[Journal]

    @abstractmethod
    def get_Journal(self,
                    Journal_type: str, 
                    Journal_id: uuid) -> Journal:
        Journal = next((x for x in self._Journals 
                        if x.id == Journal_id 
                        and x.Journal_type == Journal_type
                        ),None)
        return Journal
    
    
    # @abstractmethod
    # def create_Journal(self, Journal: Journal) -> None:
    #     self._Journals.append(Journal)
    

    # @abstractmethod
    # def update_Journal_basic(self, 
    #                          Journal_type: str, 
    #                          Journal_id: uuid, 
    #                          basic_Journal: BasicJournal) -> None:
    #     Journal = next((x for x in self._Journals 
    #                     if x.id == Journal_id 
    #                     and x.Journal_type == Journal_type
    #                     ), None)
    #     if Journal:
    #         Journal.basic_Journal = basic_Journal
    #     else:
    #         raise JournalNotFound()
    

    # @abstractmethod
    # def update_Journal_extra(self, 
    #                          Journal_type, 
    #                          Journal_id: uuid, 
    #                          extra_Journals: List[ExtraJournal]) -> None:
    #     Journal = next((x for x in self._Journals 
    #                     if x.id == Journal_id 
    #                     and x.Journal_type == Journal_type
    #                     ), None)
    #     if Journal:
    #         Journal.extra_Journal = extra_Journals
    #     else:
    #         raise JournalNotFound()