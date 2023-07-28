# Cotacao_Cryptomoeda

---------------------------------------------------------------------------------------------

Esse projeto feito em python visa apresentar as últimas cinco variações do valor das criptomoedas BTC (Bitcoin), ETH (Ether) e MTC (Matic).
O arquivo main.py contem duas partes. A primeira é responsável pela parte de pegar os dados que correspondem à cotação das criptomoedas,
enquanto a segunda parte é responsável por desenvolver a interface da aplicação usando o tkinter.

---------------------------------------------------------------------------------------------

BIBLIOTECAS UTILIZADAS: 
requests
tkinter

---------------------------------------------------------------------------------------------

API UTILIZADA:
Desenvolvida pela CryptoCompare:  
Link --> https://min-api.cryptocompare.com/documentation?key=Historical&cat=dataHistoday

---------------------------------------------------------------------------------------------

BREVES EXPLICAÇÕES DO CÓDIGO:

def cria_url(h, c):
    api_link = f'https://min-api.cryptocompare.com/data/v2/histo{h}?fsym={c}&tsym=BRL&limit=4'
    return api_link

A API da cryptocompare disponibiliza as cotações das cryptomoedas de diferentes formas. Você pode ver as últimas variações com base nos dias, horas ou até minutos. Além disso, pode ver a cotação de algumas criptomoedas. No nosso caso, estamos trabalhando apenas com BTC, ETH e MTC. Perceba que existem dois parâmetros criados por mim: "h" (historical) e "c" (cryptocurrency). O esperado é que "h" receba um desses três valores: day, hour ou minute. Já "c", em nosso caso, poderia receber valores como "BTC", "ETH" ou "MTC". De acordo com esses parâmetros, o link gerado é modificado de acordo com o que nós queremos. No código, eu defino "h" como sendo "day" e para "c" passo as três cryptomoedas (uma de cada vez). Essa função é chamada quando crio a variável "response" dentro de uma outra função (que denominei "info") que faz uma requisição http que pega o link gerado. Depois converto as informações em um dicionário e guardo um tipo específico de dado na variável "referencias".  A partir desta variável, consigo pegar o valor da cotação em R$.

---------------------------------------------------------------------------------------------

INTERFACE:
![73124065-2798-4092-8731-bfdff30899f1](https://github.com/Gb-dev371/Cotacao_Cryptomoeda/assets/116456573/064a5c66-9529-458b-9eeb-316813aa16e2)
