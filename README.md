# mind_space
## Table of Contents:
* [General Information](#general-information)
* [Hosted Application Access](#hosted-application-access)
* [Technology Stack](#technology-stack)
* [How to use](#how-to-use) 
* [Requirements](#requirements)
* [Setting up the development environment](#setting-up-the-development-environment)

## General Information
Keep organised with a sticky note alternative 😃

## Hosted Application Access
~~http://mind-space.azurewebsites.net/~~

## Technology Stack
* Python 3.8
* Flask
* jQuery
* Bootstrap
* HTML and CSS
* SQLAlchemy
* Web Deployment: Kudu
* Azure SQL database

## How to use
### How it looks
![image](https://user-images.githubusercontent.com/60835426/92992419-2669f380-f52e-11ea-92f6-920079af209e.png)
### Adding a note
![image](https://user-images.githubusercontent.com/60835426/92433492-a61b5980-f1e0-11ea-96e9-58e313e652df.png)
### When a note is created
![image](https://user-images.githubusercontent.com/60835426/92433583-de229c80-f1e0-11ea-8924-826f73c72dcf.png)
### Dragging boxes
Boxes are draggable and coordinates are updated in the database. This means that it looks the same when the application is reopened <br />  
![movingBox](https://user-images.githubusercontent.com/60835426/92434982-90a82e80-f1e4-11ea-9f58-2033b25cc586.gif)
### Deleting boxes
Dragging the box and dropping it into the bin will remove the note from the database and screen <br />  
![deleteBox](https://user-images.githubusercontent.com/60835426/92435343-7884df00-f1e5-11ea-868e-4aa9bd9658a8.gif)


## Requirements
```
click==7.1.2
Flask==1.1.2
Flask-SQLAlchemy==2.4.4
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
SQLAlchemy==1.3.19
Werkzeug==1.0.1
```
## Setting up the development environment
```
$ git clone https://github.com/N-Tandiono/mind_space.git
$ cd mind_space
$ sudo apt-get install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install flask
$ flask run
```
