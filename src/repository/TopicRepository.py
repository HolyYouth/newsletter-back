from src.util.MongoDBHelper import getContentdb,getTopicdb
from src.repository.ContentRepository import getContentsByTopicId
import pymongo

topicDB = getTopicdb()

def getTopicsAndContentsByTemplateId(args):
    if 'templateId' in args:
        topics=[]
        for topic in topicDB.find({'templateId':int(args['templateId'])},{'_id':0}):
            topics.append(topic)
        contents=[]
        for topic in topics:
            contents.append(getContentsByTopicId({'topicId':topic['id']}))
        return {'topics':topics,'contents':contents}
    else:
        return 'No templateId received'
        
def addTopic(args):
    if 'templateId' in args and 'fatherId' in args:
        newId = int(args['templateId'] + args['fatherId'])
        args['id'] = newId
        topicDB.insert_one(args)
        return 'Add topic success'
    else:
        return 'Information missed, add topic failed!'

def deleteTopic(args):
    if 'id' in args:
        topicDB.delete_one({'id':int(args['id'])})
        return 'Successfully deleted!'
    else:
        return 'Failed to delete'