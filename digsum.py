#!/usr/bin/env python

import math
import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('nahay', 'nw9ie3vouh')

def digitalSum(n):
    """Defined recursively, returns digital sum of any integer"""
    if n < 10:
       return n
    return n % 10 + digitalSum( n // 10)

squares = [x**2 for x in range(1000)]
digsums = [digitalSum(n) for n in squares]

trace = go.Scatter(
    x = squares,
    y = digsums,
    mode = 'markers'
)

data = [trace]

# Plot in html file
#plot_url = py.plot(data, filename='perfect-squares1')
py.iplot(data, filename='basic-scatter2')
