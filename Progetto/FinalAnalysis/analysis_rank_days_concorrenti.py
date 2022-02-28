import copy
import csv
import os

import spacy

from ConcorrenteAmici import Concorrente_Amici

# DESCRIZIONE: produce un file .csv contenente il rank di ogni giorno per ogni concorrente

# SECONDA PARTE DEL CODICE
print("Analisi dettagliata dei Tweet")
nlp = spacy.load("it_core_news_sm")
nomi_concorrenti_amici = []

data_read = []

#Prendiamo tutte le righe del file 'File_finale.csv'
with open("./Risultati_finali/File_finale.csv", 'r', encoding='utf-8', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"')
    next(csv_reader)
    for row in csv_reader:
        data_read.append(row)
csv_file.close()

#Prendiamo tutti i nomi dei concorrenti
for row in data_read:
    lista_nomi_concorrenti_row = row[8].split(";")
    for nome_concorrente in lista_nomi_concorrenti_row:
        if nome_concorrente not in nomi_concorrenti_amici and nome_concorrente!= "":
            nomi_concorrenti_amici.append(nome_concorrente)

array_giorni_concorrenti = []
#head = ["Id", "Screen_name", "Created_at", "Retweet", "Text", "Hashtags", "Sentiment", "Compound", "Ents"]
# Cattura delle righe dei csv dei tweets 2022
folder_path_tweets_2021 = os.getcwd() + "\\tweets (2021)"
for filename in os.listdir(folder_path_tweets_2021):
    data_read_temp = []
    if (filename=="desktop.ini"):
        continue
    print(f"File name: {filename}")
    with open(folder_path_tweets_2021 + "\\" + filename, 'r', encoding='utf-8', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"')
        next(csv_reader)
        for row in csv_reader:
            data_read_temp.append(row)
    csv_file.close()
    # creazione oggetti concorrenti per salvare gli score
    concorrenti_amici_objects = []
    for concorrente_amici in nomi_concorrenti_amici:  # Creazione degli oggetti dei concorrenti
        name = concorrente_amici
        concorrenti_amici_objects.append(Concorrente_Amici(name))

    for row in data_read_temp:
        amici_objects_clone = copy.deepcopy(concorrenti_amici_objects)
        doc = nlp(row[4])

        ents = []
        for entity in doc.ents:
            for concorrente in concorrenti_amici_objects:
                # non mettiamo il break, a fine 'if', poichè all'interno di un soggetto potrebbero esserci più concorrenti e quindi vogliamo
                # prima estrapolare tutti i concorrenti dal soggetto e poi andare avanti col prossimo soggetto
                if ((concorrente.getName().upper() in entity.text.upper()) and (concorrente in amici_objects_clone)):
                    ents.append(concorrente.getName())
                    #print("text: " + entity.text, ", concorrente_name: " + concorrente.getName())
                    concorrente.addScore(int(row[6]))
                    amici_objects_clone.pop(amici_objects_clone.index(concorrente))

    array_giorni_concorrenti.append(concorrenti_amici_objects)
    for c in concorrenti_amici_objects:
        print(c)

# Scrittura dei rank di ogni giorno di ogni concorrente
with open("./Risultati_finali/rank_days.csv", 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    end_format_day = "/12/2021"
    head = []
    head.append("nomi_concorrenti")
    for i in range(31):
        day = i+1
        head.append(f"d{str(day)}{end_format_day}")

    writer.writerow(head)


    for j in range(len(nomi_concorrenti_amici)):
        temp_row_score = []
        temp_row_score.append(nomi_concorrenti_amici[j])
        for i in range(len(array_giorni_concorrenti)):
            temp_row_score.append(str(array_giorni_concorrenti[i].__getitem__(j).calculate_rank()))

        writer.writerow(temp_row_score)

csv_file.close()
