import copy
import csv

import spacy

from ConcorrenteAmici import Concorrente_Amici

# DESCRIZIONE: produce un file .csv contenente il rank finale di ogni concorrente

data_read = []
#head = ["Id", "Screen_name", "Created_at", "Retweet", "Text", "Hashtags", "Sentiment", "Compound", "Ents"]
with open("./Risultati_finali/File_finale.csv", 'r', encoding='utf-8', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"')
    next(csv_reader)
    for row in csv_reader:
        data_read.append(row)
csv_file.close()



# SECONDA PARTE DEL CODICE
print("Analisi dettagliata dei Tweet")
nlp = spacy.load("it_core_news_sm")
nomi_concorrenti_amici = []

for row in data_read:
    lista_nomi_concorrenti_row = row[8].split(";")
    for nome_concorrente in lista_nomi_concorrenti_row:
        if nome_concorrente not in nomi_concorrenti_amici and nome_concorrente!= "":
            nomi_concorrenti_amici.append(nome_concorrente)

# creazione oggetti concorrenti per salvare gli score
concorrenti_amici_objects = []
for concorrente_amici in nomi_concorrenti_amici:  # Creazione degli oggetti dei concorrenti
    name = concorrente_amici
    concorrenti_amici_objects.append(Concorrente_Amici(name))


for row in data_read:
    amici_objects_clone = copy.deepcopy(concorrenti_amici_objects)
    doc = nlp(row[4])
    print("TWEET: ")
    print("Testo tweet: " + row[4])
    print("Sentiment: " + str(row[6]))


    ents = []
    for entity in doc.ents:
        for concorrente in concorrenti_amici_objects:
            # non mettiamo il break, a fine 'if', poichè all'interno di un soggetto potrebbero esserci più concorrenti e quindi vogliamo
            # prima estrapolare tutti i concorrenti dal soggetto e poi andare avanti col prossimo soggetto
            if ((concorrente.getName().upper() in entity.text.upper()) and (concorrente in amici_objects_clone)):
                ents.append(concorrente.getName())
                print("text: " + entity.text, ", concorrente_name: " + concorrente.getName())
                concorrente.addScore(int(row[6]))
                amici_objects_clone.pop(amici_objects_clone.index(concorrente))

    print("Ents: " + str(ents))
    print()

# Salvataggio degli score nel file
name_file_concorrenti_score = "./Risultati_finali/Amici_Score_Concorrenti(TOTALE).csv"
print(f"\nWriting in file '{name_file_concorrenti_score}' ...")

# Creazione nostro file
csv_file = open(name_file_concorrenti_score, 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
head2 = ["Name_concorrente", "score_negativo", "score_tendente_negativo", "score_neutro", "score_tendente_positivo",
         "score_positivo"]
writer.writerow(head2)

lista_rank_concorrenti = []
# Aggiunta dei concorrenti con i relativi score nel file CSV
for c in concorrenti_amici_objects:
    lista_rank_concorrenti.append(c.calculate_rank())
    writer.writerow(
        [str(c.getName()), str(c.getScoreNegativo()), str(c.getScoreTendenteNegativo()), str(c.getScoreNeutro()),
         str(c.getScoreTendentePositivo()),
         str(c.getScorePositivo())])
csv_file.close()

print(f"File '{name_file_concorrenti_score}' writing completed!")

#Migliori concorrenti: Alex, Mattia, Christian, Carola, Luigi
#Scrittura del file dove c'è il rank finale di ogni concorrente di Amici
name_file_concorrenti_rank = "./Risultati_finali/amici_rank_concorrenti(TOTALE).csv"
csv_file = open(name_file_concorrenti_rank, 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
head = ["Name_concorrente", "Rank"]
writer.writerow(head)
i = 0
for c in concorrenti_amici_objects:
    print(f"Nome: {c.getName()}, rank: {lista_rank_concorrenti[i]}")
    writer.writerow([str(c.getName()), str(lista_rank_concorrenti[i])])
    i += 1
csv_file.close()

print(f"File '{name_file_concorrenti_rank}' writing completed!")

