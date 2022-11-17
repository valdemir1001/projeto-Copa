
from tkinter import *
from tkinter import ttk
import base64
from base64 import *
import PIL
from PIL import Image,ImageTk
import io
from img_B64 import *
import customtkinter

class Janela_1930():
         
    # Janela 1930
    def janela_1930(self):
        self.root_1930 = Toplevel()
        self.root_1930.title('1930 - Uruguai')
        self.root_1930.configure(background='lightblue')
        self.root_1930.geometry('1500x1000+10+10')
        self.root_1930.attributes('-fullscreen')
        self.root_1930.resizable(True,True)
        self.root_1930.transient(self.root)
        self.root_1930.focus_force()
        self.root_1930.grab_set()
        self.frames_1930()
      
        self.widget_1930()
        
    def frames_1930(self):
        self.frame_1_1930 = Frame(self.root_1930)
        self.frame_1_1930.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.20)
            
        self.frame_2_1930 = Frame(self.root_1930,bg='lightgreen')
        self.frame_2_1930.place(relx=0.01,rely=0.22,relwidth=0.98,relheight=0.77)

        """self.frame_3_1930 = Frame(self.root_1930,bg='green')
        self.frame_3_1930.place(relx=0.59,rely=0.22,relwidth=0.40,relheight=0.77) """
        
        # Imagem da Label do Título
        self.selo = base64.b64decode(self.selo_uruguai_1930)
        self.lb_selo = PIL.Image.open(io.BytesIO(self.selo))
        self.lb_selo = self.lb_selo.resize((1500, 200))
        self.lb_selo = ImageTk.PhotoImage(self.lb_selo)

        self.label_selo = customtkinter.CTkLabel(self.frame_1_1930, 
                                image=self.lb_selo,
                                text='uruguai 1930'.upper(), 
                                width=900,
                                compound=CENTER, 
                                relief=RAISED, 
                                #anchor=NW,
                                text_font=('verdana 70 bold'), 
                                fg='black')
        self.label_selo.place(relx=0, rely=0, relwidth=1, relheight=1)
        
    def widget_1930(self):
        
    # Label Grupos
        self.label_grupos = customtkinter.CTkLabel(self.frame_2_1930, 
                                text='grupos'.upper(), 
                                width=900,
                                compound=CENTER, 
                                relief=RAISED, 
                                #anchor=NW,
                                text_font=('verdana 16 bold'), 
                                fg='black')
        self.label_grupos.place(relx=0, rely=0.05, relwidth=0.10, relheight=0.05)
       
    # Botão Grupo A       
        self.gp_A = customtkinter.CTkButton(self.frame_2_1930,
                            text_font=('Arial 30 bold'),
                            text='A',
                            width=900,
                            compound=CENTER,
                            relief=RAISED,
                            #anchor=CENTER,
                            hover= True,
                            hover_color= "lightgray",
                            border_width=2,
                            corner_radius=10,
                            text_color='black',
                            border_color= "red",
                            fg_color= "white"
                            )
        self.gp_A.place(relx=0.02,rely=0.10,relwidth=0.05,relheight=0.09)
        
    # Bandeira Argentina primeira do Grupo A
        self.band_argentina_30 = base64.b64decode(self.bandeira_argentina)
        self.band_argentina_1930 = PIL.Image.open(io.BytesIO(self.band_argentina_30))
        self.band_argentina_1930 = self.band_argentina_1930.resize((50,30))
        self.band_argentina_1930 = ImageTk.PhotoImage(self.band_argentina_1930)

        self.botao_band_argentina_1930 = customtkinter.CTkButton(
                                    self.frame_2_1930,  
                                    image=self.band_argentina_1930,
                                    
                                    text='argentina'.upper(), 
                                    text_font=('Arial 7 bold'),
                                    width=900, 
                                    compound=BOTTOM, 
                                    relief=RAISED, 
                                    text_color="white",
                                    hover= True,
                                    hover_color= "#09c184",
                                    border_width=2,
                                    corner_radius=8,
                                    border_color= "red",
                                    fg_color= "#0c5149"
                                    )
        self.botao_band_argentina_1930.place(relx=0.08, rely=0.10, relwidth=0.05, relheight=0.09)
        
        # Imagem da Label do Título
        self.stadio_1930 = base64.b64decode(self.campo)
        self.lb_titulo_1930 = PIL.Image.open(io.BytesIO(self.stadio_1930))
        self.lb_titulo_1930 = self.lb_titulo_1930.resize((480, 250))
        self.lb_titulo_1930 = ImageTk.PhotoImage(self.lb_titulo_1930)
        
        self.label_placar = customtkinter.CTkLabel(self.frame_2_1930, 
                                  image=self.lb_titulo_1930,
                                  text='semifinais\n argentina | 6 x 1 | u.s.a\n\niuguslavia | 1 x 6 | uruguai \n\nfinal\n  argentina | 2 x 4 | uruguai'.upper(), 
                                  width=900,
                                  compound=CENTER, 
                                  relief=RAISED, 
                                  #anchor=CENTER,
                                  text_font='arial 17 bold', 
                                  fg='#cfd5e1',
                                  text_color='black',
                                  corner_radius=2,
                                  
                                  fg_color= "lightgray"
                                  
                                  )
        self.label_placar.place(relx=0.15, rely=0.15, relwidth=0.32, relheight=0.30)
        
    # Botão Grupo B       
        self.gp_B = customtkinter.CTkButton(self.frame_2_1930,
                            text_font=('Arial 30 bold'),
                            text='B',
                            width=900,
                            compound=CENTER,
                            relief=RAISED,
                            #anchor=CENTER,
                            hover= True,
                            hover_color= "lightgray",
                            border_width=2,
                            corner_radius=10,
                            text_color='black',
                            border_color= "blue",
                            fg_color= "white"
                            )
        self.gp_B.place(relx=0.02,rely=0.20,relwidth=0.05,relheight=0.09)
        
        
    # Bandeira da Iuguslavia primeira do grupo B
        self.band_iuguslavia_30 = base64.b64decode(self.bandeira_iuguslavia)
        self.band_iuguslavia_1930 = PIL.Image.open(io.BytesIO(self.band_iuguslavia_30))
        self.band_iuguslavia_1930 = self.band_iuguslavia_1930.resize((50,30))
        self.band_iuguslavia_1930 = ImageTk.PhotoImage(self.band_iuguslavia_1930)

        self.botao_band_iuguslavia_1930 = customtkinter.CTkButton(
                                    self.frame_2_1930,  
                                    image=self.band_iuguslavia_1930,
                                    
                                    text='iuguslavia'.upper(), 
                                    text_font=('Arial 7 bold'),
                                    width=900, 
                                    compound=BOTTOM, 
                                    relief=RAISED, 
                                    text_color="white",
                                    hover= True,
                                    hover_color= "#09c184",
                                    border_width=2,
                                    corner_radius=8,
                                    border_color= "blue",
                                    fg_color= "#0c5149"
                                    )
        self.botao_band_iuguslavia_1930.place(relx=0.08, rely=0.20, relwidth=0.05, relheight=0.09)
        
 
        
    # Botão Grupo C       
        self.gp_C = customtkinter.CTkButton(self.frame_2_1930,
                            text_font=('Arial 30 bold'),
                            text='C',
                            width=900,
                            compound=CENTER,
                            relief=RAISED,
                            #anchor=CENTER,
                            hover= True,
                            hover_color= "lightgray",
                            border_width=2,
                            corner_radius=10,
                            text_color='black',
                            border_color= "green",
                            fg_color= "white"
                            )
        self.gp_C.place(relx=0.02,rely=0.30,relwidth=0.05,relheight=0.09)
        
        
    # Bandeira da Uruguai primeira do grupo C
        self.band_uruguai_30 = base64.b64decode(self.bandeira_uruguai)
        self.band_uruguai_1930 = PIL.Image.open(io.BytesIO(self.band_uruguai_30))
        self.band_uruguai_1930 = self.band_uruguai_1930.resize((50,30))
        self.band_uruguai_1930 = ImageTk.PhotoImage(self.band_uruguai_1930)

        self.botao_band_uruguai_1930 = customtkinter.CTkButton(
                                    self.frame_2_1930,  
                                    image=self.band_uruguai_1930,
                                    
                                    text='uruguai'.upper(), 
                                    text_font=('Arial 7 bold'),
                                    width=900, 
                                    compound=BOTTOM, 
                                    relief=RAISED, 
                                    text_color="white",
                                    hover= True,
                                    hover_color= "#09c184",
                                    border_width=2,
                                    corner_radius=8,
                                    border_color= "green",
                                    fg_color= "#0c5149"
                                    )
        self.botao_band_uruguai_1930.place(relx=0.08, rely=0.30, relwidth=0.05, relheight=0.09)
        
        
    # Botão Grupo D       
        self.gp_D = customtkinter.CTkButton(self.frame_2_1930,
                            text_font=('Arial 30 bold'),
                            text='D',
                            width=900,
                            compound=CENTER,
                            relief=RAISED,
                            #anchor=CENTER,
                            hover= True,
                            hover_color= "lightgray",
                            border_width=2,
                            corner_radius=10,
                            text_color='black',
                            border_color= "black",
                            fg_color= "white"
                            )
        self.gp_D.place(relx=0.02,rely=0.40,relwidth=0.05,relheight=0.09)
        
        
    # Bandeira da USA primeira do grupo D
        self.band_usa_30 = base64.b64decode(self.bandeira_usa)
        self.band_usa_1930 = PIL.Image.open(io.BytesIO(self.band_usa_30))
        self.band_usa_1930 = self.band_usa_1930.resize((50,30))
        self.band_usa_1930 = ImageTk.PhotoImage(self.band_usa_1930)

        self.botao_band_usa_1930 = customtkinter.CTkButton(
                                    self.frame_2_1930,  
                                    image=self.band_usa_1930,
                                    
                                    text='u.s.a'.upper(), 
                                    text_font=('Arial 7 bold'),
                                    width=900, 
                                    compound=BOTTOM, 
                                    relief=RAISED, 
                                    text_color="white",
                                    hover= True,
                                    hover_color= "#09c184",
                                    border_width=2,
                                    corner_radius=8,
                                    border_color= "black",
                                    fg_color= "#0c5149"
                                    )
        self.botao_band_usa_1930.place(relx=0.08, rely=0.40, relwidth=0.05, relheight=0.09)
        
    # Botão Grupo FINAL      
        self.gp_final = customtkinter.CTkButton(self.frame_2_1930,
                            text_font=('Arial 20 bold'),
                            text='FINAL',
                            width=900,
                            compound=CENTER,
                            relief=RAISED,
                            #anchor=CENTER,
                            hover= True,
                            hover_color= "lightgray",
                            border_width=2,
                            corner_radius=10,
                            text_color='black',
                            border_color= "green",
                            fg_color= "white"
                            )
        self.gp_final.place(relx=0.80,rely=0.19,relwidth=0.08,relheight=0.07)

Janela_1930()
