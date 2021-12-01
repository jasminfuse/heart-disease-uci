from flask import Flask, render_template, request
from src.predict_model import standard_classifier, predict

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("form.html")

@app.route('/predict_disease',methods=["POST"])
def predict_disease():
    input_data = list(request.form.to_dict().values())
    converted_inp = [float(x) for x in input_data]
    X_prod_stdsclr = standard_classifier(converted_inp)

    if request.method=="POST":
        result = predict(X_prod_stdsclr)

    return render_template("form.html", prediction_text = "Patient has {}".format(result))


if __name__=="__main__":
    app.run(host="localhost")