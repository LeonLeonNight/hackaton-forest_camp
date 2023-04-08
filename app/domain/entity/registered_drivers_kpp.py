from app.myapp import db, flask_bcrypt

class Registered_drivers_kpp(db.Model):

    __tablename__ = "registered_drivers_kpp"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pass_number = db.Column(db.String(15), unique=True, nullable=False)
    auto_number = db.Column(db.String(15), unique=False, nullable=True)
    status = db.Column(db.Integer, unique=False, nullable=True)
    
    def __repr__(self):
        return "<Registered_drivers_kpp '{}'>".format(self.registered_drivers_kpp_name)
