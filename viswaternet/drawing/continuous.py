# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
from viswaternet.network import processing
from viswaternet.utils import save_fig, normalize_parameter, unit_conversion, fancyarrowpatch_to_linecollection, label_generator
from viswaternet.drawing import base
from viswaternet.utils.markers import *

default_cmap = 'autumn_r'


def plot_continuous_nodes(
    self,
    ax=None,
    parameter=None,
    element_list=None,
    value=None,
    unit=None,
    vmin=None,
    vmax=None,
    include_tanks=False,
    include_reservoirs=False,
    draw_tanks=True,
    draw_reservoirs=True,
    draw_pumps=True,
    draw_valves=True,
    cmap=default_cmap,
    color_bar_title=None,
    node_size=100,
    node_shape=".",
    edge_colors=None,
    line_widths=None,
    legend=True,
    base_legend_loc="upper right",
    savefig=False,
    save_name=None,
    dpi='figure',
    save_format='png',
    base_legend_label_font_size=15,
    base_legend_label_font_color="k",
    discrete_legend_label_font_size=15,
    discrete_legend_label_font_color="k",
    discrete_legend_title_font_size=17,
    discrete_legend_title_font_color='k',
    draw_legend_frame=False,
    node_sizes=None,
    link_sizes=None,
    element_size_intervals=None,
    element_size_legend_title=None,
    element_size_legend_loc=None,
    element_size_legend_labels=None,
    draw_base_legend=True,
    reservoir_size=150,
    reservoir_color='b',
    reservoir_shape='s',
    reservoir_border_color='k',
    reservoir_border_width=3,
    tank_size=200,
    tank_color='b',
    tank_shape='h',
    tank_border_color='k',
    tank_border_width=2,
    valve_element='node',
    valve_size=200,
    valve_color='orange',
    valve_shape=epa_valve,
    valve_border_color='k',
    valve_border_width=1,
    valve_width=3,
    valve_line_style='-',
    valve_arrows=False,
    pump_element='link',
    pump_size=200,
    pump_color='b',
    pump_shape=epa_pump,
    pump_border_color='k',
    pump_border_width=1,
    pump_width=3,
    pump_line_style='-',
    pump_arrows=False,
    base_node_color='k',
    base_node_size=30,
    base_link_color='k',
    base_link_width=1,
    base_link_line_style='-',
    base_link_arrows=False,
    draw_color_bar=True,
    color_bar_width=0.03,
    color_bar_height=0.8
):
    if len(self.model['G_list_pumps_only']) == 0:
        draw_pumps = False
    if ax is None:
        fig, ax = plt.subplots(figsize=self.figsize)
        self.fig = fig
        self.ax = ax
        ax.set_frame_on(self.axis_frame)
    if parameter is not None:
        parameter_results, node_list = processing.get_parameter(
            self,
            "node",
            parameter,
            value=value,
            element_list=element_list,
            include_tanks=include_tanks,
            include_reserovirs=include_reservoirs)
        if unit is not None:
            parameter_results = unit_conversion(
                parameter_results, parameter, unit)
        g = base.draw_nodes(
            self,
            ax,
            node_list,
            parameter_results=parameter_results,
            vmin=vmin,
            vmax=vmax,
            node_size=node_size,
            cmap=cmap,
            node_shape=node_shape,
            edge_colors=edge_colors,
            line_widths=line_widths,
        )

        base.draw_base_elements(
            self,
            ax,
            draw_nodes=False,
            draw_reservoirs=draw_reservoirs,
            draw_tanks=draw_tanks,
            draw_valves=draw_valves,
            draw_pumps=draw_pumps,
            reservoir_size=reservoir_size,
            reservoir_color=reservoir_color,
            reservoir_shape=reservoir_shape,
            reservoir_border_color=reservoir_border_color,
            reservoir_border_width=reservoir_border_width,
            tank_size=tank_size,
            tank_color=tank_color,
            tank_shape=tank_shape,
            tank_border_color=tank_border_color,
            tank_border_width=tank_border_width,
            valve_element=valve_element,
            valve_size=valve_size,
            valve_color=valve_color,
            valve_shape=valve_shape,
            valve_border_color=valve_border_color,
            valve_border_width=valve_border_width,
            valve_width=valve_width,
            valve_line_style=valve_line_style,
            valve_arrows=valve_arrows,
            pump_element=pump_element,
            pump_size=pump_size,
            pump_color=pump_color,
            pump_shape=pump_shape,
            pump_border_color=pump_border_color,
            pump_border_width=pump_border_width,
            pump_width=pump_width,
            pump_line_style=pump_line_style,
            pump_arrows=pump_arrows,
            base_node_color=base_node_color,
            base_node_size=base_node_size,
            base_link_color=base_link_color,
            base_link_width=base_link_width,
            base_link_line_style=base_link_line_style,
            base_link_arrows=base_link_arrows
        )
        if draw_color_bar == True:
            if color_bar_title is None:
                color_bar_title = label_generator(parameter, value, unit)

            base.draw_color_bar(ax,
                                g,
                                cmap,
                                color_bar_title=color_bar_title,
                                color_bar_width=color_bar_width,
                                color_bar_height=color_bar_height)
    if legend:

        base.draw_legend(ax,
                         draw_pumps=draw_pumps,
                         base_legend_loc=base_legend_loc,
                         base_legend_label_font_size=base_legend_label_font_size, 
                         base_legend_label_font_color=base_legend_label_font_color,
                         discrete_legend_label_font_size=discrete_legend_label_font_size, 
                         discrete_legend_label_font_color=discrete_legend_label_font_color,
                         discrete_legend_title_font_size=discrete_legend_title_font_size,
                         discrete_legend_title_font_color=discrete_legend_title_font_color,
                         draw_legend_frame=draw_legend_frame,
                         pump_color=pump_color,
                         base_link_color=base_link_color,
                         node_sizes=node_sizes,
                         link_sizes=link_sizes,
                         element_size_intervals=element_size_intervals,
                         element_size_legend_title=element_size_legend_title,
                         element_size_legend_loc=element_size_legend_loc,
                         element_size_legend_labels=element_size_legend_labels,
                         draw_base_legend=draw_base_legend,
                         linewidths=line_widths,
                         edge_colors=edge_colors,
                         pump_line_style=pump_line_style,
                         base_link_line_style=base_link_line_style,
                         base_link_arrows=base_link_arrows,
                         pump_arrows=pump_arrows,
                         draw_base_links=True,
                         draw_valves=draw_valves,
                         valve_element=valve_element,
                         valve_line_style=valve_line_style,
                         valve_color=valve_color,
                         valve_arrows=valve_arrows,
                         pump_element=pump_element)
    if savefig:

        save_fig(self, save_name=save_name, dpi=dpi, save_format=save_format)


def plot_continuous_links(
    self,
    ax=None,
    parameter=None,
    element_list=None,
    value=None,
    unit=None,
    widths=1,
    min_width=1,
    max_width=1,
    vmin=None,
    vmax=None,
    link_style='-',
    link_arrows=False,
    draw_tanks=True,
    draw_reservoirs=True,
    draw_pumps=True,
    draw_valves=True,
    cmap=default_cmap,
    color_bar_title=None,
    legend=True,
    base_legend_loc="upper right",
    savefig=False,
    save_name=None,
    dpi='figure',
    save_format='png',
    base_legend_label_font_size=15,
    base_legend_label_font_color="k",
    discrete_legend_label_font_size=15,
    discrete_legend_label_font_color="k",
    discrete_legend_title_font_size=17,
    discrete_legend_title_font_color='k',
    draw_legend_frame=False,
    node_sizes=None,
    link_sizes=None,
    element_size_intervals=None,
    element_size_legend_title=None,
    element_size_legend_loc=None,
    element_size_legend_labels=None,
    draw_base_legend=True,
    reservoir_size=150,
    reservoir_color='b',
    reservoir_shape='s',
    reservoir_border_color='k',
    reservoir_border_width=3,
    tank_size=200,
    tank_color='b',
    tank_shape='h',
    tank_border_color='k',
    tank_border_width=2,
    valve_element='node',
    valve_size=200,
    valve_color='orange',
    valve_shape=epa_valve,
    valve_border_color='k',
    valve_border_width=1,
    valve_width=3,
    valve_line_style='-',
    valve_arrows=False,
    pump_element='link',
    pump_size=200,
    pump_color='b',
    pump_shape=epa_pump,
    pump_border_color='k',
    pump_border_width=1,
    pump_width=3,
    pump_line_style='-',
    pump_arrows=False,
    base_node_color='k',
    base_node_size=30,
    base_link_color='k',
    base_link_width=1,
    base_link_line_style='-',
    base_link_arrows=False,
    draw_color_bar=True,
    color_bar_width=0.03,
    color_bar_height=0.8
):
    if len(self.model['G_list_pumps_only']) == 0:
        draw_pumps = False
    if ax is None:
        if ax is None:
            fig, ax = plt.subplots(figsize=self.figsize)
            ax.set_frame_on(self.axis_frame)
    if parameter is not None:

        parameter_results, link_list = processing.get_parameter(
            self, "link", parameter, value=value, element_list=element_list
        )

        if unit is not None:
            parameter_results = unit_conversion(
                parameter_results, parameter, unit)
        normalized_parameter = normalize_parameter(
            parameter_results, min_width, max_width
        )

        widths = normalized_parameter

        g = base.draw_links(
            self,
            ax,
            link_list,
            parameter_results=parameter_results,
            cmap=cmap,
            widths=widths,
            vmin=vmin,
            vmax=vmax,
            link_style=link_style,
            link_arrows=link_arrows,
        )

        base.draw_base_elements(
            self,
            ax,
            draw_nodes=False,
            draw_links=False,
            draw_reservoirs=draw_reservoirs,
            draw_tanks=draw_tanks,
            draw_valves=draw_valves,
            draw_pumps=draw_pumps,
            reservoir_size=reservoir_size,
            reservoir_color=reservoir_color,
            reservoir_shape=reservoir_shape,
            reservoir_border_color=reservoir_border_color,
            reservoir_border_width=reservoir_border_width,
            tank_size=tank_size,
            tank_color=tank_color,
            tank_shape=tank_shape,
            tank_border_color=tank_border_color,
            tank_border_width=tank_border_width,
            valve_element=valve_element,
            valve_size=valve_size,
            valve_color=valve_color,
            valve_shape=valve_shape,
            valve_border_color=valve_border_color,
            valve_border_width=valve_border_width,
            valve_width=valve_width,
            valve_line_style=valve_line_style,
            valve_arrows=valve_arrows,
            pump_element=pump_element,
            pump_size=pump_size,
            pump_color=pump_color,
            pump_shape=pump_shape,
            pump_border_color=pump_border_color,
            pump_border_width=pump_border_width,
            pump_width=pump_width,
            pump_line_style=pump_line_style,
            pump_arrows=pump_arrows,
            base_node_color=base_node_color,
            base_node_size=base_node_size,
            base_link_color=base_link_color,
            base_link_width=base_link_width,
            base_link_line_style=base_link_line_style,
            base_link_arrows=base_link_arrows
        )
        if link_arrows == True:
            g = fancyarrowpatch_to_linecollection(
                g, cmap, vmin, vmax, parameter_results)

        if draw_color_bar == True:
            if color_bar_title is None:
                color_bar_title = label_generator(parameter, value, unit)

            base.draw_color_bar(ax,
                                g,
                                cmap,
                                color_bar_title=color_bar_title,
                                color_bar_width=color_bar_width,
                                color_bar_height=color_bar_height)

    if legend:

        base.draw_legend(ax,
                         draw_pumps=draw_pumps,
                         base_legend_loc=base_legend_loc,
                         base_legend_label_font_size=base_legend_label_font_size, 
                         base_legend_label_font_color=base_legend_label_font_color,
                         discrete_legend_label_font_size=discrete_legend_label_font_size, 
                         discrete_legend_label_font_color=discrete_legend_label_font_color,
                         discrete_legend_title_font_size=discrete_legend_title_font_size,
                         discrete_legend_title_font_color=discrete_legend_title_font_color,
                         draw_legend_frame=draw_legend_frame,
                         pump_color=pump_color,
                         base_link_color=base_link_color,
                         node_sizes=node_sizes,
                         link_sizes=link_sizes,
                         element_size_intervals=element_size_intervals,
                         element_size_legend_title=element_size_legend_title,
                         element_size_legend_loc=element_size_legend_loc,
                         element_size_legend_labels=element_size_legend_labels,
                         draw_base_legend=draw_base_legend,
                         pump_line_style=pump_line_style,
                         base_link_line_style=base_link_line_style,
                         base_link_arrows=base_link_arrows,
                         pump_arrows=pump_arrows,
                         draw_base_links=False,
                         draw_valves=draw_valves,
                         valve_element=valve_element,
                         valve_line_style=valve_line_style,
                         valve_color=valve_color,
                         valve_arrows=valve_arrows,
                         pump_element=pump_element)
    if savefig:

        save_fig(self, save_name=save_name, dpi=dpi, save_format=save_format)
