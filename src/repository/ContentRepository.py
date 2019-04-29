from src.util.MongoDBHelper import getContentdb
import pymongo


contentDB = getContentdb()

def getContentsByTopicId(args):
    if 'topicId' in args:
        contents = []
        contents.append(contentDB.find({'topicId':int(args['topicId'])}))
        return {args['topicId']:contents}
    else:
        return 'No topicId received'

def newContent(args):
    if 'topicId' in args and 'wordContent' in args and 'templateId' in args and 'layoutType' in args:
        newId = 0
        for id in contentDB.find({},{'_id':0,'id':1},sort=[('id',pymongo.DESCENDING)],limit=1):
            # print(id)
            newId = int(id['id']) + 1    
        args['id'] = newId
        contentDB.insert_one(args)
        return 'New content success'
    else:
        return 'Information missed, new content failed'

def modifyContent(args):
    if 'id' in args and 'topicId' in args and 'wordContent' in args and 'templateId' in args and 'layoutType' in args:
        contentDB.update_one({'id':int(args['id'])},{'$set':{'topicId':args['topicId'],'lastModifiedBy':args['lastModifiedBy'],'lastModifiedTime':args['lastModifiedTime'],'wordContent':args['wordContent'],'imgSrc':args['imgSrc'],'layoutType':args['layoutType']}})
        return 'Modify success'
    else:
        return 'Failed to modify'

