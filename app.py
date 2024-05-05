from flask import Flask,render_template, request
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
def predict():
    prediction=model.predict([[int(request.form.get('diagnosis')),
                               int(request.form.get('idh1')),
                               int(request.form.get('tp53')),
                               int(request.form.get('atrx')),
                               int(request.form.get('pten')),
                               int(request.form.get('egfr')),
                               int(request.form.get('cic')),
                               int(request.form.get('fubp1')),
                               int(request.form.get('rb1')),
                               int(request.form.get('notch1')),
                              request.form.get('tenure')]])
    if prediction[0]==0:
        return render_template("index.html",prediction_text=f"The Predicted Grade is GlioBlastoma Multiforme")
    else:
        return render_template("index.html",prediction_text=f"The Predicted Grade is Lower Grade Glioma")
if __name__=="__main__":
    app.run(debug=True)  
    


