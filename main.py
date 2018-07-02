#Importing modules
from textblob import TextBlob as tb #modulo NLP
import tweepy #Twitter API
import numpy as np #Usado para calculos estatísticos

#Configurando o app
consumer_key = '4ANHOycHd5EMSW2X5dPMAMnOK'
consumer_secret = ' EHi8F6QBhqyj6dGaN4h7sUdDiYBMcveFEiFkQhSrVOaqMs7U4c'

access_token = '86339809-KN1HZmx26KkUMNLaWi9kT0aBqk4yPTzpw1RzATfLJ'
access_token_secret = ' W9clOatxiZc5n2vh2hzxx6IEEn3qvb57ZMyCDP8tuL6zM'

#Processo de autenticação
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Chamando a API
api = tweepy.API(auth)

#procurar tweets
tweets = api.search('president')

analysis = None

#Loop for que printa todos os tweets e sua polaridade
tweets = []
for tweet in tweets:
    print(tweet.text)
    frase = tweet.text
    if frase.detect_language() != 'en':
        traducao = tb(str(frase.translate(to='en')))
        print('Tweet: {0} - Sentimento: {1}'.format(tweet.text, traducao.sentiment))
    else:
        print('Tweet: {0} - Sentimento: {1}'.format(tweet.text, frase.sentiment))
    analysis = tb(tweet.text)
    polarity = analysis.sentiment.polarity
    tweets.append(polarity)
    print(polarity)

#Checando a polaridade média dos tweets
print('SENTIMENT AVERAGE: ' + str(np.mean(tweets)))