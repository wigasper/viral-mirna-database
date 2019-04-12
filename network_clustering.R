library(igraph)

edge_list <- read.csv("ebv_target_interactions.csv", header=FALSE)

edge_list <- as.matrix(edge_list)

graph <- graph_from_edgelist(edge_list, directed=FALSE)

graph <- simplify(graph)

#plot(graph)

# plot(graph, vertex.label=NA)

start <- Sys.time()
#communities <- cluster_fast_greedy(graph, weights=NULL)
#maybe edit walktrap steps???
communities <- cluster_walktrap(graph, weights=NULL)
#communities <- cluster_edge_betweenness(graph, weights=NULL)
system("python3 /media/wkg/storage/bender/discordnotifier.py -m ppi_clustering_done")
Sys.time() - start

#plot(communities, graph)

V(graph)$community <- communities$membership
colors <- palette(terrain.colors(1024, alpha=.6))
plot(graph, vertex.color=colors[V(graph)$community], vertex.label=NA)
