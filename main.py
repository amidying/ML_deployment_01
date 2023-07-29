import pickle
from flask import Flask, render_template, request



# OOPs --->
# Class, Objects, Methods,Inheritance, Polymorphism, Abstruction, Encapsulation, Decorators
# Generators, Dunder Methods, Abstract Methods, Static Method

# 1. Create an object first

app = Flask (__name__,template_folder='template')

# loading the model

model = pickle.load(open("model.pkl","rb"))


# main directory
@app.route("/") #------ whenever anyone hits this url go to the index function
def index():
    return render_template("/index.html")

@app.route("/predict",methods=["GET","POST"])# by default GET Method only 
def predict():
    rsp = request.form.get("temperature")
    if rsp != "":
        try:
            if float(rsp) <0 : 
                return render_template("/index.html",prediction_text=f"Please Enter positive temperature")
            prediction = model.predict([[float(rsp)]]) # ! if valu error occurs might use pip install -U scikit-learn
            output = round(prediction[0],2)
            return render_template("/index.html",prediction_text=f"Total Revenue Generated is: {output}Tk/-")
        except:
            return render_template("/index.html",prediction_text=f"Please input number not characters.")
    else:
        return render_template("/index.html",prediction_text=f"The input must not be blank")


# for final work
if __name__=="__main__":
    app.run(debug=True) # when you select debug = True if any error occurs it will print in the terminal
    
    