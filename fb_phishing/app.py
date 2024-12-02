from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def Index():
    email = request.form.get("email")
    password = request.form.get("password")
    global details1
    details1 = {"Email": email, "Password": password}  # Save details1 for use in other routes
    return render_template("index.html")


@app.route("/json_data")
def json_data():
    # Return details1 as JSON response
    return jsonify(details1)

if __name__ == "__main__":
    app.run(debug=True)
