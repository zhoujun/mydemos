# -*- coding: utf-8 -*-

import random
from time import sleep
from greenlet import greenlet
from Queue import Queue

queue = Queue(1)

@greenlet
def producer():
    chars = ['a', 'b', 'c', 'd', 'e']
    global queue
    while True:
        char = random.choice(chars)
        queue.put(char)
        print "Produced: ", char
        sleep(1)
        consumer.switch()

@greenlet
def consumer():
    global queue
    while True:
        char = queue.get()
        print "Consumed: ", char
        sleep(1)
        producer.switch()

if __name__ == "__main__":
    producer.run()
    consumer.run()
