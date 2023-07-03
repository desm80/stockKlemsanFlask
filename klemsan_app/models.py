from klemsan_app import db


class KlemsanStock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_number = db.Column(db.String(16), nullable=False)
    amount = db.Column(db.Integer)
    store = db.Column(db.String(16))
