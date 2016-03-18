#from plotly import plotly  as py 
#from plotly import graph_objs as go 
#from plotly.graph_objs import Marker, Figure , XAxis, YAxis
#
#
#def createClusterPlots(low_cluster_x_papram, low_cluster_y_papram, hig_cluster_x_papram, high_cluster_y_papram):
#
#	# Create traces
#	low_trace = go.Scatter(
#	  x = low_cluster_x_papram,
#	  y = low_cluster_y_papram,
#	  mode = 'markers',
#	 name = 'Low', 
#	 marker=Marker(
#            color='grey',
#            symbol='square'
#        )
#	)
#
#	high_trace = go.Scatter(
#	x = hig_cluster_x_papram,
#	y = high_cluster_y_papram,
#	mode = 'markers',
#	name = 'High', 
#	marker=Marker(
#            color='black',
#            symbol='circle'
#        )
#	)
#	layout_to_use = go.Layout(
#    showlegend=True,
#    height=600,
#    width=600,
#    xaxis=XAxis(
#        autorange=False,
#        range=[15.0, 60.0],
#        showgrid=True,
#        showline=True,
#        zeroline=False
#    ),
#    yaxis=YAxis(
#        autorange=False,
#        range=[0.0, 60.0],
#        showgrid=True,
#        showline=True,
#        zeroline=False
#    )    
#  )
#
#	data_to_use = [low_trace, high_trace]
#	#print "Interesting stuff ... len-low:{} \n \n len-high:{}".format(low_cluster_y_papram, high_cluster_y_papram)
#	fig = Figure(data=data_to_use, layout=layout_to_use)
#	py.plot(fig)
#
#
