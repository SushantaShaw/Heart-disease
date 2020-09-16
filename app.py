from flask import Flask,render_template,request,jsonify
import pickle
from flask_cors import CORS,cross_origin

app=Flask(__name__)


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            age = float(request.form['age'])
            sex = float(request.form['sex'])
            cp = float(request.form['cp'])
            trestbps = float(request.form['trestbps'])
            chol = float(request.form['chol'])
            fbs = float(request.form['fbs'])
            restecg = float(request.form['restecg'])
            thalach = float(request.form['thalach'])
            exang = float(request.form['exang'])
            oldpeak = float(request.form['oldpeak'])
            slope = float(request.form['slope'])
            ca = float(request.form['ca'])
            thal = float(request.form['thal'])

            filename = 'modelprediction.pickle'
            # loading the model file from the storage
            loaded_model = pickle.load(open(filename, 'rb'))
            # predictions using the loaded model file
            prediction = loaded_model.predict_proba(
                [[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                  exang, oldpeak, slope, ca, thal]])[0][1]
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction=round(prediction*100))
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
