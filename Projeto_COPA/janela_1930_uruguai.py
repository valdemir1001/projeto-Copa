
from tkinter import *
from tkinter import ttk
import base64
from base64 import *
import PIL
from PIL import Image,ImageTk
import io
from img_B64 import *


class Janela_1930():
         
    # Janela 1930
    def janela_1930(self):
        self.root_1930 = Toplevel()
        self.root_1930.title('1930 - Uruguai')
        self.root_1930.configure(background='lightblue')
        self.root_1930.geometry('1200x1000+10+10')
        self.root_1930.resizable(False,False)
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
        self.lb_selo = self.lb_selo.resize((1200, 200))
        self.lb_selo = ImageTk.PhotoImage(self.lb_selo)

        self.label_selo = Label(self.frame_1_1930, image=self.lb_selo,
                                  text='uruguai 1930'.upper(), width=900,
                                  compound=CENTER, relief=RAISED, anchor=NW,
                                  font=('verdana 70 bold'), fg='black')
        self.label_selo.place(relx=0, rely=0, relwidth=1, relheight=1)
        
    def widget_1930(self):
        """self.label_pesquisa = Label(self.frame_2_1930, text='    pesquise aqui pelo ano e país'.upper(), font=('verdana 12 bold'), bg='lightblue')
        self.label_pesquisa.place(relx=0.01, rely=0.02, relwidth=0.50, relheight=0.03)

        self.label_ano = Label(self.frame_2_1930,text='ano'.upper(),font=('verdana 12 bold'),bg='lightblue')
        self.label_ano.place(relx=0.01,rely=0.08,relwidth=0.10,relheight=0.03)

        self.entry_ano = ttk.Combobox(self.frame_2_1930,font=('verdana 12 bold'),values=self.ano_pais)
        self.entry_ano.set('Busque Aqui')
        self.entry_ano.place(relx=0.15,rely=0.08,relwidth=0.40,relheight=0.03)

        self.bola = base64.b64decode(self.bola_pais_B64)
        self.bt_bola_pais = PIL.Image.open(io.BytesIO(self.bola))
        self.bt_bola_pais = self.bt_bola_pais.resize((45, 45))
        self.bt_bola_pais = ImageTk.PhotoImage(self.bt_bola_pais)

        self.botao_ano = Button(self.frame_2_1930,
                            image=self.bt_bola_pais,text='pesquisar'.upper(),font=('verdana 10 bold'),
                            width=900,compound=TOP,relief=RAISED,anchor=NW)
        self.botao_ano.place(relx=0.60,rely=0.02,relwidth=0.14,relheight=0.10)"""
        
    
        self.gp_A = Button(self.frame_2_1930,text='Grupo A\n\nArgentina\nChile\nFrança\nMéxico',
                              font=('verdana 12 bold'),bg='lightblue',width=900,compound=TOP,relief=RAISED,anchor=NW)
        self.gp_A.place(relx=0.02,rely=0.05,relwidth=0.08,relheight=0.15)

Janela_1930()
