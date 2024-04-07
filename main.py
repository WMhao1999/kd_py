from data import index_data
from flask import *
import datetime

app = Flask(__name__)
@app.after_request

def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ

@app.route('/userinfo', methods=['POST'])
def userinfo():
    now = datetime.datetime.now()
    print('POST请求，接口名称: ', '/userinfo' ,'时间：', now, ' ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
    print(request)
    info = dict();
    info['status_code'] = 200
    info['data'] = index_data.indexUserInfoData
    return jsonify(info)

@app.route('/getChargingStationList', methods=['POST'])
def getlist():
    now = datetime.datetime.now()
    print('POST请求，接口名称: ', '/getChargingStationList', '时间：', now, ' ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
    print(request.data)
    info = dict();
    info['status_code'] = 200
    info['data'] = index_data.indexChargingListData
    return jsonify(info)

if __name__ == '__main__':
    app.run(host='192.168.0.164', port=8080, debug=True)