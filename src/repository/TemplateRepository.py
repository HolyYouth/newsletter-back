from src.util.MongoDBHelper import getTemplatedb
import pymongo


templateDB = getTemplatedb()

def getTemplateList():
    templates = []
    for Template in templateDB.find({},{'_id':0}):
        # print(Template)
        templates.append(Template)       
    print(templates)
    return templates

def getTemplateById(args):
    if 'id' in args:
        template = templateDB.find_one({'id':int(args['id'])},{'_id':0})
        print(args['id'])
        if template is not None:
            return template
        else:
            return 'template not found!'
    else:
        return 'No ID received!'

def newTemplate(args):
    newId = 0
    if 'templateName' in args and 'createdBy' in args and 'createdTime' in args and 'lastModifiedBy' in args and 'lastModifiedTime' in args and 'DDL' in args:
        for id in templateDB.find({},{'_id':0,'id':1},sort=[('id',pymongo.DESCENDING)],limit=1):
            # print(id)
            newId = int(id['id']) + 1
        args['id'] = newId
        args['isAlive'] = True
        templateDB.insert_one(args)
        return 'New template success!'
    else:
        return 'Information missed, new template failed!'
    
def deleteTemplate(args):
    if 'id' in args:
        templateDB.delete_one({'id':int(args['id'])})
        return 'Successfully deleted!'
    else:
        return 'Failed to delete'

def modifyTemplate(args):
    if 'id' in args:
        templateDB.update_one({'id':int(args['id'])},{'$set':{'templateName':args['templateName'],'lastModifiedBy':args['lastModifiedBy'],'lastModifiedTime':args['lastModifiedTime'],'DDL':args['DDL'],'isAlive':args['isAlive']}})
        return 'Modify success'
    else:
        return 'Failed to modify'
