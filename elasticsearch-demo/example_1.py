#!/usr/bin/env python
# *_* encoding=utf-8 *_*

from datetime import datetime
from elasticsearch_dsl import DocType, Date, Integer, Keyword, Text
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])


class Article(DocType):
    title = Text(analyzer='snowball', fields={'raw': Keyword()})
    body = Text(analyzer='snowball')
    tags = Keyword()
    published_from = Date()
    lines = Integer()

    class Meta:
        index = 'blog'

    def save(self, ** kwargs):
        self.lines = len(self.body.split())
        return super(Article, self).save(** kwargs)

    def is_published(self):
        return datetime.now() >= self.published_from

# create the mappings in elasticsearch
Article.init()


def create_article():

    # create and save and article
    article = Article(meta={'id': 1}, title='Hello elasticsearch!', tags=['elasticsearch'])
    article.body = ''' looong text '''
    article.published_from = datetime.now()
    article.save()


def get_article():
    article = Article.get(id=1)
    print(article.to_dict())


def update_article():
    article = Article.get(id=1)
    article.body = 'this is test body.'
    article.tags = ['elasticsearch', 'hello']
    article.save()

    # you can also update just individual fields which will call the update API
    # and also update the document in place
    article.update(body='Today is good day!', published_by='me')


def delete_article():
    article = Article.get(id=1)
    article.delete()


if __name__ == '__main__':
    # create_article()
    # get_article()
    # update_article()
    # delete_article()
    pass