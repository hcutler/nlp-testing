library(data.table)
library(plyr)
setwd("/Users/Hannah-Cutler/Desktop/summer-2016/Microsoft/civictech-blog-analysis")

blog <- read.csv("unique_en_all.csv", sep=",")
graph <- read.csv("cg_entities.csv", sep=",")
d1 <- data.frame(blog)
d2 <- data.frame(graph)

both <- join(d1, d2, by = "Name",type = "inner", match = "all")

write.csv(both, "both.csv", row.names = FALSE, quote=FALSE)

bNOTg <- read.csv("blog_not_graph.csv", sep=",")
d3 <- data.frame(bNOTg)

