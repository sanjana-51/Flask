
# Integrating HTML with Data source
'''
{%...%} = for
{{ }}= print oitput
{#...#} = comment
'''
from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)                                   # request= read the posted value

@app.route('/')
def welcome():
    return render_template('style1_08.html')



@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score,'res':res}
    
    return render_template('result.html',result=exp)
    
    

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
        science=int(request.form['science'])
        maths=int(request.form['maths'])
        c=int(request.form['c'])
        data_science=int(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4

        res=""
        
                        # url for = dynmic url generation
        return redirect(url_for('success',score=total_score))
        



if __name__=='__main__':
    app.run(debug=True)
 