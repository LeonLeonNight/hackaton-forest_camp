from app.application import db

class Client(db.Model):

    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False)

    journals = db.relationship('Journal', backref='journal')

    def __repr__(self):
        return "<Client '{}'>".format(self.name)    