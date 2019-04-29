from flask import Flask,jsonify,request
from .. import app
from src.util.HttpRequestsHelper import requestsHelper
from src.repository import ContentRepository

@app.route('/getContentsByTopicId')
def getContentsByTopicId():
    return 'getContentsByTopicId'

@app.route('/newContent/',methods=['post'])
def newContent():
    args = requestsHelper(request)
    return jsonify(ContentRepository.newContent(args))

@app.route('/modifyContent/',methods=['post'])
def modifyContent():
    args = requestsHelper(request)
    return jsonify(ContentRepository.modifyContent(args))
    