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


# FOR INSERTING MORE FAKER DATA!
# fake = Faker()
# doc_data = {}
# FOR INSERTING MORE FAKER DATA!






class Resource(object):
    def on_get(self, req, resp):


# FOR INSERTING MORE FAKER DATA!

        # for x in range(0, 10):
        #     doc = {
        #         'name': fake.name(),
        #         'address':fake.address(),
        #         'remarks':fake.word()
        #     }
        #     doc_data.update(doc)
        #     db.save(doc)
# FOR INSERTING MORE FAKER DATA!
        doc=[]
        for item in db.view('searchdoc/searchview'):

            doc.append(item)
            resp.body = json.dumps(doc, ensure_ascii=False)
            resp.status = falcon.HTTP_200
            print(item)
            # print(item.key, item.id, item.value)
        # Create a JSON representation of the resource
        # resp.body = json.dumps(doc, ensure_ascii=False)
        # resp.status = falcon.HTTP_200
        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
    # def on_get(self, req, resp):
    #     doc = {
    #         'name': fake.name(),
    #         'address':fake.address()
    #     }
    #     resp.status = falcon.HTTP_200
    #     resp.body = (doc)



class getData(object):
    def on_post(self, req, resp):


        # print 'try'
 
        test_users = {}
        print("Checking...")
        # insert_data = json.dumps(req.media, indent = 2)

        insert_data = req.media
        print(insert_data['comment'])
        doc=[]
        for item in dbSearch.view('jobspecdoc/jobspecview'):
            doc.append(item.value['job_title'])
 
   
  
        # print(json.dumps(req.media))
   
        
        # print(insert_data['value']['name'])
        # print(insert_data['value']['email'])
        # print(insert_data['value']['address'])
        # print(insert_data['value']['remarks'])
        # print(insert_data['id'])
    
        # print(insert_data)

 

        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
        # doc={}
        # doc = resp.media
        # resp.body = json.dumps(doc, ensure_ascii=False)
        # print(doc)
        # db.save(json.dumps(doc, ensure_ascii=False))
        # print(json.dumps(doc, ensure_ascii=False))
        # print(req)        
        # return ""

app = falcon.API()

# Resources are represented by long-lived class instances
things = Resource()
catchData = getData()




# things will handle all requests to the '/things' URL path
app.add_route('/catchData', catchData)


# things will handle all requests to the '/things' URL path
app.add_route('/things', things)
