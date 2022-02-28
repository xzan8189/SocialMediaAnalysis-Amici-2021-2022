function_retta_di_regressione <- function(indice_concorrente, main) {
  matrix <- as.matrix(rank_days)
  concorrente<-indice_concorrente
  start_column<-3
  end_column <- 32
  first_15_rank <- c()
  last_15_rank <- c()
  for (start_column in start_column:end_column) {
    if (start_column<=17) {
      first_15_rank = c(
        first_15_rank, 
        as.double(matrix[[concorrente:concorrente,start_column:start_column]])
        )
    } else {
      last_15_rank = c(
        last_15_rank, 
        as.double(matrix[[concorrente:concorrente,start_column:start_column]])
      )
    }
    start_column = start_column + 1
  }
  
  x1 <- first_15_rank
  x2 <- last_15_rank
  
  plot(x1,x2,main=main,
       xlab="Ultimi 15 giorni",ylab="Primi 15 giorni",
       col="red")
  abline(lm(x2~x1),col="blue")
  stime<-fitted(lm(x2~x1))
  segments(x1,stime,x1,x2,col="magenta")
}

function_retta_di_regressione(5, "Retta di regressione e residui\nLuigi")
function_retta_di_regressione(4, "Retta di regressione e residui\nCarola")
function_retta_di_regressione(7, "Retta di regressione e residui\nChristian")
function_retta_di_regressione(2, "Retta di regressione e residui\nMattia")
function_retta_di_regressione(6, "Retta di regressione e residui\nAlex")