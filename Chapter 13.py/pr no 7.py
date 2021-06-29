
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="s7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl"ha384-BmbxuPwQa2lc/FVzBcNJ crossorigin="anonymous"> '''
if __name__ == "__main__":
    app.run(debug=True)

    # thus we can make a website as a internal server