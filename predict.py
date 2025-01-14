import pickle
import numpy as np

from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor

from flask import Flask
from flask import request
from flask import jsonify

app = Flask('saleprice')
model_file = 'model.bin'

with open(model_file, 'rb') as model:
    dv, model = pickle.load(model)

# Use this decorator: this will be the predict that gives you the output of a request
@app.route('/predict', methods=['POST'])
def predict():
    # Get your house informations
    house = request.get_json()
    
    # Make your prediction using the loaded model and dv
    X = dv.transform([house])
    y_pred = model.predict(X)
    y_pred = np.expm1(y_pred)
    
    # Obtain the result: you have to specify the type of the variables
    result = {
        'saleprice': int(y_pred)
    }
    
    # Return your result in a json format
    return jsonify(result)

# Here, when you run your script with python in dev environment, you can debug it
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
