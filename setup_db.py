from app import app, db
from app.models import Note

db.drop_all()
db.create_all()

notes = []

for note in notes:
    new_note = Note(name=note, colour = grey, user = admin, important = 'True', description='')
    db.session.add(new_note)
db.session.commit()