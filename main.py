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

def resolveData(request, data):
    now = datetime.datetime.now()
    print('POST请求，时间：', now, ' ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
    print(request.data)
    info = dict();
    info['status_code'] = 200
    if data:
        info['data'] = data
    return jsonify(info)

@app.route('/login', methods=['POST'])
def userlogin():
    return resolveData(request, index_data.loginData)

@app.route('/sendVerCode', methods=['POST'])
def sendVerCode():
    return resolveData(request, index_data.verCodeData)

@app.route('/verCodeLogin', methods=['POST'])
def verCodeLogin():
    return resolveData(request, index_data.loginData)

@app.route('/setRegisterPassword', methods=['POST'])
def setLoginPassword():
    return resolveData(request, index_data.loginData)

@app.route('/userinfo', methods=['POST'])
def userinfo():
    return resolveData(request, index_data.userInfoData)

@app.route('/getBannerListData', methods=['POST'])
def bannerlist():
    return resolveData(request, index_data.bannerListData)

@app.route('/getFilterDetailOption', methods=['POST'])
def filterDetail():
    return resolveData(request, index_data.filterDetailOptions)

@app.route('/setFilterDetailOption', methods=['POST'])
def setFilterDetail():
    return resolveData(request, {})

@app.route('/setQuickFilterOption', methods=['POST'])
def setQuickFilter():
    return resolveData(request, {})

@app.route('/getInCommonUseFilter', methods=['POST'])
def getInUseFilter():
    return resolveData(request, index_data.inCommonUseFilterData)

@app.route('/setInCommonUseFilter', methods=['POST'])
def setInUseFilter():
    return resolveData(request, {})


@app.route('/getChargingStationList', methods=['POST'])
def getlist():
    return resolveData(request, index_data.chargingListData)

@app.route('/getChargingStationDetail', methods=['POST'])
def getchargingdetail():
    return resolveData(request, index_data.chargingdetaildata)


if __name__ == '__main__':
    app.run(host='192.168.0.164', port=8080, debug=True)