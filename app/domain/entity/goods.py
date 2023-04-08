from app.myapp import db

class Goods(db.Model):
    __tablename__ = "goods"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(255), unique=False)
    journals = db.relationship('Journal', backref='goods', lazy='dynamic')

    def __repr__(self):
        return "<Goods '{}'>".format(self.name)    