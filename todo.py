from flask import Flask, render_template,request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/dell/Desktop/TodoApp/todo.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos = Todo.query.all()
    """
    [
        {"id":1,"title":"Test1","content":"Test1,"complete"=0}
    ]
    """
    return render_template("index.html",todos=todos)

@app.route("/add",methods=["POST"])
def addTodo():
    title =  request.form.get("title")
    content = request.form.get("content")
    newTodo = Todo(title = title,content = content, complete = False)

    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def completeTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo.complete == False:
        todo.complete = True
    else:
        todo.complete = False
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/detail/<string:id>")
def detailTodo(id):
    todo = Todo.query.filter_by(id=id).first()

    return render_template("detail.html",todo=todo)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)

if __name__ == '__main__':
    app.run(debug=True)

#Burda SQLAlchemy-i calisdirdiq ve db yaratdiq, python >>> commandlari yazaraq db-de yeni admin user yaratdiq.
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80),unique=True,nullable=False)
#     email = db.Column(db.String(120),unique=True,nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username
