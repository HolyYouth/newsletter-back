import pymongo

def getDB():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    return client.newsletter

def getTemplatedb():
    templatedb = getDB().templates
    return templatedb

def getTopicdb():
    topicdb = getDB().topics
    return topicdb

def getContentdb():
    contentdb = getDB().contents
    return contentdb

def getHeaddb():
    headdb = getDB().heads
    return headdb
