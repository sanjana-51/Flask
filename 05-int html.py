from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)                                   # request= read the posted value

@app.route('/')
def welcome():
    return render_template('new.html')



@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',result=res)
    
    
    
    
       
    return render_template('result.html')

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

# Result checker html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':  # name in[]
        # by default it is string
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4

        res=""
        if total_score>=50:
            res="success"
        else:
            res="fail"
                        # url for = dynmic url generation
        return redirect(url_for(res,score=total_score))
        



if __name__=='__main__':
    app.run(debug=True)
 