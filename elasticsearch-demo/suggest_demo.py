#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticsearch_dsl import DocType, Text, Keyword, Completion
from elasticsearch_dsl.connections import connections


connections.create_connection(hosts=['localhost'])


class BlogLive(DocType):
    subject = Text()
    description = Text()
    topics = Keyword()
    live_suggest = Completion()

    class Meta:
        index = 'blog'
        type = 'live'

    def save(self, ** kwargs):
        return super(BlogLive, self).save(** kwargs)


# create the mappings in elasticsearch
BlogLive.init()


def add_live(id_, subject, description):
    live = BlogLive(meta={'id': id_})
    live.subject = subject
    live.description = description
    live.live_suggest = subject
    live.save()


def init_data():
    add_live(1, 'python', 'python is good')
    add_live(2, 'python django', 'django is web framework')
    add_live(3, 'python flask', 'flask is web framework')
    add_live(4, 'elasticsearch', 'elasticsearch is searchengine')
    add_live(5, 'elasticsearch-dsl python', 'python elasticsearch dsl is client API')


def suggest(key):
    s = BlogLive.search()
    s = s.suggest('live_suggestion', key,
                  completion={'field': 'live_suggest', 'fuzzy': {'fuzziness': 2, 'prefix_length': 2}, 'size': 10})
    print(s.to_dict())
    """
    {'suggest': 
        {'live_suggestion': 
             {
                'completion': {'field': 'live_suggest', 'size': 10, 'fuzzy': {'fuzziness': 2, 'prefix_length': 2}}, 
                'text': 'python'
            }
        }
    }
    """
    suggestions = s.execute_suggest()
    # print(suggestions.live_suggestion)
    for match in suggestions.live_suggestion[0].options:
        source = match._source
        print(source['subject'],  source['description'], match._score)

if __name__ == '__main__':
    # init_data()

    suggest('python')
    pass
