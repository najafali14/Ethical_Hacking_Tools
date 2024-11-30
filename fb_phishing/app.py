from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods=["POST","GET"])
def Index():
  email = request.form.get("email")
  password = request.form.get("password")
  print(email,password)
  return render_template("index.html")
if __name__ == "__main__":
  app.run(debug=True)
