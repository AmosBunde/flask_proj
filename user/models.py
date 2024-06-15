from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(main):
    db.app = main
    db.init_app(main)
    

class User(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    username = db.Column(db.String(255),unique = True)
    password = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean)
    api_key = db.Column(db.String(255),unique =True, nullable= True)
    is_active = db.Column(db.Boolean, default = True)
    authenticated = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<user {self.id} {self.username}>'
    
    def serialize(self):
        return {
            'id':self.id,
            'username': self.username,
            'is_admin': self.is_admin,
            'api_key': self.api_key,
            'is_active': self.is_active
        }