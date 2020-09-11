from flask import render_template, request, redirect, url_for
from app import app, models, db

Note = models.Note

@app.route('/')
def index():
    title = 'Mind-Space'
    notes = Note.query.all()
    return render_template("static.html", title=title, notes = notes)

# POST (Forms)
@app.route('/notes/', methods=['POST'])
def add_item():
    # Get data from form fields taskName and taskDescription
    noteName = request.form.get('taskName')
    noteDescription = request.form.get('taskDescription')
    noteImportant = request.form.get('taskImportant')
    noteColour = request.form.get('Pick a Colour')

    xCoordinate = 30
    yCoordinate = 30
    new_item = Note(name=noteName, description=noteDescription, important=noteImportant, colour=noteColour, xCoordinate=xCoordinate, yCoordinate=yCoordinate)
    
    # Add and commit the changes to the database
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

# UPDATE COORDINATES
@app.route('/notes/update/<int:id>/<float:xcoord>/<int:ycoord>/', methods=['GET', 'POST'])
def update_item(id = 0, xcoord = 0, ycoord = 0):
    print("WE ARE GONNA UPDATE!")
    xcoord = xcoord - (255 * (id - 1))
    ycoord = ycoord - 80
    update = Note.query.filter_by(id=id).first()
    update.xCoordinate = xcoord
    update.yCoordinate = ycoord
    db.session.commit()

    return redirect(url_for('index'))

# Delete from 
@app.route('/notes/delete/<int:id>/<float:xcoord>/<int:ycoord>/', methods=['GET', 'POST'])
def delete_item(id = 0, xcoord = 0, ycoord = 0):

    toRemove = Note.query.filter_by(id = id).first()
    toCheck = toRemove.id
    db.session.delete(toRemove)
    db.session.commit()

    notes = Note.query.all()
    for note in notes:
        if note.id > toCheck:
            note.id -= 1

    db.session.commit()
    return redirect(url_for('index'))