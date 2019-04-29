from flask import Flask,jsonify,request
from .. import app
from src.repository import HeadRepository
from src.util.HttpRequestsHelper import requestsHelper

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
    args = requestsHelper(request)
    return jsonify(HeadRepository.newHeader(args))

@app.route('/modifyHeader/',methods=['post'])
def modifyHeader():
    args = requestsHelper(request)
    return jsonify(HeadRepository.modifyHeader(args))
