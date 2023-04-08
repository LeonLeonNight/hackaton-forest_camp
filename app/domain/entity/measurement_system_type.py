from app.myapp import db

class MeasurementSystemType(db.Model):

    __tablename__ = "measurement_system_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False)

    journals = db.relationship('Journal', backref='journal')

    def __repr__(self):
        return "<MeasurementSystemType '{}'>".format(self.name)    