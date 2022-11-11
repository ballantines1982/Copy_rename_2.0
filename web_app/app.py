from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
app.add_url_rule("/", "hello", index)

@app.route("/about")
def about():
    return "About Peter"

@app.route("/dynamic/<int:args>")
def dynamic(args):
    return "%s" % args
    
if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug=True)