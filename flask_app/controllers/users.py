from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.users import user

@app.route('/')
def index():
    users = user.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route('/new')
def newUser():
    print("success!")
    return render_template("create.html")

@app.route('/submit', methods=["POST"])
def submit():
    data = {
        "firstName": request.form["firstName"],
        "lastName" : request.form["lastName"],
        "email" : request.form["email"]
    }
    user.save(data)
    return redirect('/')

@app.route('/users/<id>')
def show(id):
    show = user.show(id)
    print(show)
    return render_template("show.html", user_info = show)

@app.route('/user/edit/<id>')
def editor(id):
    show = user.show(id)
    return render_template('edit.html', user_info = show)

@app.route('/edit/<id>', methods=["POST"])
def edit(id):
    data = {
        "id" : id,
        "firstName" : request.form["firstName"],
        "lastName" : request.form["lastName"],
        "email" : request.form["email"]
    }
    user.edit(data)
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    data = {
        "id" : id,
    }
    user.delete(data)
    return redirect('/')
