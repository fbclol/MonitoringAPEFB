#!/usr/bin/env python3
# coding: utf-8

import pygal

line_chart = pygal.Line()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Firefox', 8)
line_chart.render_to_file('c:/temp/chart.svg')