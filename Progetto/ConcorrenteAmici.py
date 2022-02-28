class Concorrente_Amici:

    # Metodo costruttore
    def __init__(self, name):
        self.name = name
        self.score_negativo = 0
        self.score_tendente_negativo = 0
        self.score_neutro = 0
        self.score_tendente_positivo = 0
        self.score_positivo = 0

    # Getter
    def getName(self):
        return self.name
    def getScoreNegativo(self):
        return self.score_negativo
    def getScoreTendenteNegativo(self):
        return self.score_tendente_negativo
    def getScoreNeutro(self):
        return self.score_neutro
    def getScoreTendentePositivo(self):
        return self.score_tendente_positivo
    def getScorePositivo(self):
        return self.score_positivo

    # Setter
    def setName(self, name):
        self.name = name
    def setScoreNegativo(self, score):
        self.score_negativo = score
    def setScoreTendenteNegativo(self, score):
        self.score_tendente_negativo = score
    def setScoreNeutro(self, score):
        self.score_neutro = score
    def setScoreTendentePositivo(self, score):
        self.score_tendente_positivo = score
    def setScorePositivo(self, score):
        self.score_positivo = score

    # Metodi d'appoggio
    def addScore(self, type: int):
        int(type)
        if (type == 1):
            self.score_negativo += 1
        elif (type == 2):
            self.score_tendente_negativo += 1
        elif (type == 3):
            self.score_neutro += 1
        elif (type == 4):
            self.score_tendente_positivo += 1
        elif (type == 5):
            self.score_positivo += 1
        elif ():
            print("ERRORE IN FUNZIONE 'addScore' di 'Concorrente_Amici'")

    # Metodi d'appoggio
    def calculate_rank(self):
        rank = 0.0
        rank += float(self.getScoreNegativo() * (-1))
        rank += float(self.getScoreTendenteNegativo() * (-0.5))
        rank += float(self.getScoreNeutro() * (0))
        rank += float(self.getScoreTendentePositivo() * (+0.5))
        rank += float(self.getScorePositivo() * (+1))

        return rank

    # Metodi sovrascritti
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Concorrente_Amici):
            return self.name == o.name

    def __str__(self):
        return f"Name: {self.getName()}\n" \
               f"score_negativo: {str(self.getScoreNegativo())}\n" \
               f"score_tendente_negativo: {str(self.getScoreTendenteNegativo())}\n" \
               f"score_neutro: {str(self.getScoreNeutro())}\n" \
               f"score_tendente_positivo: {str(self.getScoreTendentePositivo())}\n" \
               f"score_positivo: {str(self.getScorePositivo())}\n"