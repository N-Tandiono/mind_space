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
    important = request.form.get('taskimportant')

    # if not taskName:
    #     print("No TaskName!")
    #     return redirect(url_for('index'))

    # if not taskDescription:
    #     print("No DESCRIPTION!")
    #     return redirect(url_for('index'))

    # Put data into a new Task item 
    new_item = Note(name=noteName, description=noteDescription, important = important)
    
    # Add and commit the changes to the database
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))