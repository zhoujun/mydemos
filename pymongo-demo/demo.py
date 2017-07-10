# -*- coding: utf-8 -*-

from pymongo import MongoClient
import datetime
import pprint

client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')

db = client.test_database
# db = client['test-database']

def insert():
    post = {"author":"Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}

    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    print post_id

def insert_news():
    new_posts = [{"author": "Mike",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]

    posts = db.posts
    result = posts.insert_many(new_posts)
    print result.inserted_ids


from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
    return document

def find_one():
    posts = db.posts
    pprint.pprint(posts.find_one())

    pprint.pprint(posts.find_one({"author": "Mike"}))

    post = posts.find_one()
    print post
    post_id = post.get('_id')
    print post_id

    pprint.pprint(posts.find_one({"_id": post_id}))

    pprint.pprint(get(post_id))

def find():
    posts = db.posts
    for post in posts.find():
        pprint.pprint(post)

    # counting
    print posts.count()


def range_query():
    posts = db.posts
    d = datetime.datetime(2009, 11, 12, 12)
    for post in posts.find({"date": {"$lt": d}}).sort("author"):
        pprint.pprint(post)

def create_index():
    import pymongo
    result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
                                   unique=True)
    print sorted(list(db.profiles.index_information()))

if __name__ == '__main__':
    # find_one()
    # insert_news()
    # find()
    # range_query()
    create_index()

