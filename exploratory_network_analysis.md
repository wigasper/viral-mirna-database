Protein-Protein Interaction Network Community Detection
================

As part of a simple exploratory analysis for this project, I am interested in identifying communities of EBV and KSHV gene targets based on their interaction partners. I am hoping that the community characteristics will yield insights, particularly with the added context of Gene Ontology annotations.

Protein-protein interaction data was initially obtained by downloading BioGRID. After insertion into my database, an edge list was generated using two queries (per virus) to isolate interactions only involving known targets of EBV and KSHV.

Community detection, plotting, and other graph functions were all done using the igraph package.

    ## 
    ## Attaching package: 'igraph'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     decompose, spectrum

    ## The following object is masked from 'package:base':
    ## 
    ##     union

First, let's look at a density plot of node degrees:

``` r
# get node degrees
degrees <- degree(graph)
degrees <- as.data.frame(degrees)
ggplot(degrees, aes(degrees)) + geom_density(color="firebrick3", fill="firebrick3", alpha=0.4) + coord_cartesian(xlim=c(0,150))
```

![](exploratory_network_analysis_files/figure-markdown_github/unnamed-chunk-2-1.png)

Not suprisingly, the degree distribution is highly skewed, characteristic of a scale-free network. This may also be somewhat due to scientific focus on studying certain genes. For example, the top few genes with the most interaction partners are:

``` r
temp_df <- data.frame(rownames(degrees), c(degrees$degrees))
names(temp_df) <- c("Gene", "Degree")
temp_df <- temp_df[order(-temp_df$Degree),]
#degrees <- degrees[order(-degrees$degrees),]
knitr::kable(head(temp_df, n=10), row.names=TRUE)
```

|      | Gene   |  Degree|
|------|:-------|-------:|
| 771  | ELAVL1 |    1787|
| 599  | XPO1   |    1263|
| 139  | BRCA1  |    1002|
| 339  | MCM2   |     952|
| 6354 | TNIP2  |     897|
| 3878 | RNF2   |     736|
| 4048 | CDK2   |     690|
| 171  | EWSR1  |     670|
| 3788 | MYC    |     665|
| 3764 | CHD4   |     644|

Next, community membership is decided using the infomap algorithm:

``` r
communities <- cluster_infomap(graph, nb.trials=10)
length(communities)
```

    ## [1] 591

``` r
V(graph)$community <- communities$membership
colors <- palette(terrain.colors(length(communities), alpha=.6))
plot(graph, vertex.color=colors[V(graph)$community], vertex.label=NA)
```

![](exploratory_network_analysis_files/figure-markdown_github/unnamed-chunk-5-1.png)
