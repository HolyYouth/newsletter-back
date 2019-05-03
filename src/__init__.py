from flask import Flask
from flask_cors import *
app = Flask(__name__)


CORS(app, supports_credentials=True) 

@app.route('/')
def index():
    return 'INDEX PAGE'

from .service import TemplateServices
from .service import TopicServices
from .service import ContentServices
from .service import HeadServices