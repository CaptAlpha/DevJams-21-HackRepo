import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model1 = joblib.load(open('ML-Models\Diabetes\model.pkl', 'rb'))
model2 = joblib.load(open('ML-Models\Heart\model.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/predict_diabetes',methods=['POST'])
def predict_diabetes():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model1.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', diabetes_prediction='Diabetes: {}'.format(output), diabetes_bool=1)

@app.route('/predict_heart',methods=['POST'])
def predict_heart():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model2.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', heart_prediction='Heart Disease: {}'.format(output), heart_bool=1)

if __name__ == "__main__":
    app.run(debug=True)