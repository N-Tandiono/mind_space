from app import app, db
from app.models import Note

db.drop_all()
db.create_all()

notes = []

for note in notes:
    new_note = Note(id=0, name=note, colour = grey, user = admin, important = 'True', description='', xCoordinate = 30, yCoordinate = 30)
    db.session.add(new_note)
db.session.commit()