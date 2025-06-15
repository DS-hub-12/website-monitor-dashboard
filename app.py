from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, db

firebase_json = os.environ.get("FIREBASE_CREDENTIALS")
cred = credentials.Certificate(json.loads(firebase_json))
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project.firebaseio.com/'
})

app = Flask(__name__)

@app.route('/')
def index():
    logs = db.reference("logs").get()
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
