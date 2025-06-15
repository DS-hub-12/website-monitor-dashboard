import os
import json
import io
from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, db

firebase_json = os.environ.get("FIREBASE_CREDENTIALS")
cert_data = json.loads(firebase_json)
cred = credentials.Certificate(cert_data)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://websitemonitor-d6c65-default-rtdb.firebaseio.com/'
})

app = Flask(__name__)

@app.route('/')
def index():
    logs = db.reference("logs").get()
    if logs is None:
        logs = {}  # ✅ prevent crash if DB is empty
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
