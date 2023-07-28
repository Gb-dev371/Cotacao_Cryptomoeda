# Faça um programa em python que mostre o preço do bitcoin em tempo real e os
# 5 últimos valores. Desafio bônus: mostre bitcoin, ethereum e matic. Bônus 2:
# organize num quadro numa PySimpleGUI ou tkinter

import requests
from tkinter import *
from tkinter import ttk

lista_valores = []


# Função que cria a url:
def cria_url(h, c):
    api_link = f'https://min-api.cryptocompare.com/data/v2/histo{h}?fsym={c}&tsym=BRL&limit=4'
    return api_link


# Função para pegar dados
def info(historical, cryptocurrency):

    # -- HTTP requests
    response = requests.get(cria_url(historical, cryptocurrency))

    # -- convertendo os dados em dicionário
    dados = response.json()

    referencias = dados['Data']['Data']

    for r in referencias:
        valor_brl = r['close']
        valor_formatado_brl = "R${:,.3f}".format(valor_brl)
        lista_valores.append(valor_formatado_brl)


def pega_valores(i):
    return lista_valores[i]


info("day", "BTC")
info("day", "ETH")
info("day", "MTC")


# ---------- PARTE 2 ----------

# Definindo as cores
co0 = "#444466"
co1 = "#feffff"
co2 = "#6f9fbd"

fundo = "#484f60"

janela = Tk()
janela.title('')
janela.geometry('750x300')
janela.configure(bg=fundo)


# Dividindo a janela em 2 frames
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=800, height=50, bg=co1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=800, height=400, bg=fundo, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)


# Configurando o frame cima

l_icon = Label(frame_cima, compound=LEFT, bg=co1, relief=FLAT)
l_icon.place(x=10, y=10)

l_nome = Label(frame_cima, text="Cotação de Criptomoedas", bg=co1, fg=co2, relief=FLAT, anchor='center', font=('Arial 20'))
l_nome.place(x=220, y=5)

# Configurando o frame baixo


# Bitcoin
l_t_btc = Label(frame_baixo, text="Últimas 5 variações do Bitcoin:", width=30,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_t_btc.place(x=-20, y=20)

l_v_5_btc = Label(frame_baixo, text=f"{pega_valores(0)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_5_btc.place(x=0, y=50)

l_v_4_btc = Label(frame_baixo, text=f"{pega_valores(1)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_4_btc.place(x=0, y=80)

l_v_3_btc = Label(frame_baixo, text=f"{pega_valores(2)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_3_btc.place(x=0, y=110)

l_v_2_btc = Label(frame_baixo, text=f"{pega_valores(3)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_2_btc.place(x=0, y=140)

l_v_1_btc = Label(frame_baixo, text=f"{pega_valores(4)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_1_btc.place(x=0, y=170)


# Ethereum
l_t_eth = Label(frame_baixo, text="Últimas 5 variações do Ethereum:", width=30,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_t_eth.place(x=240, y=20)

l_v_5_eth = Label(frame_baixo, text=f"{pega_valores(5)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_5_eth.place(x=240, y=50)

l_v_4_eth = Label(frame_baixo, text=f"{pega_valores(6)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_4_eth.place(x=240, y=80)

l_v_3_eth = Label(frame_baixo, text=f"{pega_valores(7)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_3_eth.place(x=240, y=110)

l_v_2_eth = Label(frame_baixo, text=f"{pega_valores(8)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_2_eth.place(x=240, y=140)

l_v_1_eth = Label(frame_baixo, text=f"{pega_valores(9)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_1_eth.place(x=240, y=170)


# Matic
l_t_mtc = Label(frame_baixo, text="Últimas 5 variações do Matic:", width=30,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_t_mtc.place(x=500, y=20)

l_v_5_mtc = Label(frame_baixo, text=f"{pega_valores(10)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_5_mtc.place(x=500, y=50)

l_v_4_mtc = Label(frame_baixo, text=f"{pega_valores(11)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_4_mtc.place(x=500, y=80)

l_v_3_mtc = Label(frame_baixo, text=f"{pega_valores(12)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_3_mtc.place(x=500, y=110)

l_v_2_mtc = Label(frame_baixo, text=f"{pega_valores(13)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_2_mtc.place(x=500, y=140)

l_v_1_mtc = Label(frame_baixo, text=f"{pega_valores(14)}", width=14,  bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_v_1_mtc.place(x=500, y=170)

janela.mainloop()
