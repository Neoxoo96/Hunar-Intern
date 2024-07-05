from flask import Flask, render_template, request, redirect, url_for
from collections import OrderedDict

app = Flask(__name__)

# Sample to-do list (replace with a database for persistence)
tasks = OrderedDict()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_content = request.form["task"]
        tasks[task_content] = False
        return redirect(url_for("index"))  # Redirect to avoid form resubmission
    return render_template("index.html", tasks=tasks)

@app.route("/complete/<task_name>")
def complete(task_name):
    if task_name in tasks:
        tasks[task_name] = True
    return redirect(url_for("index"))

@app.route("/delete/<task_name>")
def delete(task_name):
    if task_name in tasks:
        del tasks[task_name]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)