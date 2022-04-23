from flask import Flask, request, Response, jsonify
from flask_cors import CORS

from response import Response

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import executor
from my_utils import DictUtil

app = Flask(__name__)
app.debug = True
app.config['JSON_AS_ASCII'] = False
# 开启全局跨域
CORS(app, supports_credentials=True)

@app.route("/api/trigger", methods=['GET', 'POST'])
def trigger() -> Response:
    """触发爬虫
    """
    requestId = request.form['requestId']
    try:
        url = request.form['urls']
        # depth参数，默认值为0
        depth = int(request.form.get('depth', 0))
        nextPageLinkText = request.form.get('nextPageLinkText', '')
        return jsonify(DictUtil.objectToDict(executor.trigger(url, requestId, depth, nextPageLinkText)))
    except Exception as e:
        response = Response(requestId)
        response.buildError(str(e))
        return jsonify(DictUtil.objectToDict(response))
    
@app.route("/api/obtain", methods=['GET'])
def obtainResults() -> Response:
    """获取爬虫结果

    Returns:
        Response: _description_
    """
    requestId = request.values['requestId']
    try:
        response = executor.obtainResults(requestId)
        return jsonify(DictUtil.objectToDict(response))
    except Exception as e:
        response = Response(requestId)
        response.buildError(str(e))
        return jsonify(DictUtil.objectToDict(response))