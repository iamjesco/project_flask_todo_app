from app import db
from datetime import datetime


class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), unique=True, nullable=False)
	content = db.Column(db.Text(), nullable=False)
	date = db.Column(db.DateTime, default=datetime.now)
	
	def __repr__(self):
		return self.title
