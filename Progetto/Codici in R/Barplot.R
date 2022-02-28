createBarplot<-function(ranks, main){
  
  x<-barplot(ranks, ylab="Ranks", main=main,
             col=1:40,
             las=2,
             names.arg=`amici_rank_concorrenti(TOTALE)`[,1:1],
             cex.axis=0.80,
             cex.names=0.80,
             font.lab=2)
  abline(h=mean(ranks),col="red",lty=2,xpd=FALSE)
  print(mean(ranks))
  print(median(ranks))
  print(var(ranks))
  print(sd(ranks))
}

createBarplot(`amici_rank_concorrenti(TOTALE)`[,2:2], "Rank dei concorrenti nel mese di Dicembre")

