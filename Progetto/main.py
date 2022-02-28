import spacy
import tweepy

from concorrenti import *
from functions_utils import *
from Tweet import Tweet
from config import *

# Login
CONFIG = DefaultConfig()
auth = tweepy.OAuthHandler(CONFIG.CONS_KEY, CONFIG.CONS_SECR)
auth.set_access_token(CONFIG.ACCESS_TOKEN, CONFIG.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Variabili
tweets = []
tweetsTranslated = []

# Inserimento Hashtag da cercare
inputTerm = "#Amici21 AND ("
for i in range(len(concorrenti_amici)):
    if (i < (len(concorrenti_amici)-1)):
        inputTerm += "#" + concorrenti_amici[i] + " OR "
    elif (i == (len(concorrenti_amici)-1)):
        inputTerm += "#" + concorrenti_amici[i] + ")"

print("--------------Operazioni preliminari-------------")
print("Concorrenti di Amici: \n" + str(concorrenti_amici) + "\n")
print("L'inputTerm: \n" + inputTerm)
searchTerm = inputTerm + " -filter:retweets"

print("-------------------------------------------------")
print()
print("Start Tweet Capturing..")
date_tweepy = "2022-01-28"
date_to_match_into_CSV = "2022-01-27"
for tweet in tweepy.Cursor(api.search_tweets,q=searchTerm, lang="it",
                           until = date_tweepy,
                           result_type="mixed",
                           tweet_mode="extended").items(100):
    rt_count = tweet.retweet_count
    p2 = ["", tweet.full_text]
    hast = ""
    a = tweet.full_text.count("#")
    if (a >= 0):
        for c in range(a):
            p1 = p2[1].split("#", 1)
            try:
                if (p1[1].find(" ") < 0):
                    hast += "#" + p1[1]
                    hast = hast.replace("\n", "")
                    break
                else:
                    p2 = p1[1].split(" ", 1)
                    hast += "#" + p2[0]
                    hast = hast.replace("\n", "")
            except IndexError:
                hast+="#"+p1[0]
        tweet.full_text = cleanTweet(tweet.full_text)
        hast = cleanHashtags(hast)

        tt = {
            "Id": tweet.id,
            "Screen_name": tweet.user.name,
            "Created_at": tweet.created_at,
            "Retweet": str(rt_count),
            "Text": tweet.full_text,
            "Hashtags": hast,
            "Sentiment": 0,
            "Compound": 0
        }
        tt = Tweet(tweet.id, tweet.user.name, tweet.created_at, str(rt_count), tweet.full_text, hast, 0, 0)
        if (str(tt.getCreated_at()).find(date_to_match_into_CSV) != -1):
            tweets.append(tt)   # Tweet italiani
            tweetsTranslated.append(translatorTweet(tt))  #Tweet inglesi

# Traduzione e sentiment score dei tweet
for i in tweets:
    calculate_and_set_compound_score_to_tweet(i)
    calculate_and_set_sentiment_score_to_tweet(i)
    print_tweet(i)
    print_emotion_score(i)
    print()

# Per procedere con la SECONDA PARTE del codice bisogna installare le seguenti librerie (sono presenti già nel file 'requirements.txt'
# pip install -U pip setuptools wheel
# pip install -U spacy
# python -m spacy download en_core_web_sm
# python -m spacy download it_core_news_sm

# SECONDA PARTE DEL CODICE
print("Analisi più dettagliata dei Tweet")
nlp = spacy.load("it_core_news_sm")

print(concorrenti_amici)
for tweet in tweets:
    amici_objects_clone = copy.deepcopy(concorrenti_amici_objects)
    doc = nlp(tweet.getText())
    print("TWEET: ")
    print("Testo tweet: " + tweet.getText())
    print("Sentiment: " + str(tweet.getSentiment()))

    ents = []
    for entity in doc.ents:
        for concorrente in concorrenti_amici_objects:
            # non mettiamo il break, a fine 'if', poichè all'interno di un soggetto potrebbero esserci più concorrenti e quindi vogliamo
            # prima estrapolare tutti i concorrenti dal soggetto e poi andare avanti col prossimo soggetto
            if ((concorrente.getName().upper() in entity.text.upper()) and (concorrente in amici_objects_clone)):
                ents.append(concorrente.getName())
                print("text: " + entity.text, ", concorrente_name: " + concorrente.getName())
                concorrente.addScore(tweet.getSentiment())
                amici_objects_clone.pop(amici_objects_clone.index(concorrente))
                #print("FINE " + "text: " + entity.text, "type/label: " + entity.label_)

    tweet.setEnts(ents)
    print("Ents: " + str(tweet.getEnts()))
    print()

print("LISTA CON PUNTEGGI")
for c in concorrenti_amici_objects:
    print("Name: " + c.getName())
    print("score_negativo: " + str(c.getScoreNegativo()))
    print("score_tendente_negativo: " + str(c.getScoreTendenteNegativo()))
    print("score_neutro: " + str(c.getScoreNeutro()))
    print("score_tendente_positivo: " + str(c.getScoreTendentePositivo()))
    print("score_positivo: " + str(c.getScorePositivo()))
    print()


print("Done analysis!")


