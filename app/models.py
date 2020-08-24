from app import db

# Models
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    colour = db.Column(db.String(10))
    name = db.Column(db.String(64))
    description = db.Column(db.String(512))
