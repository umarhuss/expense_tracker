from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

from app import routes
