from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")


#request form from from.html and then send into register.html to show.
@app.route("/register", methods=["POST"])
def register():
    result = request.form
    print(result)
    return render_template("register.html", register = result)

if __name__ == "__main__":
    app.run(debug=True)