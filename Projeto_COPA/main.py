
#from cgitb import text
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
import customtkinter

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
        
    # Funcão imagem do MAIN
        
    def gerar_widget_copa(self,img,janela,nome,x,y,w,h):
        
        self.img_widget_copa = base64.b64decode(img)
        self.bt_img_widget_copa = PIL.Image.open(io.BytesIO(self.img_widget_copa))
        self.bt_img_widget_copa = self.bt_img_widget_copa.resize((70, 86))
        self.bt_img_widget_copa = ImageTk.PhotoImage(self.bt_img_widget_copa)

        self.botao_imgcopa = customtkinter.CTkButton(
                                    self.frame_2_main,  
                                    image=self.bt_img_widget_copa,
                                    command=janela,
                                    text=nome.upper(), 
                                    text_font=('Arial 7 bold'),
                                    width=900, 
                                    compound=BOTTOM, 
                                    relief=RAISED, 
                                    text_color="white",
                                    hover= True,
                                    hover_color= "#09c184",
                                    border_width=2,
                                    corner_radius=8,
                                    border_color= "#f8ca00",
                                    fg_color= "#0c5149"
                                    ).place(relx=x, rely=y, relwidth=w, relheight=h)
        return self.botao_imgcopa    
    
    def tela(self):
        self.root.title('Copa do Mundo')
        self.root.geometry('1200x1000+10+10')
        self.root.configure(background='white')

    def frames_main(self):
        self.frame_1_main = customtkinter.CTkFrame(self.root,
                                    border_width=2,
                                    corner_radius=20,
                                    border_color= "black",
                                    bg_color="white",
                                    fg_color= "white")
        self.frame_1_main.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.20)
        
        self.frame_2_main = customtkinter.CTkFrame(self.root,      
                                    border_width=2,
                                    corner_radius=20,
                                    border_color= "black",
                                    bg_color="white",
                                    fg_color= "#0c5149")
        self.frame_2_main.place(relx=0.01,rely=0.22,relwidth=0.57,relheight=0.77)

        self.frame_3_main = customtkinter.CTkFrame(self.root,
                                    border_width=2,
                                    corner_radius=20,
                                    border_color= "black",
                                    bg_color="white",
                                    fg_color= "#0c5149")
        self.frame_3_main.place(relx=0.59,rely=0.22,relwidth=0.40,relheight=0.77)

    # Imagem da Label do Título
        self.stadio = base64.b64decode(self.stadio_B64)
        self.lb_titulo = PIL.Image.open(io.BytesIO(self.stadio))
        self.lb_titulo = self.lb_titulo.resize((1900, 200))
        self.lb_titulo = ImageTk.PhotoImage(self.lb_titulo)

        self.label_titulo = customtkinter.CTkLabel(self.frame_1_main, 
                                  image=self.lb_titulo,
                                  text='copa do mundo'.upper(), 
                                  width=900,
                                  compound=CENTER, 
                                  relief=RAISED, 
                                  #anchor=CENTER,
                                  text_font='verdana 70 bold', 
                                  fg='#cfd5e1',
                                  text_color='lightgray'
                                  )
        self.label_titulo.place(relx=0, rely=0, relwidth=1, relheight=1)

 # Botoes Label e Entry
    def widgats_principal(self):

    # LABEL TAÇA
        self.label_taca = customtkinter.CTkLabel(self.frame_3_main, 
                                text=' " A TAÇA do mundo é Nossa, \ncom o brasileiro não há quem possa..."\n\n Essa foi uma das canções \nque ecoavam durante as copas \n que se seguiram ao longo dos anos...'.upper(), 
                                text_font=('Arial 12 bold'), 
                                text_color='black',
                                bg='lightblue',
                                fg='black',
                                corner_radius=20,
                                fg_color= "lightgray"
                                )
                                
        self.label_taca.place(relx=0.01, rely=0.68, relwidth=0.98, relheight=0.30)
        
    # TROFEU JULES RIMET
        self.taca= base64.b64decode(self.taca_jules_rimet)
        self.bt_taca_dividida = PIL.Image.open(io.BytesIO(self.taca))
        self.bt_taca_dividida = self.bt_taca_dividida.resize((200, 450))
        self.bt_taca_dividida= ImageTk.PhotoImage(self.bt_taca_dividida)

        self.botao_taca =customtkinter.CTkButton(self.frame_3_main,
                            image=self.bt_taca_dividida,
                            text_font=('Arial 10 bold'),
                            text='Trofeu Jules Rimet\nde 1930 a 1970',
                            width=900,
                            compound=TOP,
                            relief=RAISED,
                            #anchor=CENTER,
                            hover= True,
                            hover_color= "lightgreen",

                            corner_radius=20,
                            text_color='black',
                            
                            fg_color= "white"
                            )
        self.botao_taca.place(relx=0.01,rely=0.01,relwidth=0.47,relheight=0.65)
        
    # TAÇA FIFA
        self.taca= base64.b64decode(self.taca_fifa)
        self.bt_taca_dividida = PIL.Image.open(io.BytesIO(self.taca))
        self.bt_taca_dividida = self.bt_taca_dividida.resize((430, 400))
        self.bt_taca_dividida= ImageTk.PhotoImage(self.bt_taca_dividida)

        self.botao_taca =customtkinter.CTkButton(self.frame_3_main,
                            image=self.bt_taca_dividida,
                            text_font=('Arial 10 bold'),
                            text='Troféu da Copa do Mundo\nde 1974 até os dias atuais',
                            width=900,
                            compound=TOP,
                            relief=RAISED,
                            #anchor=CENTER,
                            hover= True,
                            hover_color= "lightgreen",
                            corner_radius=20,
                            text_color='black',
                            fg_color= "white"
                            )
        self.botao_taca.place(relx=0.52,rely=0.01,relwidth=0.47,relheight=0.65)
   
    # 1930 - URUGUAI
        self.botao_img_Uruguai_1930 = self.gerar_widget_copa(self.uruguai_1930,self.janela_1930,'copa de 1930\nUruguai',0.02,0.02,0.12,0.23)
           
    # 1934 - ITÁLIA
        self.botao_img_Italia_1934 = self.gerar_widget_copa(self.italia_1934,self.janela_1930,'copa de 1934\nItália',0.16,0.02,0.12,0.23)
        
    # 1938 - FRANÇA
        self.botao_img_Franca_1938 = self.gerar_widget_copa(self.franca_1938,self.janela_1930,'copa de 1938\nFrança',0.30,0.02,0.12,0.23)
        
    # 1950 - BRASIL
        self.botao_img_Brasil_1950 = self.gerar_widget_copa(self.brasil_1950,self.janela_1930,'copa de 1950\nBrasil',0.44,0.02,0.12,0.23)    
       
    # 1954 - SUIÇA
        self.botao_img_Suica_1954 = self.gerar_widget_copa(self.suica_1954,self.janela_1930,'copa de 1954\nSuiça',0.58,0.02,0.12,0.23)
        
    # 1958 - SUÉCIA
        self.botao_img_Suecia_1958 = self.gerar_widget_copa(self.suecia_1958,self.janela_1930,'copa de 1958\nSuécia',0.72,0.02,0.12,0.23)
        
    # 1962 - CHILE
        self.botao_img_Chile_1962 = self.gerar_widget_copa(self.chile_1962,self.janela_1930,'copa de 1962\nChile',0.86,0.02,0.12,0.23)
    
    # 1966 - INGLATERRA
        self.botao_img_Inglaterra_1966 = self.gerar_widget_copa(self.inglaterra_1966,self.janela_1930,'copa de 1966\nInglaterra',0.02,0.26,0.12,0.23)
        
    # 1970 - MÈXICO
        self.botao_img_Mexico_1970 = self.gerar_widget_copa(self.mexico_1970,self.janela_1930,'copa de 1970\nMéxico',0.16,0.26,0.12,0.23)
        
    # 1974 - ALEMANHA OCIDENTAL
        self.botao_img_Alemanha_O_1974 = self.gerar_widget_copa(self.alemanha_O_1974,self.janela_1930,'copa de 1974\nAlemanha O',0.30,0.26,0.12,0.23)
        
    # 1978 - ARGENTINA
        self.botao_img_Argentina_1978 = self.gerar_widget_copa(self.argentina_1978,self.janela_1930,'copa de 1978\nArgentina',0.44,0.26,0.12,0.23)
    
    # 1982 - ESPANHA
        self.botao_img_Espanha_1982 = self.gerar_widget_copa(self.espanha_1982,self.janela_1930,'copa de 1982\nEspanha',0.58,0.26,0.12,0.23)
        
    # 1986 - MÉXICO
        self.botao_img_Mexico_1986 = self.gerar_widget_copa(self.mexico_1986,self.janela_1930,'copa de 1986\nMéxico',0.72,0.26,0.12,0.23)
        
    # 1990 - ITÁLIA
        self.botao_img_Italia_1990 = self.gerar_widget_copa(self.italia_1990,self.janela_1930,'copa de 1990\nItália',0.86,0.26,0.12,0.23)
        
    # 1994 - ESTADOS UNIDOS
        self.botao_img_USA_1994 = self.gerar_widget_copa(self.usa_1994,self.janela_1930,'copa de 1994\nU.S.A',0.02,0.50,0.12,0.23)
        
    # 1998 - FRANÇA
        self.botao_img_Fraca_1998 = self.gerar_widget_copa(self.franca_1998,self.janela_1930,'copa de 1998\nFrança',0.16,0.50,0.12,0.23)
        
    # 2002 - COREIA - JAPÃO
        self.botao_img_Coreia_japao_2002 = self.gerar_widget_copa(self.coreia_japao_2002,self.janela_1930,'copa de 2002\nCoreia -Japão',0.30,0.50,0.12,0.23)
        
    # 2006 - ALEMANHA
        self.botao_img_Alemanha_2006 = self.gerar_widget_copa(self.alemanha_2006,self.janela_1930,'copa de 2006\nAlemanha',0.44,0.50,0.12,0.23)
        
    # 2010 - AFRICA DO SUL
        self.botao_img_Africa_Sul_2010 = self.gerar_widget_copa(self.africa_sul_2010,self.janela_1930,'copa de 2010\nAfrica do Sul',0.58,0.50,0.12,0.23)
        
    # 2014 - BRASIL
        self.botao_img_Brasil_2014 = self.gerar_widget_copa(self.brasil_2014,self.janela_1930,'copa de 2014\nBrasil',0.72,0.50,0.12,0.23)
        
    # 2018 - RUSSIA
        self.botao_img_Russia_2018 = self.gerar_widget_copa(self.russia_2018,self.janela_1930,'copa de 2018\nRussia',0.86,0.50,0.12,0.23)
        
    # 2022 - QATAR
        self.botao_img_Qatar_2022 = self.gerar_widget_copa(self.qatar_2022,self.janela_1930,'copa de 2022\Qatar',0.02,0.74,0.12,0.23)
        
Application()