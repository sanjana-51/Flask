from flask import Flask
app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome Sanjana'

@app.route('/members')
def members():    #function should be differnt
    return 'Heyy guyzz'

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is "+ str(score)



if __name__=='__main__':
    app.run(debug=True)
 