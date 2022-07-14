from flask import Flask, request, jsonify
import numpy as np
import pickle
app = Flask(__name__)

@app.route("/")
def home():
    return ("Hello world")
model = pickle.load(open("model.pkl", "rb"))



@app.route("/predict", methods=["GET", "POST"])
def predict():
    Sugar = request.form.get('Sugar')
    BloodUrea = request.form.get('BloodUrea')
    WBC = request.form.get('WBC')
    RBC = request.form.get('RBC')
    Bacteria = request.form.get('Bacteria')
    Hypertension = request.form.get('Hypertension')
    Appetite = request.form.get('Appetite')
    PedalEdema = request.form.get('PedalEdema')
    Anemia = request.form.get('Anemia')

    input_query = np.array([[Sugar, BloodUrea, WBC, RBC, Bacteria, Hypertension, Appetite, PedalEdema, Anemia]])

    result = model.predict(input_query)[0]

    return jsonify({'Chronic kidney Disease': str(result)})
    if __name__ == '__main__':
        app.run(debug=True)

    print(input_query)

    result = model.predict(sc.transform(input_query))
    print(result)
    return jsonify({'placement': str(result)})
if __name__ == '__main__':
    app.run(debug=True)






