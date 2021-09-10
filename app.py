from flask import Flask, render_template, request, jsonify
import os
import yaml 
import joblib
import numpy as np

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder = static_dir, template_folder = template_dir)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config
 
def predict(data):
    config = read_params(params_path)
    model_dir_path= config['webapp_model_dir']
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print(prediction)
    return prediction

def api_response(request):
    pass





@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            if request.form:  # if the request if coming from thw web application. these values are in the form of dictionary and we will take values only
                data = dict(request.form).values()
                data = [list(map(float,data))]  #mapping all the values into float form
                response = predict(data)
                return render_template('index.html', response = response)
            
            elif request.json: # if we dnt want to enter the details and etails are coming form some api in the form of json
                response = api_response(request)
                return jsonify(response)


        except Exception as e:
            print(e)
            error = {'error':'Something wnet wrong!! Try again...'}
            return render_template('404.html', error = error)   # in order to put our own error message we use 404.html
        pass
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)