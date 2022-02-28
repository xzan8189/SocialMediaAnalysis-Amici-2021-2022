matrix <- as.matrix(rank_days)
#matrix[2:20,]

type_line="l"
nomi_concorrenti_da_stampare = c("Alex","Mattia","Christian","Carola","Luigi")
plot_rank_days <- plot(x=rep(c(0),each=31),
                       main = "Andamento popolarità dei 5 migliori concorrenti",
                       xlab = "Giorni",
                       ylab ="Rank", 
                       ylim=c(-5,15),
                       lty=2,
                       type="l")
plot_rank_days

colors <- c("RED","#ff8400","#88ff00","#0048ff","#9000ff")
j<-1
i<-1
row_end <- 20
names_for_legend<-c()
colors_for_legend<-c()
for (i in i:row_end) {
  if (matrix[i,1:1] %in% nomi_concorrenti_da_stampare) {
    print(matrix[i,1:1])
    names_for_legend <- c(names_for_legend, matrix[i,1:1])
    lines ( matrix[i,2:32] , col =colors[j], type=type_line)
    colors_for_legend <- c(colors_for_legend, col=colors[j])
    j <- j+1
    i <- i+1
  }
}
legend(x=18,y=14,legend=names_for_legend, ncol=3, fill=colors_for_legend, cex=0.7)


# #inserimento colori nella legend
# i<-1
# for (i in i:row_end) {
#   colors_for_legend <- c(colors_for_legend, i)
#   i <- i+1
# }
# 
# #inserimento nomi nella legend
# names_for_legend<-c()
# i<-1
# for (i in i:row_end) {
#   names_for_legend <- c(names_for_legend, matrix[i,1:1])
#   i <- i+1
# }
# legend(x=15,y=14,legend=names_for_legend, ncol=5, fill=colors_for_legend, cex=0.6)
# abline(h=0)