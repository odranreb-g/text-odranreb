from app.extensions import db


class Text(db.Model):
    __tablename__ = "texts"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
