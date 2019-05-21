import networkx as nx
import random
import json

def construct_graph(nodes_set, edges):
	nodes = list(nodes_set)
	graph = nx.Graph()
	# add nodes from a list of nodes
	# [1,2,3,...]
	graph.add_nodes_from(nodes)
	#print(graph.nodes)
	# initialize the class of each node
	for v, n in enumerate(nodes):
		graph.node[n]['class'] = v
		#print(graph.node[n])
		#graph.node[n]['text'] = nodes[v]
	# [(1,2), (2,3), ...]
	graph.add_edges_from(edges)
	return graph

def chinese_whispers(nodes, edges, iterations=2):
	graph = construct_graph(nodes, edges)

	for i in range(0, iterations):
		graph_nodes = list(graph.nodes())
		#print(graph_nodes)
		# random starting point
		random.shuffle(graph_nodes)
		for node in graph_nodes:
			neighbours = graph[node]
			classes = {}
			for neighbour in neighbours:
				if graph.node[neighbour]['class'] in classes:
					classes[graph.node[neighbour]['class']] += graph[node][neighbour]['weight']
				else:
					classes[graph.node[neighbour]['class']] = graph[node][neighbour]['weight']	

			max = 0
			maxclass = 0
			for c in classes:
				if classes[c] > max:
					max = classes[c]
					maxclass = c
			graph.node[node]['class'] = maxclass
			#print(graph.nodes.data('class'))

	return  nx.readwrite.json_graph.node_link_data(graph)