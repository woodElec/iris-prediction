import pickle

from flask import Flask, request, jsonify


app = Flask(__name__)


with open('logistic_model.pkl', 'rb') as f:
    logistic_model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


@app.route('/predict', methods=['GET'])
def predict():
    print("entre a predict")
    if request.method == 'GET':
        prediction = None
        data = request.json
        x = data.get("features", [])
        if len(x) != 0:
            scaled_x = scaler.transform(x)
            prediction = logistic_model.predict(scaled_x)
            prediction = prediction.tolist()
    return jsonify(prediction)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
