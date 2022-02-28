from ConcorrenteAmici import Concorrente_Amici

# DESCRIZIONE: ci sono tutti i nomi dei concorrenti di Amici

amici_cantanti = ["Crytical", "Liner", "Alex", "Sissi", "Luigi", "LDA", "Albe", "Nicole", "Rea", "Aisha", "Elena"]
amici_ballerini = ["Cosmary", "Dario", "Serena", "Carola", "Christian", "Mattia"]
concorrenti_amici = amici_cantanti + amici_ballerini

concorrenti_amici_objects = []
for concorrente_amici in concorrenti_amici: #Creazione degli oggetti dei concorrenti
    name = concorrente_amici
    concorrenti_amici_objects.append(Concorrente_Amici(name))


