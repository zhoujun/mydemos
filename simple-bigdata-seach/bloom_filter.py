#!/usr/bin/env python
# *_* encoding=utf-8 *_*


class Bloomfilter(object):
    """
    A Bloom filter is a probabilistic data-structure that trades space for accuracy
    when determining if a value is in a set.  It can tell you if a value was possibly
    added, or if it was definitely not added, but it can't tell you for certain that
    it was added.
    """
    def __init__(self, size):
        """Setup the BF with the appropriate size"""
        self.values = [False] * size
        self.size = size

    def hash_value(self, value):
        """Hash the value provided and scale it to fit the BF size"""
        return hash(value) % self.size

    def add_value(self, value):
        """Add a value to the BF"""
        h = self.hash_value(value)
        self.values[h] = True

    def might_contain(self, value):
        """Check if the value might be in the BF"""
        h = self.hash_value(value)
        return self.values[h]

    def print_contents(self):
        """Dump the contents of the BF for debugging purposes"""
        print(self.values)

if __name__ == '__main__':
    bf = Bloomfilter(10)
    bf.add_value('dog')
    bf.add_value('fish')
    bf.add_value('cat')
    bf.print_contents()
    bf.add_value('bird')
    bf.print_contents()
    # Note: contents are unchanged after adding bird - it collides
    for term in ['dog', 'fish', 'cat', 'bird', 'duck', 'emu']:
        print('{}: {} {}'.format(term, bf.hash_value(term), bf.might_contain(term)))
