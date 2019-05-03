from flask import Flask,jsonify,request
from .. import app
import json
from src.repository import TemplateRepository
from src.util.HttpRequestsHelper import requestsHelper
# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/lulu/')
# def luluzuikeai():
#     return '璐璐最可爱！'

@app.route('/getTemplateList/',methods=['get'])
def getTemplateList():
    templateList = TemplateRepository.getTemplateList() 
    if templateList==[]:
        return ''
    else:
        # print(jsonify(templateList))
        return jsonify(templateList)

@app.route('/getTemplateById/', methods=['post'])
def getTemplateById():
    args = requestsHelper(request)
    return jsonify(TemplateRepository.getTemplateById(args))

@app.route('/newTemplate/',methods=['post'])
def newTemplate():
    args = requestsHelper(request)
    # data = str(request.get_data(),encoding='utf-8')
    # data = request.get_data()
    # data = json.loads(request.get_data())
    # print(args)
    return jsonify(TemplateRepository.newTemplate(args))   

@app.route('/deleteTemplate/',methods=['post'])
def deleteTemplate():
    args = requestsHelper(request)
    return jsonify(TemplateRepository.deleteTemplate(args))

@app.route('/modifyTemplate/',methods=['post'])
def modifyTemplate():
    args = requestsHelper(request)
    return jsonify(TemplateRepository.modifyTemplate(args))