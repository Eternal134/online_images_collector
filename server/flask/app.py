import sys, os
from flask import Flask, request, Response, jsonify
from flask_cors import CORS

from response import Response

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import spider

app = Flask(__name__)
app.debug = True
app.config['JSON_AS_ASCII'] = False
# 开启全局跨域
CORS(app, supports_credentials=True)

@app.route("/api/crawlImages", methods=['GET', 'POST'])
def crawlWebImages() -> Response:
    response = Response()
    try:
        url = request.form['urls']
        response.data = spider.crawl(url)
    except Exception as e:
        response.buildError(str(e))
    finally:
        return jsonify(response.__dict__)