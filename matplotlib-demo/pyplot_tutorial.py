#-*- coding: utf-8 -*-


"""
Example:
http://matplotlib.org/2.0.2/examples/index.html
https://zhuanlan.zhihu.com/p/24309547
"""

import matplotlib.pyplot as plt
import numpy as np

def test6():
    """
    ====================
    Horizontal bar chart
    ====================

    This example showcases a simple horizontal bar chart.
    """
    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.barh(y_pos, performance, xerr=error, align='center',
            color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')

    plt.show()

def test5():
    '''
    Plot lines with points masked out.

    This would typically be used with gappy data, to
    break the line at the data gaps.
    '''
    x = np.arange(0, 2*np.pi, 0.02)
    y = np.sin(x)
    y1 = np.sin(2*x)
    y2 = np.sin(3*x)
    ym1 = np.ma.masked_where(y1 > 0.5, y1)
    ym2 = np.ma.masked_where(y2 < -0.5, y2)

    lines = plt.plot(x, y, x, ym1, x, ym2, 'o')
    plt.setp(lines[0], linewidth=4)
    plt.setp(lines[1], linewidth=2)
    plt.setp(lines[2], markersize=10)

    plt.legend(('No mask', 'Masked if > 0.5', 'Masked if < -0.5'),
               loc='upper right')
    plt.title('Masked line demo')
    plt.show()

def test4():
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2*np.pi*t)
    plt.plot(t, s)

    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    # plt.savefig("test.png")   // save image
    plt.show()

def test3():
    plt.xlabel(u'Sex')
    plt.ylabel(u'People')

    plt.title(u"Sex ratio analysis")
    plt.xticks((0,1), (u'man',u'woman'))
    rect = plt.bar(left = (0,1), height = (1,0.5), width = 0.35, align="center")

    plt.legend((rect,),(u"legend",))

    plt.show()

def test2():

    """
    ========
    Barchart
    ========

    A bar plot with errorbars and height labels on individual bars
    """

    N = 5
    menMeans = (20, 35, 30, 35, 27)
    menStd =   (2, 3, 4, 1, 2)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

    womenMeans = (25, 32, 34, 20, 25)
    womenStd =   (3, 5, 2, 3, 3)
    rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)

    # add some
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )

    ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    plt.show()


def test1():

    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()


if __name__ == '__main__':

    testId = 5
    eval("test%s()" % testId )
