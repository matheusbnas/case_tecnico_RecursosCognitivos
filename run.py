# run.py
from dotenv import load_dotenv
import os
from escola_manager import create_app

load_dotenv()
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
