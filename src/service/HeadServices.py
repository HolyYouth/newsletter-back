from flask import Flask,jsonify,request
from .. import app
from werkzeug.utils import secure_filename
from src.repository import HeadRepository
from src.util.HttpRequestsHelper import requestsHelper
import os

@app.route('/getHeadlineByTemplateId/',methods=['post'])
def getHeadlineByTemplateId():
    args = requestsHelper(request)
    return jsonify(HeadRepository.getHeadlineByTemplateId(args))

@app.route('/newHeadline/',methods=['post'])
def newHeadline():
    args = requestsHelper(request)
    return jsonify(HeadRepository.newHeadline(args))

@app.route('/modifyHeadline/',methods=['post'])
def modifyHeadline():
    args = requestsHelper(request)
    return jsonify(HeadRepository.modifyHeadline(args))

@app.route('/getHeaderByTemplateId/',methods=['post'])
def getHeaderByTemplateId():
    args = requestsHelper(request)
    return jsonify(HeadRepository.getHeaderByTemplateId(args))

@app.route('/newHeader/',methods=['post'])
def newHeader(): 
    f = request.files['file']
    user_input = request.form.get("name")
    basepath = os.path.dirname(__file__)
    upload_path = os.path.join('D:\\code\\newsletter-back\\src\\', 'static\\images', secure_filename(f.filename))
    f.save(upload_path)
    
    args = requestsHelper(request)
    args['imgSrc']='http://127.0.0.1:5000/static/images/'+f.filename
    # print(open(upload_path, "rb").read())
    # print(args)
    return jsonify(HeadRepository.newHeader(args))
    


@app.route('/modifyHeader/',methods=['post'])
def modifyHeader():
    args = requestsHelper(request)
    return jsonify(HeadRepository.modifyHeader(args))
