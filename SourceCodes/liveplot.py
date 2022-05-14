import time

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

is_ipython = 'inline' in matplotlib.get_backend()

if is_ipython:
    from IPython import display

plt.ion()

class liveplot:

    def __init__(self, x, y1, y2):
        self.x = x
        self.y1 = y1
        self.y2 = y2


    def plot_duration(self, x, y):
        plt.figure(2,figsize= (20, 15), dpi = 72)
        #plt.clf()
        plt.subplot(211)
        plt.plot(x,abs(y[:, 0]), color='blue', marker = 'o')
        plt.xlabel('bias/V')
        plt.yscale('log')
        plt.ylabel('Capacitance/f')
        plt.grid()

        plt.subplot(212)
        plt.plot(x, y[:, 1],  color = 'red', marker = 'd')
        plt.xlabel('bias/V')
        plt.ylabel('Transconducatance')
        plt.grid()

        plt.pause(0.05) # pause to wait for update the line

        if is_ipython:
            display.clear_output(wait=True)
            display.display(plt.gcf())

    def collect(self):
        y = []
        x = []
        x.append(self.x)
        y.append(np.array([self.y1, self.y2]))
        for i in range(len(x)):
            self.plot_duration(x[i], np.array(y))


    def stop(self):
        time.sleep(20)
        plt.show()


