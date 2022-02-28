import csv
import os

# DESCRIZIONE: produce un file .csv contenente i tweets di tutti i giorni

array_stampa=[]

# Cattura delle righe dei csv dei tweets 2021
folder_path_tweets_2021 = os.getcwd() + "\\tweets (2021)"
for filename in os.listdir(folder_path_tweets_2021):
    if (filename=="desktop.ini"):
        continue
    print(f"File name: {filename}")
    with open(folder_path_tweets_2021 + "\\" + filename, 'r', encoding='utf-8', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"')
        next(csv_reader)
        for row in csv_reader:
            array_stampa.append(row)
    csv_file.close()

# Cattura delle righe dei csv dei tweets 2022
folder_path_tweets_2021 = os.getcwd() + "\\tweets (2022)"
for filename in os.listdir(folder_path_tweets_2021):
    if (filename=="desktop.ini"):
        continue
    print(f"File name: {filename}")
    with open(folder_path_tweets_2021 + "\\" + filename, 'r', encoding='utf-8', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"')
        next(csv_reader)
        for row in csv_reader:
            array_stampa.append(row)
    csv_file.close()

# Scrittura di tutti i tweets nel file 'File_finale.csv'
csv_file = open("./Risultati_finali/File_finale.csv", 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
head = ["Id", "Screen_name", "Created_at", "Retweet", "Text", "Hashtags", "Sentiment", "Compound", "Ents"]
writer.writerow(head)
writer.writerows(array_stampa)
csv_file.close()