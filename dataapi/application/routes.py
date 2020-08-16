from application import app
from application.models import Data

@app.route('/')
def db():
    data = Data.query.all()
    return data[0].name