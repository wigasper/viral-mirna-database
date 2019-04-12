library(igraph)

edge_list <- read.csv("ebv_target_interactions.csv", header=FALSE)

edge_list <- as.matrix(edge_list)

graph <- graph_from_edgelist(edge_list, directed=FALSE)

graph <- simplify(graph)

#plot(graph)

# Walktrap testing, here I am looking for the steps value that minimizes
# the number of communities (to a certain extent)
steps <- c(20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80)
comm_size <- c()
times <- c()
for (step in steps)
{
  start <- Sys.time()
  communities <- cluster_walktrap(graph, weights=NULL, steps=step)
  comm_size <- c(comm_size, length(communities))
  times <- c(times, (Sys.time() - start))
}
system("python3 /media/wkg/storage/bender/discordnotifier.py -m ppi_clustering_done")
results <- data.frame(steps, comm_size, times)
#start <- Sys.time()
#communities <- cluster_fast_greedy(graph, weights=NULL)
#maybe edit walktrap steps???
# 6 steps has lowest num of communities right now
#communities <- cluster_walktrap(graph, weights=NULL, steps=35)
#communities <- cluster_edge_betweenness(graph, weights=NULL)
#system("python3 /media/wkg/storage/bender/discordnotifier.py -m ppi_clustering_done")
#Sys.time() - start

#plot(communities, graph)

V(graph)$community <- communities$membership
colors <- palette(terrain.colors(length(communities), alpha=.6))
plot(graph, vertex.color=colors[V(graph)$community], vertex.label=NA)

# get membership values for nodes
membership <- cbind(V(graph)$name, communities$membership)
