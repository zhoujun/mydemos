#!/usr/bin/env python
# *_* encoding=utf-8 *_*

def major_segments(s):
    """
    Perform major segmenting on a string.  Split the string by all of the major
    breaks, and return the set of everything found.  The breaks in this implementation
    are single characters, but in Splunk proper they can be multiple characters.
    A set is used because ordering doesn't matter, and duplicates are bad.
    """
    major_breaks = ' '
    last = -1
    results = set()

    # enumerate() will give us (0, s[0]), (1, s[1]), ...
    for idx, ch in enumerate(s):
        if ch in major_breaks:
            segment = s[last+1:idx]
            results.add(segment)

            last = idx

    # The last character may not be a break so always capture
    # the last segment (which may end up being "", but yolo)
    segment = s[last+1:]
    results.add(segment)

    return results


def minor_segments(s):
    """
    Perform minor segmenting on a string.  This is like major
    segmenting, except it also captures from the start of the
    input to each break.
    """
    minor_breaks = '_.'
    last = -1
    results = set()

    for idx, ch in enumerate(s):
        if ch in minor_breaks:
            segment = s[last+1:idx]
            results.add(segment)

            segment = s[:idx]
            results.add(segment)

            last = idx

    segment = s[last+1:]
    results.add(segment)
    results.add(s)

    return results


def segments(event):
    """Simple wrapper around major_segments / minor_segments"""
    results = set()
    for major in major_segments(event):
        for minor in minor_segments(major):
            results.add(minor)
    return results


if __name__ == '__main__':
    for term in segments('src_ip = 1.2.3.4'):
        print(term)
