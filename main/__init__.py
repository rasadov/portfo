from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = 'fPfKdLHcBn7JOCeDxPORUns0ZSo9i4HY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


from main import routes


# with app.app_context():
    # project1 = routes.Projects(title='News Filterer',text='Scraps data from Hacker News and filters it based on points', link='https://github.com/rasadov/News_filterer.git')
    # project2 = routes.Projects(title='Web Store',text='Fun MarketPlace with User Authentification and SQLite Database.', link='https://github.com/rasadov/Web-Store.git')
    # db.session.add(project1)
    # db.session.add(project2)
    # db.session.commit()
