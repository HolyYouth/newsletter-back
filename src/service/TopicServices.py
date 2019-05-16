from flask import Flask,jsonify,request
from .. import app
from src.repository import TopicRepository
from src.util.HttpRequestsHelper import requestsHelper
import os
from werkzeug.utils import secure_filename


@app.route('/getTopicsAndContentsByTemplateId/',methods=['post'])
def getTopicsAndContentsByTemplateId():
    args = requestsHelper(request)
    return jsonify(TopicRepository.getTopicsAndContentsByTemplateId(args))

@app.route('/addTopic/',methods=['post'])
def addTopic():
    f = request.files['file']
    user_input = request.form.get("name")
    basepath = os.path.dirname(__file__)
    upload_path = os.path.join('D:\\code\\newsletter-back\\src\\', 'static\\images', secure_filename(f.filename))
    f.save(upload_path)

    args = requestsHelper(request)
    args['imgSrc']='http://127.0.0.1:5000/static/images/'+f.filename
    return jsonify(TopicRepository.addTopic(args)) 

@app.route('/deleteTopic/',methods=['post'])
def deleteTopic():
    args = requestsHelper(request)
    return jsonify(TopicRepository.deleteTopic(args))