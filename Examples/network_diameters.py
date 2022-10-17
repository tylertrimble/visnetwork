# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 17:18:55 2022

@author: Tyler
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:36:38 2022

@author: Tyler
"""
import visnet.network as visinit
import visnet.drawing as visplot
import matplotlib.pyplot as plt
import os

model = visinit.initialize_model(r'Networks\Net3.inp')

cwd = os.getcwd()
model['image_path'] = cwd + '\Images'

fig, ax = plt.subplots(figsize=(10,15))
plt.title("Pipe Diameters for CTown Network",fontsize=16)

ax.set_frame_on(False);

visplot.plot_unique_data(model, 
                         ax, 
                         parameter='diameter',
                         unit='in',
                         cmap='Blues',
                         legend_loc_2='lower left',
                         legend_title='Pipe Diameter (in)',
                         font_color='k',
                         legend_sig_figs=3,
                         pump_color='mediumseagreen',
                         pump_width=5,
                         tank_shape='h',
                         tank_color='b',
                         tank_border_color='k',
                         tank_border_width=2,
                         reservoir_color='b',
                         reservoir_size=150,
                         reservoir_border_color='k',
                         reservoir_border_width=3)
plt.show()