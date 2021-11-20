import pandas as pd
from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)
model = joblib.load(open('model.pkl', 'rb'))
scaler = joblib.load(open('scaler.pkl','rb'))

if os.path.isfile("y_encoder.pkl"):
    y_encoder = joblib.load(open('y_encoder.pkl', 'rb'))


@app.route('/predict_api',methods=['POST'])
def predict_api():

    '''
    For direct API calls trought request
    '''

    data = "data.json"
    df = pd.read_json(data, orient='records')
    i=1
    
    for col in df:
        if(df[col].dtype=='object'):
            encoder = joblib.load(open('x_encoder' + str(i) + '.pkl', 'rb'))
            df[col]=encoder.transform(df[col])
            i+=1

    x=df.iloc[:,:].values
    x[:,:]=scaler.transform(x[:,:])
    prediction = model.predict(x)
   
    #Returning class labels


    if os.path.isfile("y_encoder.pkl"):
        prediction = y_encoder.inverse_transform(prediction)
        
    output = {"target" : {"1" : prediction[0]}}
    for i in range(1,len(prediction)):
        output["target"][str(i + 1)] = prediction[i]
    return jsonify(output)

if __name__ == "__main__":  
    app.run(debug=True)
