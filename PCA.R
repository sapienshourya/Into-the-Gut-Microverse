

ge.data <- read.csv("", header = TRUE)
d <- ge.data[ , 3:5 ]
d.pca <- prcomp(d, center = TRUE, scale = TRUE)
summary(d.pca)
pv <- (d.pca$sdev^2)/sum(d.pca$sdev^2)
plot(pv, xlab = "Principal Component", 
     ylab = "PVE", 
     pch = 20, cex = 2, col = 4)

cpv <- cumsum(pv)
plot(cpv, xlab = "Principal Component", 
     ylab = "Cumulative PVE", 
     pch = 20, cex = 2, col = 2)

d.load <- d.pca$rotation
d.score <-d.pca$x

library(ggbiplot)
p1 <- ggbiplot(d.pca, choices= c(1,2), obs.scale = 1, 
               var.scale = 1,labels = ge.data[ ,2])
print(p1)



p1 <- p1 + xlim(-2,2) + ylim(-2,2)

print(p1)



p2<-  ggbiplot(d.pca, choices= c(1,2), obs.scale = 1, var.scale = 1, 
              labels = ge.data[,2], groups = ge.data[ ,1], 
              var.axes = FALSE) 
print(p2)

