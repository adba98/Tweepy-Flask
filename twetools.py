import tweepy
import json
import pandas as pd
import modelo as md

# Clave de consumidor (clave de API)
consumer_key = 'eDKAdQHwyqrda8oyDBz7EgRe4'
consumer_secret = 'PYtBkEqPNUerzeaeBDU9m4z0u86nCKv6shz8YJTEHDRAXN5Or2'

# Secreto del consumidor (API Secret)
access_token = '1228005953435504640-16igZpdxUxv9EWgHL1UjSOLwxQ27ay'
access_token_secret = '9U0hXgq58UXrZ0WGAcsjcQmIT1Dwp2nTyglZuLV8pawEF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

results = []
# Palabras clave: hamburguesa, papas fritas, perro caliente, pizza, sandwich

# Buscar Palabra
def buscPalabra(keyword):
    for tweet in tweepy.Cursor(api.search, q=keyword, lang="es", include_entities = True).items(100):
        results.append(tweet)
    return results

def generar(keyword):
    data_set = md.process_results(results)
    #data_set["fecha"] = pd.to_datetime(data_set["fecha"])
    data_set.to_csv("analisis"+keyword+".csv")
    return data_set

# Timeline
def timeline(usuario):
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = usuario, tweet_mode = "extend").items(1):
        return json.dumps(tweet._json, indent=2)

# Buscar Twets
def tweet():
    for tweet in tweepy.Cursor(api.search, q='jugo', tweet_mode = "extend").items(2):
        return(tweet._json["text"])
