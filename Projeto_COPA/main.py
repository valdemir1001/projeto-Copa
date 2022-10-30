
from tkinter import ttk
from PIL import Image,ImageTk
import PIL  #pillow
import io
import base64
from tkinter import *
from img_B64 import *

root = Tk()

class Application(Imagens):
    def __init__(self,master=None):
        self.root = root
        self.img_64()
        self.tela()
        self.frames_main()
        self.widgats_principal()
    
        root.mainloop()

    def tela(self):
        self.root.title('Copa do Mundo')
        self.root.geometry('1200x1000+10+10')

    def frames_main(self):
        self.frame_1_main = Frame(self.root)
        self.frame_1_main.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.20)

        self.frame_2_main = Frame(self.root,bg='blue')
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

        self.label_pesquisa = Label(self.frame_2_main, text='    pesquise aqui pelo ano e país'.upper(), font=('verdana 12 bold'), bg='lightblue')
        self.label_pesquisa.place(relx=0.01, rely=0.02, relwidth=0.50, relheight=0.03)

        self.label_ano = Label(self.frame_2_main,text='ano'.upper(),font=('verdana 12 bold'),bg='lightblue')
        self.label_ano.place(relx=0.01,rely=0.08,relwidth=0.10,relheight=0.03)

        self.entry_ano = ttk.Combobox(self.frame_2_main,font=('verdana 12 bold'))
        self.entry_ano.place(relx=0.15,rely=0.08,relwidth=0.40,relheight=0.03)


        self.bola = base64.b64decode(self.bola_pais_B64)
        self.bt_bola_pais = PIL.Image.open(io.BytesIO(self.bola))
        self.bt_bola_pais = self.bt_bola_pais.resize((45, 45))
        self.bt_bola_pais = ImageTk.PhotoImage(self.bt_bola_pais)

        self.botao_ano = Button(self.frame_2_main,
                            image=self.bt_bola_pais,text='pesquisar'.upper(),font=('verdana 10 bold'),
                            width=900,compound=TOP,relief=RAISED,anchor=NW)
        self.botao_ano.place(relx=0.60,rely=0.02,relwidth=0.14,relheight=0.10)


    # 1930 - URUGUAI
        self.uruguai_30 = base64.b64decode(self.uruguai_1930)
        self.bt_1930 = PIL.Image.open(io.BytesIO(self.uruguai_30))
        self.bt_1930 = self.bt_1930.resize((72, 89))
        self.bt_1930 = ImageTk.PhotoImage(self.bt_1930)

        self.botao_img1930 = Button(self.frame_2_main, image=self.bt_1930,
                                    text=' 1930'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1930.place(relx=0.02, rely=0.20, relwidth=0.12, relheight=0.15)


    # 1934 - ITÁLIA
        self.italia_34 = base64.b64decode(self.italia_1934)
        self.bt_1934 = PIL.Image.open(io.BytesIO(self.italia_34))
        self.bt_1934 = self.bt_1934.resize((72, 89))
        self.bt_1934 = ImageTk.PhotoImage(self.bt_1934)

        self.botao_img1934 = Button(self.frame_2_main, image=self.bt_1934,
                                    text=' 1934'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1934.place(relx=0.16, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1938 - FRANÇA
        self.franca_38 = base64.b64decode(self.franca_1938)
        self.bt_1938 = PIL.Image.open(io.BytesIO(self.franca_38))
        self.bt_1938 = self.bt_1938.resize((72, 89))
        self.bt_1938 = ImageTk.PhotoImage(self.bt_1938)

        self.botao_img1938 = Button(self.frame_2_main, image=self.bt_1938,
                                    text=' 1938'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1938.place(relx=0.30, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1950 - BRASIL
        self.brasil_50 = base64.b64decode(self.brasil_1950)
        self.bt_1950 = PIL.Image.open(io.BytesIO(self.brasil_50))
        self.bt_1950 = self.bt_1950.resize((72, 89))
        self.bt_1950 = ImageTk.PhotoImage(self.bt_1950)

        self.botao_img1950 = Button(self.frame_2_main, image=self.bt_1950,
                                    text=' 1950'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1950.place(relx=0.44, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1954 - SUIÇA
        self.suica_54 = base64.b64decode(self.suica_1954)
        self.bt_1954 = PIL.Image.open(io.BytesIO(self.suica_54))
        self.bt_1954 = self.bt_1954.resize((72, 89))
        self.bt_1954 = ImageTk.PhotoImage(self.bt_1954)

        self.botao_img1954 = Button(self.frame_2_main, image=self.bt_1954,
                                    text=' 1954'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1954.place(relx=0.58, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1958 - SUÉCIA
        self.suecia_58 = base64.b64decode(self.suecia_1958)
        self.bt_1958 = PIL.Image.open(io.BytesIO(self.suecia_58))
        self.bt_1958 = self.bt_1958.resize((72, 89))
        self.bt_1958 = ImageTk.PhotoImage(self.bt_1958)

        self.botao_img1958 = Button(self.frame_2_main, image=self.bt_1958,
                                    text=' 1958'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1958.place(relx=0.72, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1962 - CHILE
        self.chile_62 = base64.b64decode(self.chile_1962)
        self.bt_1962 = PIL.Image.open(io.BytesIO(self.chile_62))
        self.bt_1962 = self.bt_1962.resize((72, 89))
        self.bt_1962 = ImageTk.PhotoImage(self.bt_1962)

        self.botao_img1962 = Button(self.frame_2_main, image=self.bt_1962,
                                    text=' 1962'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1962.place(relx=0.86, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1966 - INGLATERRA
        self.inglaterra_66 = base64.b64decode(self.inglaterra_1966)
        self.bt_1966 = PIL.Image.open(io.BytesIO(self.inglaterra_66))
        self.bt_1966 = self.bt_1966.resize((72, 89))
        self.bt_1966 = ImageTk.PhotoImage(self.bt_1966)

        self.botao_img1966 = Button(self.frame_2_main, image=self.bt_1966,
                                    text=' 1966'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1966.place(relx=0.02, rely=0.37, relwidth=0.12, relheight=0.15)


    # 1970 - MÈXICO
        self.mexico_70 = base64.b64decode(self.mexico_1970)
        self.bt_1970 = PIL.Image.open(io.BytesIO(self.mexico_70))
        self.bt_1970 = self.bt_1970.resize((72, 89))
        self.bt_1970 = ImageTk.PhotoImage(self.bt_1970)

        self.botao_img1970 = Button(self.frame_2_main, image=self.bt_1970,
                                    text=' 1970'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1970.place(relx=0.16, rely=0.37, relwidth=0.12, relheight=0.15)


    # 1974 - ALEMANHA OCIDENTAL
        self.alemanha_O_1974 = base64.b64decode(self.alemanha_O_1974)
        self.bt_1974 = PIL.Image.open(io.BytesIO(self.alemanha_O_1974))
        self.bt_1974 = self.bt_1974.resize((72, 89))
        self.bt_1974 = ImageTk.PhotoImage(self.bt_1974)

        self.botao_img1970 = Button(self.frame_2_main, image=self.bt_1974,
                                    text=' 1974'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1970.place(relx=0.30, rely=0.37, relwidth=0.12, relheight=0.15)
        
        
    # 1978 - ARGENTINA
        self.argentina_1978 = base64.b64decode(self.argentina_1978)
        self.bt_1978 = PIL.Image.open(io.BytesIO(self.argentina_1978))
        self.bt_1978 = self.bt_1978.resize((72, 89))
        self.bt_1978 = ImageTk.PhotoImage(self.bt_1978)

        self.botao_img1970 = Button(self.frame_2_main, image=self.bt_1978,
                                    text=' 1978'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1970.place(relx=0.44, rely=0.37, relwidth=0.12, relheight=0.15)   


    # 1982 - ESPANHA
        self.espanha_1982 = base64.b64decode(self.espanha_1982)
        self.bt_1982 = PIL.Image.open(io.BytesIO(self.espanha_1982))
        self.bt_1982 = self.bt_1982.resize((72, 89))
        self.bt_1982 = ImageTk.PhotoImage(self.bt_1982)

        self.botao_img1970 = Button(self.frame_2_main, image=self.bt_1982,
                                    text=' 1982'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1970.place(relx=0.58, rely=0.37, relwidth=0.12, relheight=0.15)  


Application()