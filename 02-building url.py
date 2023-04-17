from flask import Flask
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
@app.route('/result/<int:score>')
def results(score):
    result=""   #declaring variable
    if score<50:
        result='fail'
    else:
        result='pass'
    return result


    




if __name__=='__main__':
    app.run(debug=True)
 