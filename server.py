from flask import Flask, render_template, request, redirect

from users import user
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)