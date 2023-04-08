from app.myapp import db
from app.domain.entity.goods import Goods


def create_goods(data):
    goods = Goods.query.filter_by(name=data['name']).first()
    if not goods:
        new_goods = Goods(
            name=data['name']
        )
        save_changes(new_goods)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Goods already exists.',
        }
        return response_object, 409

def save_changes(data):
    db.session.add(data)
    db.session.commit()