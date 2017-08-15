#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import time


def test_streaming_bulk():
    actions = []
    for i in xrange(0, 100000):
        actions.append({'_index': 'test_index', '_type': 'test', 'x': i})

    t1 = time.time()
    print helpers.bulk(es, actions, False)
    t2 = time.time()
    print('used time: {}'.format(t2-t1))


def test_parallel_bulk():
    actions = []
    for i in xrange(0, 100000):
        actions.append({'_index': 'test_index', '_type': 'test', 'x': i})

    t1 = time.time()
    print parallel_bulk(es, actions)
    t2 = time.time()
    print('used time: {}'.format(t2-t1))


def parallel_bulk(client, actions, stats_only=False, **kwargs):

    success, failed = 0, 0

    # list of errors to be collected is not stats_only
    errors = []

    for ok, item in helpers.parallel_bulk(client, actions, **kwargs):
        # print ok, item
        # go through request-reponse pairs and detect failures
        if not ok:
            if not stats_only:
                errors.append(item)
            failed += 1
        else:
            success += 1

    return success, failed if stats_only else errors


if __name__ == '__main__':
    test_streaming_bulk()
    test_parallel_bulk()
    pass