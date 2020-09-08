# mind_space
## Table of Contents:
* [General Information](#general-information)
* [How to use](#how-to-use) 
* [Requirements](#requirements)
* [Setup](#setup)

## General Information

## How to use
![image](https://user-images.githubusercontent.com/60835426/92433458-82581380-f1e0-11ea-9140-bc24e2137572.png)

Clicking on the green button results in the following:
![image](https://user-images.githubusercontent.com/60835426/92433492-a61b5980-f1e0-11ea-96e9-58e313e652df.png)

Note boxes are created as shown below:
![image](https://user-images.githubusercontent.com/60835426/92433583-de229c80-f1e0-11ea-8924-826f73c72dcf.png)

Boxes are draggable and update coordinates in database, so it looks the same when the application is reopened
![movingBox](https://user-images.githubusercontent.com/60835426/92434982-90a82e80-f1e4-11ea-9f58-2033b25cc586.gif)

Dragging box and dropping it into the bin will remove the note from the database and screen
![deleteBox](https://user-images.githubusercontent.com/60835426/92435343-7884df00-f1e5-11ea-868e-4aa9bd9658a8.gif)


## Requirements
```
click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
Werkzeug==1.0.1
```
## Setup
```
$ git clone https://github.com/N-Tandiono/mind_space.git
$ cd mind_space
$ sudo apt-get install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install flask
$ flask run
```
