from tkinter import *
from tkinter import ttk

#  importando o pillow

from PIL import  Image, ImageTk

from dados import *

#cores
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#ef5350"  # vermelha

#criando janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief="flat")
frame_pokemon.grid(row=1, column=0)


def trocar_pok(i):
    global imagem_pokemon, pok_image

    #cor de fundo frame
    frame_pokemon['bg'] = pokemon[i]['tipo'][3]

    #tipo do pokemon
    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['tipo'][3]
    pok_tipo['text'] = pokemon[i]['tipo'][1]
    pok_tipo['bg'] = pokemon[i]['tipo'][3]
    pok_id['text'] = pokemon[i]['tipo'][0]
    pok_id['bg'] = pokemon[i]['tipo'][3]

    
    imagem_pokemon = pokemon[i]['tipo'][2]


    # imagem do pokemon 
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    pok_image = Label(frame_pokemon, image=imagem_pokemon, relief='flat', bg= pokemon[i]['tipo'][3], fg=co1)
    pok_image.place(x=60, y=50)

    pok_tipo.lift()

    # pokemon status
    pok_hp['text'] = pokemon[i]['status'][0]
    pok_attack['text'] = pokemon[i]['status'][1]
    pok_defesa['text'] = pokemon[i]['status'][2]
    pok_velocidade['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]


    #pokemon habilidades
    pok_hb_1['text'] = pokemon[i]['habilidades'][0]
    pok_hb_2['text'] = pokemon[i]['habilidades'][1]

# nome
pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
pok_nome.place(x=12, y=15)


# categoria
pok_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_tipo.place(x=12, y=50)

# id
pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_id.place(x=12, y=75)


# status
pok_status = Label(janela, text="Status", relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

# hp 
pok_hp = Label(janela, text="HP: 39", relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_hp.place(x=15, y=360)

# attack
pok_attack = Label(janela, text="Ataque: 52", relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_attack.place(x=15, y=385)

# defesa
pok_defesa = Label(janela, text="Defesa: 43", relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_defesa.place(x=15, y=410)

# velocidade
pok_velocidade = Label(janela, text="Velocidade: 65", relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_velocidade.place(x=15, y=435)

# total
pok_total = Label(janela, text="Total: 309", relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_total.place(x=15, y=460)


# habilidades
pok_status = Label(janela, text="Habilidades", relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=180, y=310)

# hp 
pok_hb_1 = Label(janela, text="", relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_hb_1.place(x=195, y=360)

# attack
pok_hb_2 = Label(janela, text="", relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_hb_2.place(x=195, y=385)

 
#criando botões 
# charmander 
imagem_pokemon_1 = Image.open('pokemon/imagens/charmander.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

b_pok_1= Button(janela,command = lambda:trocar_pok('Charmander'),image=imagem_pokemon_1, text='charmander', width=150, relief='raised',overrelief=RIDGE, compound= LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=10)

#eevee
imagem_pokemon_2 = Image.open('pokemon/imagens/eevee.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

b_pok_2= Button(janela,command = lambda:trocar_pok('Eevee'),image=imagem_pokemon_2, text='Eevee', width=150, relief='raised',overrelief=RIDGE, compound= LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_2.place(x=375, y=65)


#mimikyu
imagem_pokemon_3 = Image.open('pokemon/imagens/mimikyu.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

b_pok_3 = Button(janela,command = lambda:trocar_pok('Mimikyu'), image=imagem_pokemon_3, text='Mimikyu', width=150, relief='raised',overrelief=RIDGE, compound= LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_3.place(x=375, y=120)


#psyduck
imagem_pokemon_4 = Image.open('pokemon/imagens/psyduck.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

b_pok_4= Button(janela,command = lambda:trocar_pok('Psyduck'),image=imagem_pokemon_4, text='Psyduck', width=150, relief='raised',overrelief=RIDGE, compound= LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_4.place(x=375, y=175)

#pumpkaboo
imagem_pokemon_5 = Image.open('pokemon/imagens/pumpkaboo.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

b_pok_5= Button(janela,command = lambda:trocar_pok('Pumpkaboo'), image=imagem_pokemon_5, text='Pumpkaboo', width=150, relief='raised',overrelief=RIDGE, compound= LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_5.place(x=375, y=230)


#togepi
imagem_pokemon_6 = Image.open('pokemon/imagens/togepi.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

b_pok_6= Button(janela,command = lambda:trocar_pok('Togepi'), image=imagem_pokemon_6, text='Togepi', width=150, relief='raised',overrelief=RIDGE, compound= LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_6.place(x=375, y=285)


#mewtwo
imagem_pokemon_7 = Image.open('pokemon/imagens/mewtwo.png')
imagem_pokemon_7 = imagem_pokemon_7.resize((40, 40))
imagem_pokemon_7 = ImageTk.PhotoImage(imagem_pokemon_7)

b_pok_7= Button(janela,command = lambda:trocar_pok('Mewtwo'), image=imagem_pokemon_7, text='Mewtwo', width=150, relief='raised',overrelief=RIDGE, compound= LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_7.place(x=375, y=340)


#pikachu
imagem_pokemon_8 = Image.open('pokemon/imagens/pikachu.png')
imagem_pokemon_8 = imagem_pokemon_8.resize((40, 40))
imagem_pokemon_8= ImageTk.PhotoImage(imagem_pokemon_8)

b_pok_8= Button(janela,command = lambda:trocar_pok('Pikachu'), image=imagem_pokemon_8, text='Pikachu', width=150, relief='raised',overrelief=RIDGE, compound= LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_8.place(x=375, y=395)


#bulbassauro
imagem_pokemon_9 = Image.open('pokemon/imagens/bulbasaur.png')
imagem_pokemon_9 = imagem_pokemon_9.resize((40, 40))
imagem_pokemon_9 = ImageTk.PhotoImage(imagem_pokemon_9)

b_pok_9= Button(janela,command = lambda:trocar_pok('Bulbassauro'), image=imagem_pokemon_9, text='Bulbassauro', width=150, relief='raised',overrelief=RIDGE, compound= LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_9.place(x=375, y=450)


janela.mainloop()
