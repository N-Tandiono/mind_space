from flask import render_template, request, redirect, url_for
from app import app, models, db

Task = models.Task

@app.route('/')
def index():
    title = 'Mind-Space'
    tasks = Task.query.all()
    return render_template("static.html", title=title, tasks=tasks)

# POST (Forms)
@app.route('/task/', methods=['POST'])
def add_item():
    # Get data from form fields taskName and taskDescription
    taskName = request.form.get('taskName')
    taskDescription = request.form.get('taskDescription')
    
    # if not taskName:
    #     print("No TaskName!")
    #     return redirect(url_for('index'))

    # if not taskDescription:
    #     print("No DESCRIPTION!")
    #     return redirect(url_for('index'))

    # Put data into a new Task item
    new_item = Task(name=taskName, description=taskDescription)
    
    # Add and commit the changes to the database
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))