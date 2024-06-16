from flask import Flask
import models
from routes import user_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PmrZIfK6NQCVKDQEg1aZD2nb-z3OOhAa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'
models.init_app(app)
app.register_blueprint(user_blueprint)



app.run()