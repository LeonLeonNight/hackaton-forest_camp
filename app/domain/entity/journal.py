from app.myapp import db

class Journal(db.Model):
    __tablename__ = "journal"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pass_number = db.Column(db.String(15),unique=True, nullable=False)
    auto_number = db.Column(db.String(15), unique=False, nullable=True)
    driver = db.Column(db.String(255), unique=False, nullable=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    kpp_id = db.Column(db.Integer, db.ForeignKey('kpp.id'))
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'))
    count = db.Column(db.Float, nullable=True, default=False)
    measurement_system_type_id = db.Column(db.Integer, db.ForeignKey('measurement_system_type.id'))

    def __repr__(self):
        return "<Journal '{}'>".format(self.name)    