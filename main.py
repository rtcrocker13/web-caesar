from flask import Flask, request
from caesar import rotate_string 


app = Flask(__name__)
app.config['DEBUG'] = True

header = """
<h2>Web Caesar</h2>
"""

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
      <textarea name = "text">{0}</textarea>
      <br>
      <input type = "text" value="0" id = "rot" name = "rot" />
      <br>
      <input type ="submit" />
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")


@app.route("/", methods=['POST'])
def encrypt():
    text = request.form["text"]
    rot = request.form["rot"]
    rotInt = int(rot)

    result=rotate_string(text, rotInt)
    resultFormatted = form.format(result)
    return "<h1>"+resultFormatted+"</h1>"


app.run()