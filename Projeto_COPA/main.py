
from cgitb import text
from email.mime import image
from gzip import READ
from tkinter import ttk
from PIL import Image,ImageTk
import PIL  #pillow
import io
import base64
from tkinter import *
from img_B64 import *
from buscas import *
from janela_1930_uruguai import *

root = Tk()

class Application(Imagens,Listas,Janela_1930):
    def __init__(self,master=None):
        self.root = root
        self.img_64()
        self.tela()
        self.busca()
        self.frames_main()
        self.widgats_principal()
        
        root.mainloop()

    def tela(self):
        self.root.title('Copa do Mundo')
        self.root.geometry('1200x1000+10+10')

    def frames_main(self):
        self.frame_1_main = Frame(self.root)
        self.frame_1_main.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.20)
        
        self.frame_2_main = Frame(self.root,bg='lightgreen')
        self.frame_2_main.place(relx=0.01,rely=0.22,relwidth=0.57,relheight=0.77)

        self.frame_3_main = Frame(self.root,bg='green')
        self.frame_3_main.place(relx=0.59,rely=0.22,relwidth=0.40,relheight=0.77)

    # Imagem da Label do Título
        self.stadio = base64.b64decode(self.stadio_B64)
        self.lb_titulo = PIL.Image.open(io.BytesIO(self.stadio))
        self.lb_titulo = self.lb_titulo.resize((1200, 200))
        self.lb_titulo = ImageTk.PhotoImage(self.lb_titulo)

        self.label_titulo = Label(self.frame_1_main, image=self.lb_titulo,
                                  text='copa do mundo'.upper(), width=900,
                                  compound=CENTER, relief=RAISED, anchor=NW,
                                  font=('verdana 70 bold'), fg='#cfd5e1')
        self.label_titulo.place(relx=0, rely=0, relwidth=1, relheight=1)

 # Botoes Label e Entry
    def widgats_principal(self):

    # LABEL TAÇA
        self.label_taca = Label(self.frame_3_main, text=' " A TAÇA do mundo é Nossa, \ncom o brasileiro não há quem possa..."\n\n Essa foi uma das canções \nque ecoavam durante as copas \n que se seguiram ao longo dos anos...'.upper(), font=('verdana 12 bold'), bg='lightblue')
        self.label_taca.place(relx=0.01, rely=0.64, relwidth=0.98, relheight=0.35)
        
    # TAÇA
        self.taca= base64.b64decode(self.taca_dividida)
        self.bt_taca_dividida = PIL.Image.open(io.BytesIO(self.taca))
        self.bt_taca_dividida = self.bt_taca_dividida.resize((450, 450))
        self.bt_taca_dividida= ImageTk.PhotoImage(self.bt_taca_dividida)

        self.botao_ano = Button(self.frame_3_main,
                            image=self.bt_taca_dividida,font=('verdana 10 bold'),
                            width=900,compound=TOP,relief=RAISED,anchor=NW)
        self.botao_ano.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.62)
   
    # 1930 - URUGUAI
        self.uruguai_30 = base64.b64decode(self.uruguai_1930)
        self.bt_1930 = PIL.Image.open(io.BytesIO(self.uruguai_30))
        self.bt_1930 = self.bt_1930.resize((72, 89))
        self.bt_1930 = ImageTk.PhotoImage(self.bt_1930)

        self.botao_img1930 = Button(self.frame_2_main, image=self.bt_1930,command=self.janela_1930,
                                    text='Copa de 1930\nuruguai'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1930.place(relx=0.02, rely=0.02, relwidth=0.16, relheight=0.17)
          
    # 1934 - ITÁLIA
        self.italia_34 = base64.b64decode(self.italia_1934)
        self.bt_1934 = PIL.Image.open(io.BytesIO(self.italia_34))
        self.bt_1934 = self.bt_1934.resize((72, 89))
        self.bt_1934 = ImageTk.PhotoImage(self.bt_1934)

        self.botao_img1934 = Button(self.frame_2_main, image=self.bt_1934,
                                    text='Copa de 1934\nitália'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1934.place(relx=0.22, rely=0.02, relwidth=0.16, relheight=0.17)

    # 1938 - FRANÇA
        self.franca_38 = base64.b64decode(self.franca_1938)
        self.bt_1938 = PIL.Image.open(io.BytesIO(self.franca_38))
        self.bt_1938 = self.bt_1938.resize((72, 89))
        self.bt_1938 = ImageTk.PhotoImage(self.bt_1938)

        self.botao_img1938 = Button(self.frame_2_main, image=self.bt_1938,
                                    text='Copa de 1938\nfrança'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1938.place(relx=0.42, rely=0.02, relwidth=0.16, relheight=0.17)

    # 1950 - BRASIL    
        self.brasil_50 = base64.b64decode(self.brasil_1950)
        self.bt_1950 = PIL.Image.open(io.BytesIO(self.brasil_50))
        self.bt_1950 = self.bt_1950.resize((72, 89))
        self.bt_1950 = ImageTk.PhotoImage(self.bt_1950)

        self.botao_img1950 = Button(self.frame_2_main, image=self.bt_1950,
                                    text='Copa de 1950\nBrasil'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1950.place(relx=0.62, rely=0.02, relwidth=0.16, relheight=0.17)

    # 1954 - SUIÇA
        self.suica_54 = base64.b64decode(self.suica_1954)
        self.bt_1954 = PIL.Image.open(io.BytesIO(self.suica_54))
        self.bt_1954 = self.bt_1954.resize((72, 89))
        self.bt_1954 = ImageTk.PhotoImage(self.bt_1954)

        self.botao_img1954 = Button(self.frame_2_main, image=self.bt_1954,
                                    text='Copa de 1954\nSuiça'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1954.place(relx=0.82, rely=0.02, relwidth=0.16, relheight=0.17)

    # 1958 - SUÉCIA
        self.suecia_58 = base64.b64decode(self.suecia_1958)
        self.bt_1958 = PIL.Image.open(io.BytesIO(self.suecia_58))
        self.bt_1958 = self.bt_1958.resize((72, 89))
        self.bt_1958 = ImageTk.PhotoImage(self.bt_1958)

        self.botao_img1958 = Button(self.frame_2_main, image=self.bt_1958,
                                    text='Copa de1958\nSuécia'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1958.place(relx=0.02, rely=0.20, relwidth=0.16, relheight=0.17)

    # 1962 - CHILE
        self.chile_62 = base64.b64decode(self.chile_1962)
        self.bt_1962 = PIL.Image.open(io.BytesIO(self.chile_62))
        self.bt_1962 = self.bt_1962.resize((72, 89))
        self.bt_1962 = ImageTk.PhotoImage(self.bt_1962)

        self.botao_img1962 = Button(self.frame_2_main, image=self.bt_1962,
                                    text='Copa de 1962\nChile'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1962.place(relx=0.22, rely=0.20, relwidth=0.16, relheight=0.17)

    # 1966 - INGLATERRA
        self.inglaterra_66 = base64.b64decode(self.inglaterra_1966)
        self.bt_1966 = PIL.Image.open(io.BytesIO(self.inglaterra_66))
        self.bt_1966 = self.bt_1966.resize((72, 89))
        self.bt_1966 = ImageTk.PhotoImage(self.bt_1966)

        self.botao_img1966 = Button(self.frame_2_main, image=self.bt_1966,
                                    text='Copa de 1966\nInglaterra'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1966.place(relx=0.42, rely=0.20, relwidth=0.16, relheight=0.17)


    # 1970 - MÈXICO
        self.mexico_70 = base64.b64decode(self.mexico_1970)
        self.bt_1970 = PIL.Image.open(io.BytesIO(self.mexico_70))
        self.bt_1970 = self.bt_1970.resize((72, 89))
        self.bt_1970 = ImageTk.PhotoImage(self.bt_1970)

        self.botao_img1970 = Button(self.frame_2_main, image=self.bt_1970,
                                    text='Copa de 1970\nMéxico'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1970.place(relx=0.62, rely=0.20, relwidth=0.16, relheight=0.17)


    # 1974 - ALEMANHA OCIDENTAL
        self.alemanha_O_1974 = base64.b64decode(self.alemanha_O_1974)
        self.bt_1974 = PIL.Image.open(io.BytesIO(self.alemanha_O_1974))
        self.bt_1974 = self.bt_1974.resize((72, 89))
        self.bt_1974 = ImageTk.PhotoImage(self.bt_1974)

        self.botao_img1970 = Button(self.frame_2_main, image=self.bt_1974,
                                    text='Copa de 1974\nAlemanha'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1970.place(relx=0.82, rely=0.20, relwidth=0.16, relheight=0.17)
        
        
    # 1978 - ARGENTINA
        self.argentina_1978 = base64.b64decode(self.argentina_1978)
        self.bt_1978 = PIL.Image.open(io.BytesIO(self.argentina_1978))
        self.bt_1978 = self.bt_1978.resize((72, 89))
        self.bt_1978 = ImageTk.PhotoImage(self.bt_1978)

        self.botao_img1970 = Button(self.frame_2_main, image=self.bt_1978,
                                    text='Copa de 1978\nArgentina'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1970.place(relx=0.02, rely=0.38, relwidth=0.16, relheight=0.17)   


    # 1982 - ESPANHA
        self.espanha_1982 = base64.b64decode(self.espanha_1982)
        self.bt_1982 = PIL.Image.open(io.BytesIO(self.espanha_1982))
        self.bt_1982 = self.bt_1982.resize((72, 89))
        self.bt_1982 = ImageTk.PhotoImage(self.bt_1982)

        self.botao_img1982 = Button(self.frame_2_main, image=self.bt_1982,
                                    text='Copa de 1982\nEspanha'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1982.place(relx=0.22, rely=0.38, relwidth=0.16, relheight=0.17)  
        
    # 1986 - MÉXICO
        self.mexico_1986 = base64.b64decode(self.mexico_1986)
        self.bt_1986 = PIL.Image.open(io.BytesIO(self.mexico_1986))
        self.bt_1986 = self.bt_1986.resize((72, 89))
        self.bt_1986 = ImageTk.PhotoImage(self.bt_1986)

        self.botao_img1986 = Button(self.frame_2_main, image=self.bt_1986,
                                    text='Copa de 1986\nMéxico'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1986.place(relx=0.42, rely=0.38, relwidth=0.16, relheight=0.17)  
        
    # 1990 - ITÁLIA
        self.italia_1990 = base64.b64decode(self.italia_1990)
        self.bt_1990 = PIL.Image.open(io.BytesIO(self.italia_1990))
        self.bt_1990 = self.bt_1990.resize((72, 89))
        self.bt_1990 = ImageTk.PhotoImage(self.bt_1990)

        self.botao_img1990 = Button(self.frame_2_main, image=self.bt_1990,
                                    text='Copa de 1990\nItália'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1990.place(relx=0.62, rely=0.38, relwidth=0.16, relheight=0.17) 
        
    # 1994 - ESTADOS UNIDOS
        self.usa_1994 = base64.b64decode(self.usa_1994)
        self.bt_1994 = PIL.Image.open(io.BytesIO(self.usa_1994))
        self.bt_1994 = self.bt_1994.resize((72, 89))
        self.bt_1994 = ImageTk.PhotoImage(self.bt_1994)

        self.botao_img1994 = Button(self.frame_2_main, image=self.bt_1994,
                                    text='Copa de 1994\nU.S.A.'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1994.place(relx=0.82, rely=0.38, relwidth=0.16, relheight=0.17) 
        
    # 1998 - FRANÇA
        self.franca_1998 = base64.b64decode(self.franca_1998)
        self.bt_1998 = PIL.Image.open(io.BytesIO(self.franca_1998))
        self.bt_1998 = self.bt_1998.resize((72, 89))
        self.bt_1998 = ImageTk.PhotoImage(self.bt_1998)

        self.botao_img1998 = Button(self.frame_2_main, image=self.bt_1998,
                                    text='Copa de 1998\nFrança'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img1998.place(relx=0.02, rely=0.56, relwidth=0.16, relheight=0.17) 

    # 2002 - COREIA - JAPÃO
        self.coreia_japao_2002 = base64.b64decode(self.coreia_japao_2002)
        self.bt_2002 = PIL.Image.open(io.BytesIO(self.coreia_japao_2002))
        self.bt_2002 = self.bt_2002.resize((72, 89))
        self.bt_2002 = ImageTk.PhotoImage(self.bt_2002)

        self.botao_img2002 = Button(self.frame_2_main, image=self.bt_2002,
                                    text='Copa de 2002\nCoreia Japão'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img2002.place(relx=0.22, rely=0.56, relwidth=0.16, relheight=0.17) 
        
    # 2006 - ALEMANHA
        self.alemanha_2006 = base64.b64decode(self.alemanha_2006)
        self.bt_2006 = PIL.Image.open(io.BytesIO(self.alemanha_2006))
        self.bt_2006 = self.bt_2006.resize((72, 89))
        self.bt_2006 = ImageTk.PhotoImage(self.bt_2006)

        self.botao_img2006 = Button(self.frame_2_main, image=self.bt_2006,
                                    text='Copa de 2006\nAlemanha'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img2006.place(relx=0.42, rely=0.56, relwidth=0.16, relheight=0.17) 
        
    # 2010 - AFRICA DO SUL
        self.africa_sul_2010 = base64.b64decode(self.africa_sul_2010)
        self.bt_2010 = PIL.Image.open(io.BytesIO(self.africa_sul_2010))
        self.bt_2010 = self.bt_2010.resize((72, 89))
        self.bt_2010 = ImageTk.PhotoImage(self.bt_2010)

        self.botao_img2010 = Button(self.frame_2_main, image=self.bt_2010,
                                    text='Copa de 2010\nAfrica do Sul'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img2010.place(relx=0.62, rely=0.56, relwidth=0.16, relheight=0.17) 

    # 2014 - BRASIL
        self.brasil_2014 = base64.b64decode(self.brasil_2014)
        self.bt_2014 = PIL.Image.open(io.BytesIO(self.brasil_2014))
        self.bt_2014 = self.bt_2014.resize((72, 89))
        self.bt_2014 = ImageTk.PhotoImage(self.bt_2014)

        self.botao_img2014 = Button(self.frame_2_main, image=self.bt_2014,
                                    text='Copa de 2014\nBrasil'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img2014.place(relx=0.82, rely=0.56, relwidth=0.16, relheight=0.17) 
        
    # 2018 - RUSSIA
        self.russia_2018 = base64.b64decode(self.russia_2018)
        self.bt_2018 = PIL.Image.open(io.BytesIO(self.russia_2018))
        self.bt_2018 = self.bt_2018.resize((72, 89))
        self.bt_2018 = ImageTk.PhotoImage(self.bt_2018)

        self.botao_img2018 = Button(self.frame_2_main, image=self.bt_2018,
                                    text='Copa de 2018\nRussia'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img2018.place(relx=0.02, rely=0.74, relwidth=0.16, relheight=0.17)
        
    # 2022 - QATAR
        self.qatar_2022 = base64.b64decode(self.qatar_2022)
        self.bt_2022 = PIL.Image.open(io.BytesIO(self.qatar_2022))
        self.bt_2022 = self.bt_2022.resize((72, 89))
        self.bt_2022 = ImageTk.PhotoImage(self.bt_2022)

        self.botao_img2022 = Button(self.frame_2_main, image=self.bt_2022,
                                    text='Copa de 2022\nQatar'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=CENTER)
        self.botao_img2022.place(relx=0.22, rely=0.74, relwidth=0.16, relheight=0.17)




Application()