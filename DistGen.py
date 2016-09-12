# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:25:05 2016

@author: Ai
"""

import numpy as np
import math
import matplotlib.pylab as plb

x = 2 * math.pi * np.random.random_sample((10000,)) - math.pi

y1 = np.sin(x)
y2 = np.cos(x)

plb.hist(x/math.pi,bins=100,normed=1)
plb.xlabel("x/pi")
plb.ylabel("p(x)")
plb.show()

plb.plot(x/math.pi, y1,'b*')
plb.xlabel("x/pi")
plb.ylabel("y1")
plb.show()
plb.hist(y1,bins=100,normed=1)
plb.xlabel("y1")
plb.ylabel("p(y1)")
plb.show()

plb.plot(x/math.pi, y2, 'b*')
plb.xlabel("x/pi")
plb.ylabel("y2")
plb.show()
plb.hist(y2,bins=100,normed=1)
plb.xlabel("y2")
plb.ylabel("p(y2)")
plb.show()