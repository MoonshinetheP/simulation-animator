
import io
from flask import Response


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

def plot(filename):
    data = np.loadtxt(f'static/data/{filename}', delimiter = ',')
    
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12, 5))
    left, = ax1.plot(data[:,0], data[:,1], linewidth = 1, linestyle = '-', color = 'blue', marker = None, label = None, visible = True)
    right, = ax2.plot(data[:,1], data[:,2], linewidth = 1, linestyle = '-', color = 'red', marker = None, label = None, visible = True)
    
    output = io.BytesIO()
 
    fig.savefig(output, format="png")
    
    # Return the GIF image as a Flask response
    return Response(output.getvalue(), mimetype='image/gif')


def animate(data_filename):
    '''PLOT GENERATION'''
    data = np.loadtxt(f'static/data/{data_filename}', delimiter = ',')
    
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12, 5))
    left, = ax1.plot([], [], linewidth = 1, linestyle = '-', color = 'blue', marker = None, label = None, visible = True)
    right, = ax2.plot([], [], linewidth = 1, linestyle = '-', color = 'red', marker = None, label = None, visible = True)


    '''PLOT SETTINGS
    ax1.set_xlim(np.amin(shape.tWF) - (0.1 * (np.amax(shape.tWF) - np.amin(shape.tWF))), np.amax(shape.tWF) + (0.1 * (np.amax(shape.tWF) - np.amin(shape.tWF))))
    ax1.set_ylim(np.amin(shape.EWF) - (0.1 * (np.amax(shape.EWF) - np.amin(shape.EWF))), np.amax(shape.EWF) + (0.1 * (np.amax(shape.EWF) - np.amin(shape.EWF))))
    ax1.set_title('E vs. t', pad = 15, fontsize = 20)
    ax1.set_xlabel('t / s', labelpad = 5, fontsize = 15)
    ax1.set_ylabel('E / V', labelpad = 5, fontsize = 15)

    ax2.set_xlim(np.amin(instance.EPLOT) - (0.1 * (np.amax(instance.EPLOT) - np.amin(instance.EPLOT))), np.amax(instance.EPLOT) + (0.1 * (np.amax(instance.EPLOT) - np.amin(instance.EPLOT))))
    ax2.set_ylim(np.amin(instance.flux) - (0.1 * (np.amax(instance.flux) - np.amin(instance.flux))), np.amax(instance.flux) + (0.1 * (np.amax(instance.flux) - np.amin(instance.flux)))) 
    ax2.set_title('i vs. E', pad = 15, fontsize = 20)
    ax2.set_xlabel('E / V', labelpad = 5, fontsize = 15)
    ax2.set_ylabel('i / A', labelpad = 5, fontsize = 15)'''

    
    '''ANIMATION FUNCTIONS'''
    def potential(i):
        left.set_data(data[0, :i], data[1, :i])
        return left, 

    def current(i):
        right.set_data(data[1, :i], data[2, :i])
        return right,


    '''ANIMATION'''
    Evt = animation.FuncAnimation(fig, potential, frames = data[0].size, interval = 1, repeat = False, blit = True) 
    ivE = animation.FuncAnimation(fig, current, frames = data[0].size, interval = 1, repeat = False, blit = True)
    
    

    output = io.BytesIO()
 
    fig.savefig(output, format="png")
    
    # Return the GIF image as a Flask response
    return Response(output.getvalue(), mimetype='image/gif')

if __name__ == '__main__':
    plot('CV 0.5.txt')