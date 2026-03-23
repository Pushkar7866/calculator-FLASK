from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/", methods=["GET","POST"])
def home():
    result=""
    if request.method=="POST":
       num1=int(request.form["num1"])
       num2=int(request.form["num2"])
       operation=request.form["operation"]
       if operation=="1":
           result=num1+num2
       elif operation=="2":
           result=num1-num2
       elif operation=="3":
           result=num1*num2
       elif operation=="4":
           if num2!=0:
               result=num1/num2
           else:
               result="CANNOT DIVIDE BY ZERO"
       elif operation=="5":
           result=num1**2
       elif operation=="6":
           result=num1**3
       elif operation=="7":
           fact=1
           for i in range(1,num1+1):
              fact=fact*i
              result=fact
       elif operation=="8":
            factorial=[]
            for i in range(1,num1+1):
              if num1%i==0:
                factorial.append(i)
                result=factorial
    return render_template("index.html",result=result)

if __name__=="__main__":
    app.run(debug=True)
