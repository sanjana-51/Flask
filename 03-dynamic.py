from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome Sanjana, this is function'



@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is "+ str(score)

## Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""   #declaring variable
    if marks<50:
        result='fail'  #redirect to fail url
    else:
        result='success'    #redirect to success url   
    return redirect(url_for(result,score=marks))    



if __name__=='__main__':
    app.run(debug=True)
 