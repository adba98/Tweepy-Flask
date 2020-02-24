import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import statistics as st
import io, base64


dth  = pd.read_csv('analisishamburguesa.csv', index_col = 'id')
dtpf = pd.read_csv('analisispapas fritas.csv', index_col = 'id')
dtpc = pd.read_csv('analisisperro caliente.csv', index_col = 'id')
dtp  = pd.read_csv('analisispizza.csv', index_col = 'id')
dts  = pd.read_csv('analisissandwich.csv', index_col = 'id')

def histograma():
    img = io.BytesIO()
    plt.hist(dth['num_siguiendo'])
    plt.title("Histograma")
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

def grap():
    img = io.BytesIO()
    tfav = pd.Series(dtpf['likes'].values, index=dtpf['fecha'])
    tret = pd.Series(dtpf['retweets'].values, index=dtpf['fecha'])
    tfav.plot(figsize=(15,4), label="Me gusta", legend=True)
    tret.plot(figsize=(15,4), label="Retweets", legend=True)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

def grap2():
    img = io.BytesIO()
    a = dtpf.groupby('fuente')['retweets'].count()
    plot = a.plot.pie(y='fuente', figsize=(7, 3))
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

def grap3():
    img = io.BytesIO()
    comida = ["hamburguesa","papas fritas","perro","pizza","sandwich"]
    valores = [dth["retweets"].sum(),dtpf["retweets"].sum(),
    dtpc["retweets"].sum(),dtp["retweets"].sum(),
    dts["retweets"].sum()]
    y_pos = np.arange(len(comida))
    plt.bar(y_pos, valores, align='center', alpha=0.9)
    plt.xticks(y_pos, comida)
    plt.ylabel('retweets')
    plt.title('Comidas rapidas')
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

def moda():
    moda = st.mode(dth['retweets'])
    return moda

def media():
    media = st.mean(dth['retweets'])
    return media

def mediana():
    mediana = st.median(dth['retweets'])
    return mediana

def medianaAgrup():
    medianaAgrup = st.median_grouped(dth['retweets'])
    return medianaAgrup

def longmedia():
    longmedia = np.mean(len(dth['texto']))
    return longmedia
