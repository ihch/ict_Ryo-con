#! /usr/bin/python3
# -*- coding:utf-8 -*-
from flask import Flask, request
from logging import getLogger, StreamHandler, DEBUG
import json
import open_csv
import func
app = Flask(__name__)

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

filename = open_csv.filename

@app.route('/user_init/')
def start_user_init():
    user_name = request.args.get('user_name')
    major = request.args.get('major')
    minor = request.args.get('minor')
    notice = request.args.get('notice')
    atnd = request.args.get('atnd')

    isSuccess = False
    with open_csv.open_csv(filename=filename, opentype='a') as fa:
        isSuccess = func.user_init(
                user_info=[user_name, major, minor, notice, atnd], fa=fa)
    if isSuccess:
        return 'user_init: successed'
    else:
        return 'user_init: filed'

@app.route('/update/beacon/')
def start_update_beacon():
    user_name = request.args.get('user_name')
    major = request.args.get('major')
    minor = request.args.get('minor')

    isSuccess = False
    with open_csv.open_csv(filename=filename, opentype='r') as fr:
        isSuccess = func.update_info(
                user_info=[user_name, major, minor], fr=fr, change_list=[1, 2])
    if isSuccess:
        return 'update_beacon: successed'
    else:
        return 'update_beacon: filed'

@app.route('/update/notice/')
def start_update_notice():
    user_name = request.args.get('user_name')
    notice = request.args.get('notice')

    isSuccess = False
    with open_csv.open_csv(filename=filename, opentype='r') as fr:
        isSuccess = func.update_info(
                user_info=[user_name, notice], fr=fr, change_list=[3])
    if isSuccess:
        return 'update_notice: successed'
    else:
        return 'update_notice: filed'

@app.route('/update/attendance/')
def start_update_attendance():
    user_name = request.args.get('user_name')
    atnd = request.args.get('atnd')

    isSuccess = False
    with open_csv.open_csv(filename=filename, opentype='r') as fr:
        isSuccess = func.update_info(
                user_info=[user_name, atnd], fr=fr, change_list=[4])
    if isSuccess:
        return 'update_attendance: successed'
    else:
        return 'update_attendance: filed'

@app.route('/get_data/')
def start_get_data():
    res = None
    with open_csv.open_csv(filename=filename, opentype='r') as fr:
        res = func.get_data(fr=fr)
    if res is None:
        return 'null'
    else:
        return json.dumps({'data':res})

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=8080)

