import falcon
import msgpack
import couchdb
from array import array
import json
import os
from faker import Faker
couch = couchdb.Server()

db = couch['dictionary']
dbSearch = couch['job_spec']
dbSearchLog = couch['searchlogs']






############################################################
class Resource(object):
    def on_get(self, req, resp):

        doc=[]
        for item in db.view('searchdoc/searchview'):
            if (item['value']['isDeleted']) == 0:
                doc.append(item)
            resp.body = json.dumps(doc, ensure_ascii=False)
            resp.status = falcon.HTTP_200
            print(item)
############################################################
class getData(object):
    def on_post(self, req, resp):

        test_users = {}
        print("Checking...")
        insert_data = req.media
        doc=[]
        doc_syn = []
        for item in dbSearch.view('jobspecdoc/jobspecview'):
            if insert_data['comment'].lower() in item.value['job_title'].lower():
                doc.append(item.value['job_title'])
        for item_dict in db.view('searchdoc/searchview'):
            if insert_data['comment'].lower() == item_dict.value['job_title'].lower():
                doc_syn=item_dict.value['synonymous']
        for item in dbSearch.view('jobspecdoc/jobspecview'):
            counter=0
            while(counter<len(doc_syn)):
                if doc_syn[counter].lower() == item.value['job_title'].lower():
                    doc.append(doc_syn[counter])
                counter=counter+1
        if not doc:
            doc.append('No Result Found')
        print(doc)                
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
############################################################
class logSearch(object):
    def on_post(self, req, resp):

        insert_data = req.media
        dbSearchLog.save(insert_data)
        doc=[]
        doc.append(insert_data)
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
############################################################
class getDelete(object):
    def on_post(self, req, resp):

  
        insert_data = req.media
        print(insert_data['value']['_id'])
        document=db.get(insert_data['value']['_id'])
        if 'isDeleted' in document:
            document['isDeleted'] = 1
        db.save(document) #save database
 ############################################################
class UpdateJobTitle(object):
    def on_post(self, req, resp):

    
        insert_data = req.media
        document=db.get(insert_data['id'])

        if 'job_title' in document:
            document['job_title'] = insert_data['job_title']
        db.save(document) #save database 

############################################################
class UpdateSyno(object):
    def on_post(self, req, resp):

        insert_data = req.media
        counter_syno = 0
        for item_dict in db.view('searchdoc/searchview'):
            if insert_data['id'] == item_dict['value']['_id']:
                for test in item_dict['value']['synonymous']:
                    if insert_data['CurrentSyno'] == item_dict['value']['synonymous'][counter_syno]:
                        # print(item_dict['value']['synonymous'][counter_syno])
                        doc1=db.get(insert_data['id'])
                        doc1['synonymous'][counter_syno] = insert_data['NewSyno']
                        # print(doc1['synonymous'][counter_syno])
                        db.save(doc1)
                    counter_syno = counter_syno + 1 

############################################################
class UpdateKeywords(object):
    def on_post(self, req, resp):

        insert_data = req.media
        counter_keyword = 0
        for item_dict in db.view('searchdoc/searchview'):
            if insert_data['id'] == item_dict['value']['_id']:
                for test in item_dict['value']['keywords']:
                    if insert_data['CurrentKeyword'] == item_dict['value']['keywords'][counter_keyword]:
                        # print(item_dict['value']['keywords'][counter_keyword])
                        doc1=db.get(insert_data['id'])
                        doc1['keywords'][counter_keyword] = insert_data['NewKeyword']
                        # print(doc1['keywords'][counter_keyword])
                        db.save(doc1)
                    counter_keyword = counter_keyword + 1 
                       
############################################################
class delSyno(object):
    def on_post(self, req, resp):

        insert_data = req.media
        counter_syno = 0
        print(insert_data)
        for item_dict in db.view('searchdoc/searchview'):
            if insert_data['id'] == item_dict['value']['_id']:
                for test in item_dict['value']['synonymous']:
                    if insert_data['syno'] == item_dict['value']['synonymous'][counter_syno]:
                        print(item_dict['value']['synonymous'][counter_syno])
                        doc1=db.get(insert_data['id'])
                        del doc1['synonymous'][counter_syno]
                        db.save(doc1)
                    counter_syno = counter_syno + 1 

############################################################
class delKeywords(object):
    def on_post(self, req, resp):
        
        insert_data = req.media
        print(insert_data)
        counter_keywords = 0
        for item_dict in db.view('searchdoc/searchview'):
            if insert_data['id'] == item_dict['value']['_id']:
                for test in item_dict['value']['keywords']:
                    if insert_data['keywords'] == item_dict['value']['keywords'][counter_keywords]:
                        print(item_dict['value']['keywords'][counter_keywords])
                        doc1=db.get(insert_data['id'])
                        del doc1['keywords'][counter_keywords]
                        db.save(doc1)
                    counter_keywords = counter_keywords + 1 


############################################################
class addSearch(object):
    def on_post(self, req, resp):
        doc = req.media
        get_name = (doc)
        counter_syno = 0
        counter_keyword = 0
        syno_list = []
        keyword_list=[]
        doc_data = {}
        for i in get_name[1]:
             get_syno = get_name[1][counter_syno]['name']
             syno_list.append(get_syno)
             counter_syno = counter_syno + 1
        for i in get_name[1]:
             get_keyword = get_name[0][counter_keyword]['name']
             keyword_list.append(get_keyword)

             counter_keyword = counter_keyword + 1
        doc_data.update({'job_title':get_name[2]}) 
        doc_data.update({'synonymous':syno_list}) 
        doc_data.update({'keywords':keyword_list}) 
        doc_data.update({'isDeleted':0})
        db.save(doc_data)

 ############################################################
app = falcon.API()

 ############################################################
things = Resource()
catchData = getData()
logSearch = logSearch()
addSearch = addSearch()
getDelete = getDelete()
delSyno = delSyno()
UpdateSyno = UpdateSyno()
UpdateJobTitle = UpdateJobTitle()
delKeywords = delKeywords()
UpdateKeywords = UpdateKeywords()

 ############################################################
app.add_route('/UpdateKeywords', UpdateKeywords)
app.add_route('/delKeywords', delKeywords)
app.add_route('/UpdateJobTitle', UpdateJobTitle)
app.add_route('/UpdateSyno', UpdateSyno)
app.add_route('/delSyno', delSyno)
app.add_route('/getDelete', getDelete)
app.add_route('/addSearch', addSearch)
app.add_route('/logSearch', logSearch)
app.add_route('/catchData', catchData)
app.add_route('/things', things)

 ############################################################