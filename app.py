import base64
from io import BytesIO

from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt

import waveforms as wf
import simulation as sim

app = Flask(__name__)

@app.route('/')
def index():
    
    shape = wf.CV(Eini = 0, Eupp = 0.5, Elow = 0, dE = 0.001, sr = 0.1, ns = 1)
    instance = sim.E(input = shape, E0 = 0.25, k0 = 10, a = 0.5, cR = 0.005, cO = 0.000, DR = 5E-6, DO = 5E-6, r = 0.15, expansion = 1.05, Nernstian = False, BV = True, MH = False)
    
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12, 5))
    
    left, = ax1.plot(shape.tWF, shape.EWF, linewidth = 1, linestyle = '-', color = 'blue', marker = None, label = None, visible = True)
    right, = ax2.plot(instance.E, instance.flux, linewidth = 1, linestyle = '-', color = 'red', marker = None, label = None, visible = True)

    '''PLOT SETTINGS'''
    ax1.set_xlim(np.amin(shape.tWF) - (0.1 * (np.amax(shape.tWF) - np.amin(shape.tWF))), np.amax(shape.tWF) + (0.1 * (np.amax(shape.tWF) - np.amin(shape.tWF))))
    ax1.set_ylim(np.amin(shape.EWF) - (0.1 * (np.amax(shape.EWF) - np.amin(shape.EWF))), np.amax(shape.EWF) + (0.1 * (np.amax(shape.EWF) - np.amin(shape.EWF))))
    ax1.set_title('E vs. t', pad = 15, fontsize = 20)
    ax1.set_xlabel('t / s', labelpad = 5, fontsize = 15)
    ax1.set_ylabel('E / V', labelpad = 5, fontsize = 15)

    ax2.set_xlim(np.amin(instance.EPLOT) - (0.1 * (np.amax(instance.EPLOT) - np.amin(instance.EPLOT))), np.amax(instance.EPLOT) + (0.1 * (np.amax(instance.EPLOT) - np.amin(instance.EPLOT))))
    ax2.set_ylim(np.amin(instance.flux) - (0.1 * (np.amax(instance.flux) - np.amin(instance.flux))), np.amax(instance.flux) + (0.1 * (np.amax(instance.flux) - np.amin(instance.flux)))) 
    ax2.set_title('i vs. E', pad = 15, fontsize = 20)
    ax2.set_xlabel('E / V', labelpad = 5, fontsize = 15)
    ax2.set_ylabel('i / A', labelpad = 5, fontsize = 15)
    
         
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

if __name__ == '__main__':
    app.run(debug = True)