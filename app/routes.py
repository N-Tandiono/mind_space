from flask import render_template, request, redirect, url_for
from app import app, models, db

Note = models.Note

@app.route('/')
def index():
    title = 'Mind-Space'
    notes = Note.query.all()
    # for note in notes:
    #     print(note.colour)
    return render_template("static.html", title=title, notes = notes)

# POST (Forms)
@app.route('/notes/', methods=['POST'])
def add_item():
    # Get data from form fields taskName and taskDescription
    noteName = request.form.get('taskName')
    noteDescription = request.form.get('taskDescription')
    noteImportant = request.form.get('taskImportant')
    noteColour = request.form.get('Pick a Colour')
    # if not taskName:
    #     print("No TaskName!")
    #     return redirect(url_for('index'))

    # if not taskDescription:
    #     print("No DESCRIPTION!")
    #     return redirect(url_for('index'))
    # Put data into a new Task item 
    new_item = Note(name=noteName, description=noteDescription, important = noteImportant, colour = noteColour)
    
    # Add and commit the changes to the database
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

# UPDATE COORDINATES
@app.route('/notes/update/<int:id1>/<int:xcoord>/<int:ycoord>/', methods=['GET', 'POST'])
def update_item(id1 = "current", xcoord = "xcoord", ycoord = "ycoord"):
    print("WE ARE GONNA UPDATE!")
    print(id1)
    print(xcoord)
    print(ycoord)


    return redirect(url_for('index'))

# DELETE
@app.route('/notes/delete/<string:name>/<int:xcoord>/<int:ycoord>/', methods=['GET', 'POST'])
def delete_item(name = "current", xcoord = 0, ycoord = 0):
    print("WE ARE DELETEING!")
    toRemove = Note.query.filter_by(name = name).first()
    db.session.delete(toRemove)
    db.session.commit()
    return redirect(url_for('index'))