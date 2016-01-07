from . import db


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(256))

    def __repr__(self):
        return '<Todo %r>' % self.id

    def __str__(self):
        return '<Todo %s>' % self.id
