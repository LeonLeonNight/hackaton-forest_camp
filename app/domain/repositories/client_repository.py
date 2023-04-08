from abc import ABC, abstractmethod
from typing import List
import attr
from app.domain.exception import ClientNotFound
from app.domain.entity.client import (Client, ExtraClient, BasicClient)


@attr.s(auto_attribs=True)
class ClientRepository(ABC):
    _clients:List[Client]

    @abstractmethod
    def get_client(self, id: int) -> Client:
        client = next((x for x in self._clients 
                        if x.id == id),None)
        return client
    
    
    @abstractmethod
    def create_client(self, client: Client) -> None:
        self._clinets.append(client)
    

    @abstractmethod
    def update_client(self, id: int, client: Client) -> None:
        client = next((x for x in self._clients 
                        if x.id == id), None)
        if client:
            client.client = client
        else:
            raise ClientNotFound()