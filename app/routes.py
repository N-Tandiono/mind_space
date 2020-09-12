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

    # Default spawnpoint for boxes
    xCoordinate = 30
    yCoordinate = 30

    # Find how many entities are in the table and assign id accordingly
    count = 0
    counter = Note.query.all()
    for thing in counter:
        count += 1
    count += 1

    new_item = Note(id = count, name=noteName, description=noteDescription, important=noteImportant, colour=noteColour, xCoordinate=xCoordinate, yCoordinate=yCoordinate)
    
    # Add and commit the changes to the database
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

# Update coordinates
@app.route('/notes/update/<int:id>/<float:xcoord>/<int:ycoord>/', methods=['GET', 'POST'])
def update_item(id = -1, xcoord = 0, ycoord = 0):
    # Account for the boxes spawning on top of each other
    xcoord = xcoord - (255 * (id - 1))
    ycoord = ycoord - 80
    update = Note.query.filter_by(id=id).first()
    update.xCoordinate = xcoord
    update.yCoordinate = ycoord
    db.session.commit()

    return redirect(url_for('index'))

# Delete from database
@app.route('/notes/delete/<int:id>/<float:xcoord>/<int:ycoord>/', methods=['GET', 'POST'])
def delete_item(id = -1, xcoord = 0, ycoord = 0):

    toRemove = Note.query.filter_by(id = id).first()
    toCheck = toRemove.id
    
    # Find how many entities there are in the table
    count = 0
    counter = Note.query.all()
    for thing in counter:
        count += 1

    notes = Note.query.all()
    for note in notes:
        # Shift all elements with a id number larger than the deleted down by 1
        # Delete last column id 
        if note.id >= toCheck and note.id < count:
            first = Note.query.filter_by(id=note.id).first()
            secondId = note.id + 1
            second = Note.query.filter_by(id=secondId).first()
            first.name = second.name
            first.description = second.description
            first.important = second.important
            first.colour = second.colour
            first.xCoordinate = second.xCoordinate + 255 # adjust for bug where boxes spawn in same location
            first.yCoordinate = second.yCoordinate
    
    toRemove = Note.query.filter_by(id = count).first()
    db.session.delete(toRemove)
    db.session.commit()

    return redirect(url_for('index'))