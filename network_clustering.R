library(igraph)

edge_list <- read.csv("ebv_target_interactions.csv", header=FALSE)

edge_list <- as.matrix(edge_list)

graph < graph_from_edgelist(edge_list, directed=FALSE)

graph <- simplify(graph)

plot(graph)

# plot(graph, vertex.label=NA)

start <- Sys.time()
tester3 <- cluster_fast_greedy(graph, weights=NULL)
system("python3 /media/wkg/storage/bender/discordnotifier.py -m ppi_clustering_done")
Sys.time() - start
