from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import TodoForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gsrhe57345tg4536werft4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from database import Todo


@app.route('/', methods=['GET', 'POST'])
def create():
	form = TodoForm()
	if form.validate_on_submit():
		data = Todo(title=form.title.data, content=form.content.data)
		db.session.add(data)
		db.session.commit()
		return redirect(url_for('create'))
	todos = Todo.query.all()
	return render_template('list.html', todos=todos, form=form)


@app.route('/delete/<int:id>')
def delete(id):
	remove_todo = Todo.query.filter_by(id=id).first()
	db.session.delete(remove_todo)
	db.session.commit()
	return redirect(url_for('create'))
	

if __name__ == '__main__':
	app.run()
