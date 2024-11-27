from flask import Flask, render_template ,request ,redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default="Not Started")
    

    def __repr__(self) -> str:
        return f'{self.sno} - {self.title} - - {self.date} - {self.status}'

@app.route("/", methods=['GET','POST'])
def hello_world():
    if request.method=="POST":
        title=request.form['title']
        desc=request.form['desc']
        ddate=request.form['ddate']
        status=request.form['status']
        date_obj = datetime.strptime(ddate, '%Y-%m-%d').date()
        todo=Todo(title=title, desc=desc , date=date_obj, status=status)
        db.session.add(todo)
        db.session.commit()
    alltodo=Todo.query.all()
    return render_template('index.html', alltodo=alltodo)



@app.route("/update/<int:sno>", methods=['GET','POST'])
def update(sno):
    if request.method=="POST":
        title=request.form['title']
        desc=request.form['desc']
        ddate=request.form['ddate']
        status=request.form['status']
        date_obj = datetime.strptime(ddate, '%Y-%m-%d').date()
        todo=Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        todo.date=date_obj
        todo.status=status
        db.session.commit()
        return redirect('/')

    todo=Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route("/delete/<int:sno>", methods=['GET','POST'])
def delelte(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route("/about")
def about():
    return render_template('about.html')



@app.route("/search")
def feature_not_implemented():
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)