import imp
from pyexpat import model
from flask import Flask, render_template, request
from features import *
from recommendation import *
import sklearn
import joblib

app = Flask(__name__)

@app.route("/")
def home():
   #render the home page
   return render_template('home.html')

@app.route("/about")
def about():
   #render the about page
   return render_template('about.html')

@app.route('/recommend', methods=['POST'])
def recommend():
   model = joblib.load("model.pkl")
   #requesting the URL form the HTML form
   URL = request.form['URL']
   n = int(request.form['number-of-recs'])
   #using the extract function to get a features dataframe
   df = extract(URL)
   predictions=model.predict(df.values)
   tracks=track_reco(prediction=predictions,n=n)

   return render_template('results.html',songs= tracks['track_name'])


if __name__ == '__main__':
    app.run(debug=True)