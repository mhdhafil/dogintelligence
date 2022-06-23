import json
from flask import Flask,request,jsonify
from flask_cors import CORS
import joblib



#flask starting
app= Flask(__name__)
CORS(app)

@app.route('/',methods=['POST','GET'])
#prediction function
def predict():
    #getting request from front end
    parms1 = request.args.get('parms1')
    parms2= request.args.get('parms2')
    print('pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp')
    print(parms1,parms2)
    # loading models
    model = joblib.load("dogInt.joblib")



    

    #predicting the prices
    print('pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp')
    re = model.predict([[parms1,parms2]])
    
    
    print('pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp')
    print(re)
    if re[0]<30:
        print('Lowest Degree of Working/Obedience Intelligence')
        return jsonify('Lowest Degree of Working/Obedience Intelligence')
    elif re[0]<40:
        print("Fair Working/Obedience Intelligence")
        return jsonify('Fair Working/Obedience Intelligence')
    elif re[0]<60:
        print("Average Working/Obedience Intelligence")
        return jsonify('Average Working/Obedience Intelligence')
    elif re[0]<80:
        print('Above Average Working Dogs')
        return jsonify('Above Average Working Dogs')
    elif re[0]<90:
        print('Excellent Working Dogs')
        return jsonify('Excellent Working Dogs')
    else:
        print('Brightest Dogs')
        return jsonify('Brightest Dogs')
    # return jsonify(re[0])
    # return pred

if __name__=='__main__':
    app.run()
