# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:25:10 2023

@author: charl
"""

import numpy as np
import pylab



x1 = np.linspace(0, 10, 20)
y1 = np.sin(x1)

x2 = np.linspace(0, 10, 1000)
y2 = np.sin(x2)


pylab.plot(x1, y1, 'bo', label='sampled')
pylab.plot(x2, y2, ':k', label='continuous')
pylab.legend()

pylab.ylim(-1.5, 2.0)

