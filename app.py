import os
import json
from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, db

firebase_json = os.environ.get("FIREBASE_CREDENTIALS")
cert_data = json.loads(firebase_json)
cred = credentials.Certificate(io.StringIO(json.dumps(cert_data)))
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://console.firebase.google.com/u/0/project/websitemonitor-d6c65/'
})

app = Flask(__name__)

@app.route('/')
def index():
    logs = db.reference("logs").get()
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
