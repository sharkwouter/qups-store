from app import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aantal = db.Column(db.Integer)
    prijs = db.Column(db.Float)
    adres = db.Column(db.String(128))
    postcode = db.Column(db.String(128))
    plaats = db.Column(db.String(128))


    def __repr__(self):
        return '<Order {}, {}>'.format(self.id, self.aantal)
