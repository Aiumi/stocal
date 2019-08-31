from app import app, db
from app.models import User, Company, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Company': Company 'Post': Post}

