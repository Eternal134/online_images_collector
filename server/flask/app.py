import sys, os
from flask import Flask, request, Response, jsonify

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import spider

app = Flask(__name__)
app.debug = True
app.config['JSON_AS_ASCII'] = False

@app.route("/api/crawlImages", methods=['GET', 'POST'])
def crawlWebImages() -> Response:
    
    try:
        url = request.form['urls']
        return jsonify(spider.crawl(url))
    except Exception as e:
        return jsonify(str(e))