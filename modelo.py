import pandas as pd

def process_results(results):
    id_list = [tweet.id for tweet in results]
    data_set = pd.DataFrame(id_list, columns=["id"])

    # Processing Tweet Data
    data_set["texto"] = [tweet.text for tweet in results]
    data_set["fecha"] = [tweet.created_at for tweet in results]
    data_set["retweets"] = [tweet.retweet_count for tweet in results]
    data_set["likes"] = [tweet.favorite_count for tweet in results]
    data_set["fuente"] = [tweet.source for tweet in results]   
    
    # Processing User Data
    data_set["nickname"] = [tweet.author.screen_name for tweet in results]
    data_set["num_seguidores"] = [tweet.author.followers_count for tweet in results]
    data_set["num_siguiendo"] = [tweet.author.friends_count for tweet in results]
    data_set["ubicacion"] = [tweet.author.location for tweet in results]
    data_set["listas"] = [tweet.author.listed_count for tweet in results]
    
    return data_set

