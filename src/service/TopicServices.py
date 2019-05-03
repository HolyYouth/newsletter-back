from flask import Flask,jsonify,request
from .. import app
from src.repository import TopicRepository
from src.util.HttpRequestsHelper import requestsHelper

@app.route('/getTopicsAndContentsByTemplateId/',methods=['post'])
def getTopicsAndContentsByTemplateId():
    args = requestsHelper(request)
    return jsonify(TopicRepository.getTopicsAndContentsByTemplateId(args))

@app.route('/addTopic/',methods=['post'])
def addTopic():
    args = requestsHelper(request)
    return jsonify(TopicRepository.addTopic(args)) 

@app.route('/deleteTopic/',methods=['post'])
def deleteTopic():
    args = requestsHelper(request)
    return jsonify(TopicRepository.deleteTopic(args))