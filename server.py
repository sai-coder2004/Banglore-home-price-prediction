from flask import Flask,request,jsonify,render_template,url_for,redirect,json
import utility
app=Flask(__name__)
@app.route("/")
def fun():
    return render_template('app.html')
@app.route("/get_locations",methods=['GET'])
def get_location():
    response=jsonify({
        'locations':utility.get_locations()
    })
    return response
@app.route("/submit",methods=['POST','GET'])
def predict():
    try:
        sqft=float(request.form['total_sqft'])
        location= (request.form['location'])
        bhk=float(request.form['bhk'])
        bath=float(request.form['bath'])
        response=json.dumps({
            'estimated_price in Lakhs':utility.get_estimated_price(location,sqft,bhk,bath)
        })
        if sqft>=100 and bhk>=1 and bath>=1:
            return render_template('price.html',Response=response)
            
        else:
            return render_template('price.html',Response="Please enter appropriate values")
    except:
        return "Enter appropriate values"
         


    





    


if __name__=="__main__":
    utility.load()
    app.run(debug=True)
















