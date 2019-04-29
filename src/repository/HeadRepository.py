from src.util.MongoDBHelper import getHeaddb
import pymongo

headDB = getHeaddb()

def getHeadlineByTemplateId(args):
    if 'templateId' in args:
        headline = None
        print(headDB.find({'templateId':int(args['templateId']),'type':'headline'},{'_id':0}))
        for hl in headDB.find({'templateId':int(args['templateId']),'type':'headline'},{'_id':0}):
            print(hl)
            headline = hl
        if headline is None:
            return 'Headline not found'
        else:
            return headline
    else:
        return 'No templateId received!'

def newHeadline(args):
    if getHeadlineByTemplateId(args) != 'Headline not found':
        return 'Headline exists or bad http request'
    if 'templateId' in args  and 'wordContent' in args and 'imgSrc' in args and 'createdBy' in args and 'createdTime' in args and 'lastModifiedBy' in args and 'lastModifiedTime' in args:
        newId = 0
        for id in headDB.find({},{'_id':0,'id':1},sort=[('id',pymongo.DESCENDING)],limit=1):
            newId = int(id['id']) + 1
        args['id'] = newId
        args['type'] = 'headline'
        args['templateId'] = int(args['templateId'])
        headDB.insert_one(args)
        return 'New headline success!'
    else:
         return 'Information missed, new headline failed!'

def modifyHeadline(args):
    if 'templateId' in args:
        headDB.update_one({'templateId':int(args['templateId'])},{'$set':{'wordContent':args['wordContent'],'imgSrc':args['imgSrc'],'lastModifiedBy':args['lastmodifiedBy'],'lastModifiedTime':args['lastModifiedTime']}})
        return 'Modify success'
    else:
        return 'No templateId received!'

def getHeaderByTemplateId(args):
    if 'templateId' in args:
        header = None
        print(headDB.find({'templateId':int(args['templateId']),'type':'header'},{'_id':0}))
        for h in headDB.find({'templateId':int(args['templateId']),'type':'header'},{'_id':0}):
            print(h)
            header = h
        if header is None:
            return 'Header not found'
        else:
            return header
    else:
        return 'No templateId received!'

def newHeader(args):
    if getHeaderByTemplateId(args) != 'Header not found':
        return 'Header exists or bad http request'
    if 'templateId' in args and 'imgSrc' in args and 'createdBy' in args and 'createdTime' in args and 'lastModifiedBy' in args and 'lastModifiedTime' in args:
        newId = 0
        for id in headDB.find({},{'_id':0,'id':1},sort=[('id',pymongo.DESCENDING)],limit=1):
            newId = int(id['id']) + 1
        args['id'] = newId
        args['type'] = 'header'
        args['templateId'] = int(args['templateId'])
        headDB.insert_one(args)
        return 'New header success!'
    else:
         return 'Information missed, new header failed!'

def modifyHeader(args):
    if 'templateId' in args:
        headDB.update_one({'templateId':int(args['templateId'])},{'$set':{'imgSrc':args['imgSrc'],'lastModifiedBy':args['lastmodifiedBy'],'lastModifiedTime':args['lastModifiedTime']}})
        return 'Modify success'
    else:
        return 'No templateId received!'
    
