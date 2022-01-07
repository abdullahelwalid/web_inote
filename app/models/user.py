from app import db


class NoteModel(db.Model):
    __tablename__ = 'note'
    note_id = db.Column(db.Integer)
    note = db.Column(db.String())