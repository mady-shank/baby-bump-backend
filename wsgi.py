from main import app
import os
from os import getenv
from dotenv import load_dotenv
from flask_session import Session

sess = Session()


load_dotenv()

if __name__ == '__main__':
    app.secret_key = os.getenv("secret_key")

    sess.init_app(app)

    app.run()
