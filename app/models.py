from app import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(500), index=True, unique=False)
    score = db.Column(db.Integer, index=True, unique=False)
    location = db.Column(db.String(10), index=True, unique=False)

    def __repr__(self):
        return '<Score %r>' % (self.score)
