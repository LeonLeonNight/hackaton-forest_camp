from abc import ABC, abstractmethod
from typing import List
import attr
from app.domain.exception import GoodsNotFound
from app.domain.entity.goods import (Goods, ExtraGoods, BasicGoods)


@attr.s(auto_attribs=True)
class GoodsRepository(ABC):
    _goodsAll:List[Goods]

    @abstractmethod
    def get_goods(self, id: int) -> Goods:
        goods = next((x for x in self._goodsAll 
                        if x.id == id),None)
        return goods
    
    
    @abstractmethod
    def create_goods(self, goods: Goods) -> None:
        self._goodsAll.append(goods)
    

    @abstractmethod
    def update_goods(self, id: int, goods: Goods) -> None:
        goods = next((x for x in self._goodsAll 
                        if x.id == id), None)
        if goods:
            goods.goods = goods
        else:
            raise GoodsNotFound()