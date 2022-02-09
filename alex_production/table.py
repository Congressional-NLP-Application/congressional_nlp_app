from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Create user table through User class
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    
    def __repr__(self):
        return "<User: {}>".format(self.name)
    
# Create a tweet table through Tweet class
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    user = db.relationship("User", backref = db.backref('tweets', lazy=True))
    
    def __repr__(self):
        return "<User: {}>".format(self.text)
