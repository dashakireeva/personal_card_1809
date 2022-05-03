from flask import Flask, render_template, request
from flask import url_for
import json

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('index1.html', title = "По каютам", news=news_list)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')