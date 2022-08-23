#Inclusão da Tag V1.0
from flask import Flask, request, json
from joblib import load as load_joblib

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def process_json():

    data = json.loads(request.data)

    pipeline = load_joblib("models/sentiments-v2.joblib")

    msg = str(data['message'])

    vector = pipeline.named_steps.vectorizer.transform([msg])

    res = pipeline.named_steps.model.predict(vector)

    return res[0]

