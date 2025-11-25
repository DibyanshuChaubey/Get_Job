from flask import Flask,render_template
app=Flask(__name__,template_folder="../templates")

@app.route("/")
def home():
  return render_template("index.html",fruits=['mango','banana','apple','berries'],msg="Available Fruits : ")

app.run(debug=True)

