#!/usr/bin/python
'''
# -*- coding=utf-8 -*-

from matplotlib import font_manager
import matplotlib.pyplot as plt;
'''

import numpy as np
import pylab as pl
import csv

if __name__ == '__main__':
	'''
    thread_num = [1, 3, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    throughput1 = [574.8695765, 878.0209408, 890.9727752, 892.219843, 890.1647918, 886.6329007, 884.769794, 882.6222708,
                   880.9602467, 877.2218384, 875.8964252, 875.2639468, 874.2978296]
    throughput2 = [18.22837677, 52.29950462, 88.11752763, 161.328, 235.0830, 233.0830, 231.0830, 229.0830, 227.0830,
                   225.0830, 223.0830, 221.0830, 219.0830062]
    #zh_font = font_manager.FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=14)

    # Plot the figure.
    line,  = plt.plot(thread_num, throughput1, color='cornflowerblue', linestyle='-', linewidth=3, marker='o', markersize=8,
             label='Big Class')
    plt.plot(thread_num, throughput2, color='darkred', linestyle='-', marker='s', markersize=8, linewidth=3,
             label='Small Class')
    plt.ylim(ymin=0)

    plt.ylabel('avarage input and output(Mbit/s)')
    plt.legend(loc=(0.78, 0.8))
    plt.xlabel('number of thread')
    plt.savefig('TestConcurrentPut10Mand10K.png')

    plt.show()
 	'''
	#x = [1, 2, 3, 4, 5]# Make an array of x values
	#y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
	x=[]
	y=[]
	with open('dbscan.csv','r') as csvfile:
		plots = csv.reader(csvfile, delimiter = ',')
		print plots

	'''
		for row in plots:
			x.append(row[1])
			y.append(row[2])
	'''
	#pl.plot(x, y, 'o')# use pylab to plot x and y
	#pl.show()# show the plot on the screen
