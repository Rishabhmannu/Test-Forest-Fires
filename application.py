from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application


## import ridge regression and lasso regression models
# lasso_model=pickle.load(open('lassocv_Algerian_forest_fires.pkl','rb'))
# elastic_model=pickle.load(open('elasticcv_Algerian_forest_fires.pkl','rb'))

ridge_model = pickle.load(open('models/ridge_Algerian_forest_fires.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler_Algerian_forest_fires.pkl', 'rb'))


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))

        new_data=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data)

        return render_template('home.html',result=result[0])
    else:
      return render_template('home.html')
        

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)