#!/usr/bin/env python
# *_* encoding=utf-8 *_*

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, A
from elasticsearch_dsl.query import MultiMatch, Match, Q

from datetime import datetime
from example_1 import Article


client = Elasticsearch()
s = Search(using=client)


def add_article(id_, title, body, tags):
    article = Article(meta={'id': id_}, title=title, tags=tags)
    article.body = body
    article.published_from = datetime.now()
    article.save()


def init_test_data():
    add_article(2, 'Python is good!', 'Python is good!', ['python'])
    add_article(3, 'Elasticsearch is good!', 'Distributed, open source search and analytics engine', ['elasticsearch'])
    add_article(4, 'Python very quickly', 'Python very quickly', ['python'])
    add_article(5, 'Django', 'Python Web framework', ['python', 'django'])


def test_simple_search():
    s = Search().query("match", title="python")
    # {'query': {'match': {'title': 'python'}}}
    print(s.to_dict())
    response = s.execute()
    print response
    for hit in s:
        print(hit.title)


def test_queries():
    # 创建一个多字段查询
    multi_match = MultiMatch(query='python', fields=['title', 'body'])
    s = Search().query(multi_match)
    print(s.to_dict())
    # {'query': {'multi_match': {'fields': ['title', 'body'], 'query': 'python'}}}

    q = Q("multi_match", query='python', fields=['title', 'body'])
    s = Search().query(q)
    print(s.to_dict())

    q = Q({"multi_match": {"query": "python", "fields": ["title", "body"]}})
    s = Search().query(q)
    print(s.to_dict())

    # If you already have a query object, or a dict
    # representing one, you can just override the query used
    # in the Search object:
    s.query = Q('bool', must=[Q('match', title='python'), Q('match', body='best')])
    print(s.to_dict())


def test_query_combination():
    q = Q("match", title='python') | Q("match", title='django')
    s = Search().query(q)
    print(s.to_dict())

    q = Q("match", title='python') & Q("match", title='django')
    s = Search().query(q)
    print(s.to_dict())

    q = ~Q("match", title="python")
    s = Search().query(q)
    print(s.to_dict())


def test_filters():
    s = Search()
    s = s.filter('terms', tags=['search', 'python'])
    print(s.to_dict())
    # {'query': {'bool': {'filter': [{'terms': {'tags': ['search', 'python']}}]}}}

    s = s.query('bool', filter=[Q('terms', tags=['search', 'python'])])
    print(s.to_dict())
    # {'query': {'bool': {'filter': [{'terms': {'tags': ['search', 'python']}}]}}}

    s = s.exclude('terms', tags=['search', 'python'])
    # 或者
    # s = s.query('bool', filter=[~Q('terms', tags=['search', 'python'])])
    print(s.to_dict())
    # {'query': {'bool': {'filter': [{'bool': {'must_not': [{'terms': {'tags': ['search', 'python']}}]}}]}}}


def test_aggregations():
    s = Search()
    a = A('terms', filed='title')
    s.aggs.bucket('title_terms', a)
    print(s.to_dict())
    # {
    # 'query': {
    #   'match_all': {}
    #  },
    #  'aggs': {
    #       'title_terms': {
    #            'terms': {'filed': 'title'}
    #        }
    #    }
    # }

    # 或者
    s = Search()
    s.aggs.bucket('articles_per_day', 'date_histogram', field='publish_date', interval='day') \
        .metric('clicks_per_day', 'sum', field='clicks') \
        .pipeline('moving_click_average', 'moving_avg', buckets_path='clicks_per_day') \
        .bucket('tags_per_day', 'terms', field='tags')

    s.to_dict()
    # {
    #   "aggs": {
    #     "articles_per_day": {
    #       "date_histogram": { "interval": "day", "field": "publish_date" },
    #       "aggs": {
    #         "clicks_per_day": { "sum": { "field": "clicks" } },
    #         "moving_click_average": { "moving_avg": { "buckets_path": "clicks_per_day" } },
    #         "tags_per_day": { "terms": { "field": "tags" } }
    #       }
    #     }
    #   }
    # }


def test_sorting():
    s = Search().sort(
        'category',
        '-title',
        {"lines": {"order": "asc", "mode": "avg"}}
    )
    print(s.to_dict())


def test_prefix():
    s = Search()
    q = Q('prefix', title='dj')
    s = s.query(q)
    print(s.to_dict())
    response = s.execute()
    print response
    for hit in s:
        print(hit.title)

if __name__ == '__main__':
    # init_test_data()
    # test_simple_search()
    # test_queries()
    # test_query_combination()
    # test_filters()
    # test_aggregations()
    # test_sorting()
