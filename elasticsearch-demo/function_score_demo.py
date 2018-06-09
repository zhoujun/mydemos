#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticsearch_dsl import (
    DocType, Date, Integer, Text, Float, Boolean, Keyword, SF, Q, A, String,
    Completion, GeoPoint)
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import query
from datetime import datetime
import random


connections.create_connection(hosts=['localhost'])


class House(DocType):

    city = String()
    zip_code = String()
    address = String()
    price = Float()
    location = GeoPoint()
    created_at = Date()
    likes = Integer()

    class Meta:
        index = 'my_index'
        type = 'house'

    def save(self, ** kwargs):
        return super(House, self).save(** kwargs)

House.init()


def add_house(id_, city, address, price, location, created_at):
    house = House(meta={'id': id_})
    house.city = city
    house.address = address
    house.price = price
    house.location = location
    house.created_at = created_at
    house.likes = random.randint(0, 100)
    house.save()


class Post(DocType):
    title = String()
    content = Text()
    votes = Integer()
    created_at = Date()

    class Meta:
        index = 'blogposts'
        type = 'post'

Post.init()


def add_post(id_, title, content):
    post = Post(meta={'id': id_})
    post.title = title
    post.content = content
    post.votes = random.randint(0, 100)
    post.save()


def init_data():
    add_house(1, 'Fort Myers', '12560 Kelly Palm Dr', 339900, (26.494627, -81.961609), '2015-03-01 11:58:04')
    add_house(2, 'San Antonio', '1889 Mclain Rd', 2350000, (28.226024, -82.448905), '2015-03-03 08:04:08')
    add_house(3, 'Sarasota', '1534  Ernesto Dr', 425000, (26.494627, -81.961609), '2015-03-03 08:04:09')
    add_house(4, 'Land O Lakes', '1016 Cherbury Ln', 3490000, (26.515454, -81.903935), '2015-03-04 11:08:09')
    add_house(5, 'Stoneville', '7000 Nw 104 Ct', 169000, (27.944799, -82.816724), '2015-03-04 14:43:22')
    add_house(6, 'Kissimmee', '11255  Macaw Ct', 224900, (27.226971, -82.518084), '2017-06-28 23:16:10')
    add_house(7, 'Malibu', '4558 Ada Ln', 109900, (25.704764, -80.332775), '2017-07-02 17:16:03')
    add_house(8, 'Bradenton', '4900 BUNNIE Lane', 419990, (27.215368, -82.456293), '2017-08-11 12:28:57')
    add_house(9, 'Fort Lauderdale', '7911 Burgoyne', 555000, (28.473397, -81.567864), '2017-08-11 12:03:59')
    add_house(10, 'Nineveh', '9194  Bay Point Dr', 239100, (26.110462, -80.262753), '2017-08-11 12:37:32')

    add_post(1, 'Python is good', 'Python is good')
    add_post(2, 'Python is beautiful', 'Python is beautiful')
    add_post(3, 'Python is nice', 'Python is nice')
    add_post(4, 'Today is good day', 'Today is good day')
    add_post(5, 'Today is nice day', 'Today is nice day')
    add_post(6, 'The key aspect in promoting', 'The key aspect in promoting')
    add_post(7, 'Just a month after we started', 'Just a month after we started working on reddit')
    add_post(8, "If I can't hear your heartbeat", "If I can't hear your heartbeat, you're too far away.")
    add_post(9, 'No Country for Old Men', 'No Country for Old Men')
    add_post(10, 'Django is web framework', 'Django is python lib')


def test_raw_function_score():
    s = House.search()
    s = s.from_dict(
        {"query":
            {"function_score": {
                "gauss": {
                    'created_at': {
                        "origin": "2015-03-01",
                        "scale": "10d",
                        "offset": "5d",
                        "decay": 0.5
                    }
                }
            }}
        })
    print(s.to_dict())

"""
- 线性衰减(linear)
- 指数衰减(exp)
- 高斯衰减(gauss)

假定Scale = 10d, Decay = 0.5, score = 1. 则三个衰减共同处是10天内score都是衰减到0.5，不同之处如下所述:
线性衰减表现为20d内直接衰减为0，衰减速度一致;
高斯衰减表现为前10天衰减较缓，后10天衰减加快，25d后也会衰减为0;
指数衰减表现为前10d衰减很快，10d后衰减变缓，且永远不会衰减至0，只会无限接近与0;
"""


def test_function_score_exp():
    """
    origin: 中心点 或字段可能的最佳值, 落在原点 origin 上的文档评分 _score 为满分1.0 。
    scale:  衰减率, 即一个文档从原点origin下落时, 评分_score 改变的速度(例如，每 £10 欧元或每 100 米)。
    decay:  从原点 origin 衰减到 scale 所得的评分 _score, 默认值为 0.5。
    offset: 以原点 origin 为中心点，为其设置一个非零的偏移量 offset 覆盖一个范围，而不只是单个原点。
            在范围 -offset <= origin <= +offset 内的所有评分 _score 都是 1.0。
    :return:
    """
    q = query.Q(
        'function_score',
        functions=[
            query.SF('exp', created_at={'origin': '2015-03-01', 'scale': '10d', 'offset': '0d', 'decay': 0.5})
        ]
    )
    print(q.to_dict())
    s = House.search()
    s = s.query(q)
    response = s.execute()
    for h in response:
        print(h.city, h.created_at)


def test_function_score_gauss():
    q = query.Q(
        'function_score',
        query=query.Q('match', city='Sarasota'),
        functions=[
            query.SF('gauss', price={'origin': '0', 'scale': '20'}),
            query.SF('gauss', location={'origin': '26.494627, -81.961609', 'scale': '2km', 'offset': '0km',
                                        'decay': 0.33})
        ],
        score_mode="multiply"
    )
    s = House.search()
    s = s.query(q)
    print(s.to_dict())
    response = s.execute()
    for h in response:
        print(h.city, h.location)


def test_field_value_factor():
    q = query.Q(
        'function_score',
        query=query.Q("multi_match", query='python', fields=['title', 'content']),
        functions=[
            query.SF('field_value_factor', field='votes', modifier='log1p', factor=0.1)
        ],
        score_mode="sum",
        max_boost=1.5
    )
    s = Post.search()
    s = s.query(q)
    print(s.to_dict())
    response = s.execute()
    for h in response:
        print(h.title)


def test_random_score():
    """
    random_score 函数，它的输出是一个介于0到1之间的数字，当给它提供相同的seed值时，它能够产生一致性随机的结果
    random_score 子句不包含任何的filter，因此它适用于所有文档。
                 当然，如果你索引了能匹配查询的新文档，无论你是否使用了一致性随机，结果的顺序都会有所改变。
    :return:
    """
    q = query.Q(
        'function_score',
        functions=[
            query.SF('random_score', seed=10),
            query.SF('field_value_factor', field='likes', modifier="log1p", factor=0.1)
        ],
        score_mode="sum",
        max_boost=1.5

        # 通过制定max_boost参数来限制函数的最大影响
        # 无论field_value_factor函数的结果是多少，它绝不会大于1.5。
        # max_boost只是对函数的结果有所限制，并不是最终的_score。
    )
    s = House.search()
    s = s.query(q)
    print(s.to_dict())
    response = s.execute()
    for h in response:
        print(h.city, h.location)


if __name__ == '__main__':
    # init_data()
    # test_raw_function_score()
    test_field_value_factor()
    pass



































