import visnet.network as visinit
import visnet.drawing as visplot
import matplotlib.pyplot as plt

# Run EPANET2.0 Simulation and store results
model = visinit.initialize_model(r"Networks/CTown.inp")

# Define figure to be drawn to
fig, ax = plt.subplots(figsize=(12, 12))

# Disables frame around figure
ax.set_frame_on(False)

#Get mean pressure at each node
mean, element_list = visinit.get_parameter(
    model, "node", parameter="pressure", value="mean"
)
#Get standard deviation at  each node
standard_deviation, element_list = visinit.get_parameter(
    model, "node", parameter="pressure", value="stddev"
    )
#Bin standard deviation values
binnedParameter, interval_names = visinit.bin_parameter(
    model, standard_deviation, element_list, 5
)
#Set bin_sizes and create node_sizes array
interval_sizes = [100, 200, 300, 400]
node_sizes = [None]*len(element_list)
#Set node_sizes according to bin_sizes
for interval_name, size in zip(interval_names, interval_sizes):
    for element in binnedParameter[interval_name]:
        node_sizes[element_list.index(element)]=size
#Plot continuous mean data and pass custom node_sizes
visplot.plot_unique_data(
    model,ax,parameter="custom_data",
    parameter_type="node",data_type="continuous",
    custom_data_values=[element_list,mean],
    color_bar_title="Mean Pressure (m)",cmap="gist_heat_r",
    node_size=node_sizes,
    element_size_bins=4,
    element_size_legend_title="Standard Deviation (m)",
    element_size_legend_loc="lower left",
    element_size_legend_labels=interval_names,
)
plt.show()