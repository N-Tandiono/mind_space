from app import db

# Models
class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    
    # Store colour of the tab (Future Implementation)
    colour = db.Column(db.String(10))

    # Store the time of message posted (Future Implementation)
    time = db.Column(db.String(16))

    # Store the User who posted (Future Implementation)
    user = db.Column(db.String(12))

    # Is the message important? Will be starred
    important = db.Column(db.String(12))

    # Store the title of the message
    name = db.Column(db.String(26))

    # Store the message description
    description = db.Column(db.String(26))

    # Store the xCoordinate
    xCoordinate = db.Column(db.Integer, primary_key=False)

    # Store the yCoordinate
    yCoordinate = db.Column(db.Integer, primary_key=False)
