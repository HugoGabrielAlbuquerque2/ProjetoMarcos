from tkinter import *
from tkinter import ttk
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import os
import webbrowser
from datetime import datetime
from datetime import date, timedelta
from tkcalendar import Calendar, DateEntry


root = Tk()
class Validadores():
    def Numeros(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 1000000000000000

class funcs():

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.Nome_entry.get()
        self.telefone = self.Tel_entry.get()
        self.quant = self.Quant_entry.get()
        self.quant1 = self.Quant_entry1.get()
        self.quant2 = self.Quant_entry2.get()
        self.quant3 = self.Quant_entry3.get()
        self.quant4 = self.Quant_entry4.get()
        self.quant5 = self.Quant_entry5.get()

        self.Valor = self.Valor_entry.get()
        self.Valor1 = self.Valor_entry1.get()
        self.Valor2 = self.Valor_entry2.get()
        self.Valor3 = self.Valor_entry3.get()
        self.Valor4 = self.Valor_entry4.get()
        self.Valor5 = self.Valor_entry5.get()

        self.Esp = self.Esp_entry.get()
        self.Esp1 = self.Esp_entry1.get()
        self.Esp2 = self.Esp_entry2.get()
        self.Esp3 = self.Esp_entry3.get()
        self.Esp4 = self.Esp_entry4.get()
        self.Esp5 = self.Esp_entry5.get()

        self.malha = self.malha_entry.get()
        self.malha1 = self.malha_entry1.get()
        self.malha2 = self.malha_entry2.get()
        self.malha3 = self.malha_entry3.get()
        self.malha4 = self.malha_entry4.get()
        self.malha5 = self.malha_entry5.get()

        self.Entr = self.Entrada.get()
        self.anotacoes =self.Notes.get()
 
        self.Dat =self.Date.get()
        self.cod2 =self.Cod2_Entry.get()

    def LimparTela(self):
        self.codigo_entry.delete(0, END)
        self.Nome_entry.delete(0, END)
        self.Tel_entry.delete(0, END)
        self.Esp_entry.delete(0, END)
        self.Esp_entry1.delete(0, END)
        self.Esp_entry2.delete(0, END)
        self.Esp_entry3.delete(0, END)
        self.Esp_entry4.delete(0, END)
        self.Esp_entry5.delete(0, END)
        self.malha_entry.delete(0, END)
        self.malha_entry1.delete(0, END)
        self.malha_entry2.delete(0, END)
        self.malha_entry3.delete(0, END)
        self.malha_entry4.delete(0, END)
        self.malha_entry5.delete(0, END)
        self.Valor_entry.delete(0, END)
        self.Valor_entry1.delete(0, END)
        self.Valor_entry2.delete(0, END)
        self.Valor_entry3.delete(0, END)
        self.Valor_entry4.delete(0, END)
        self.Valor_entry5.delete(0, END)
        self.Quant_entry.delete(0, END)
        self.Quant_entry1.delete(0, END)
        self.Quant_entry2.delete(0, END)
        self.Quant_entry3.delete(0, END)
        self.Quant_entry4.delete(0, END)
        self.Quant_entry5.delete(0, END)
        self.Date2.delete(0, END)
        self.NomeVendedor.delete(0, END)
        self.Entrada.delete(0, END)

    def LimparTela2(self):   
        self.Notes.delete(0, END)
        self.Date.delete(0, END)
        self.Cod2_Entry.delete(0, END)

    def conecta(self):
        self.conn = sqlite3.connect("Clientes.bg")
        self.cursor = self.conn.cursor()

    def desconecta(self):
        self.conn.close()
        print('Desconectando ao banco de dados')

    def montatabela(self):
        self.conecta()
        self.VariaveisPdf()
        print('Conectando ao banco de dados')
        # criação da tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                Nome_Cliente CHAR(40) NOT NULL,
                telefone INTEGER(20) , Esp CHAR(40) , Esp1 CHAR(40) , Esp2 CHAR(40) , Esp3 CHAR(40) , Esp4 CHAR(40) , Esp5 CHAR(40) ,
                                    Malha CHAR(40) , Malha1 CHAR(40) , Malha2 CHAR(40) , Malha3 CHAR(40) , Malha4 CHAR(40) , Malha5 CHAR(40) ,
                                    Valor INT , Valor1 int  , Valor2 int  , Valor3 int  , Valor4 int  , valor5 int  ,
                                    Uni int  , Uni1 int  , Uni2 int  , Uni3 int  , Uni4 int  , Uni5 int , Data1 CHAR(40) , Vendedor CHAR(40),
                                    Entre INT
                                    ); """)
        self.conn.commit()
        print("Banco de dados criado")
        self.desconecta()

    def TabelaTexto(self):
        self.conecta()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS texto(
                cod1 INTEGER PRIMARY KEY,
               Dat CHAR(40),
               Anotacoes CHAR(800));""")
        self.conn.commit()
        self.desconecta()


    def add_cliente(self):
        self.variaveis()
        self.VariaveisPdf()
        self.GerarData()
        self.conecta()
        self.cursor.execute("""
            INSERT INTO clientes (nome_cliente, Telefone, Esp, Esp1, Esp2, Esp3, Esp4, Esp5,
                                    Malha, Malha1, Malha2, Malha3, Malha4, Malha5,
                                    Valor, Valor1, Valor2, Valor3, Valor4, valor5,
                                    Uni, Uni1, Uni2, Uni3, Uni4, Uni5, Data1, Vendedor, Entre
                                    )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?)
        """, (self.nome, self.telefone, self.Esp, self.Esp1, self.Esp2, self.Esp3, self.Esp4, self.Esp5,
              self.malha, self.malha1, self.malha2, self.malha3, self.malha4, self.malha5,
              self.Valor, self.Valor1, self.Valor2, self.Valor3, self.Valor4, self.Valor5,
              self.quant, self.quant1, self.quant2, self.quant3, self.quant4, self.quant5, self.Datent2, self.Vendedor, self.Entr
              ))
        self.conn.commit()
        self.desconecta()
        self.select()
        self.LimparTela()

    def Add_texto(self):
        self.conecta()
        self.variaveis()
        self.cursor.execute("""
            INSERT INTO texto(Dat, Anotacoes) VALUES (?,?)""", (self.Dat, self.anotacoes))
        self.conn.commit()
        self.desconecta()
        self.select2()
        self.LimparTela2()
            
    def select2 (self):
        self.listcli2.delete(*self.listcli2.get_children())
        self.conecta()
        lista = self.cursor.execute("""
            SELECT cod1, Dat, Anotacoes
            FROM texto
            ORDER BY Dat ASC; 
        """)
        for i in lista:
            self.listcli2.insert("", END, values=i)
        self.desconecta()

    def doubleclic2(self, event):
        self.LimparTela2()
        self.listcli2.selection()
        for n in self.listcli2.selection():
            col1,col2,col3 = self.listcli2.item(
                n, 'values')
            self.Cod2_Entry.insert(END, col1)
            self.Date.insert(END, col2)
            self.Notes.insert(END, col3)
                      
    def select(self):
        self.listcli.delete(*self.listcli.get_children())
        self.conecta()
        lista = self.cursor.execute("""
            SELECT cod, nome_cliente, telefone, Esp, Esp1, Esp2, Esp3, Esp4, Esp5,
            Malha, Malha1, Malha2, Malha3, Malha4, Malha5,
            Valor, Valor1, Valor2, Valor3, Valor4, valor5, 
            Uni, Uni1, Uni2, Uni3, Uni4, Uni5, Data1, Vendedor, Entre FROM clientes
            ORDER BY nome_cliente ASC; 
        """)
        for i in lista:
            self.listcli.insert("", END, values=i)
        self.desconecta()

    def doubleclic(self, event):
        self.LimparTela()
        self.listcli.selection()
        for n in self.listcli.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20, col21, col22, col23, col24, col25, col26, col27, col28, col29,col30 = self.listcli.item(
                n, 'values')
            self.codigo_entry.insert(END, col1)
            self.Nome_entry.insert(END, col2)
            self.Tel_entry.insert(END, col3)
            self.Esp_entry.insert(END, col4)
            self.Esp_entry1.insert(END, col5)
            self.Esp_entry2.insert(END, col6)
            self.Esp_entry3.insert(END, col7)
            self.Esp_entry4.insert(END, col8)
            self.Esp_entry5.insert(END, col9)
            self.malha_entry.insert(END, col10)
            self.malha_entry1.insert(END, col11)
            self.malha_entry2.insert(END, col12)
            self.malha_entry3.insert(END, col13)
            self.malha_entry4.insert(END, col14)
            self.malha_entry5.insert(END, col15)
            self.Valor_entry.insert(END, col16)
            self.Valor_entry1.insert(END, col17)
            self.Valor_entry2.insert(END, col18)
            self.Valor_entry3.insert(END, col19)
            self.Valor_entry4.insert(END, col20)
            self.Valor_entry5.insert(END, col21)
            self.Quant_entry.insert(END, col22)
            self.Quant_entry1.insert(END, col23)
            self.Quant_entry2.insert(END, col24)
            self.Quant_entry3.insert(END, col25)
            self.Quant_entry4.insert(END, col26)
            self.Quant_entry5.insert(END, col27)
            self.Date2.insert(END, col28)
            self.NomeVendedor.insert(END, col29)
            self.Entrada.insert(END,col30)

    def Deleta(self):
        self.variaveis()
        self.conecta()
        self.cursor.execute("""
       DELETE FROM clientes WHERE cod = ?
       """, (self.codigo))
        self.conn.commit()

        self.desconecta()
        self.LimparTela()
        self.select()

    def Deleta2(self):
        self.variaveis()
        self.conecta()
        self.cursor.execute("""
       DELETE FROM texto WHERE cod1 = ?
       """, (self.cod2))
        self.conn.commit()
        self.desconecta()
        self.LimparTela2()
        self.select2()

    def alterar(self):
        self.VariaveisPdf()
        self.GerarData()
        self.variaveis()
        self.conecta()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente
            = ?, telefone = ?, Esp = ?, Esp1 = ?, Esp2 = ?, Esp3 = ?, Esp4 = ?, Esp5 = ?,
            Malha = ?, Malha1 = ?, Malha2 = ?, Malha3 = ?, Malha4 = ?, Malha5 = ?,
            Valor = ?, Valor1 = ?, Valor2 = ?, Valor3 = ?, Valor4 = ?, valor5 = ?, 
            Uni = ?, Uni1 = ?, Uni2 = ?, Uni3 = ?, Uni4 = ?, Uni5 =?, Data1 = ?, Vendedor = ?, Entre = ? WHERE cod = ?
            """, (self.nome, self.telefone, self.Esp, self.Esp1, self.Esp2, self.Esp3, self.Esp4, self.Esp5,
                  self.malha, self.malha1, self.malha2, self.malha3, self.malha4, self.malha5,
                  self.Valor, self.Valor1, self.Valor2, self.Valor3, self.Valor4, self.Valor5,
                  self.quant, self.quant1, self.quant2, self.quant3, self.quant4, self.quant5,self.Datent2, self.Vendedor,self.Entr, self.codigo))

        self.conn.commit()
        self.desconecta()
        self.select()
        self.LimparTela()

    def Busca(self):

        self.conecta()
        self.listcli.delete(*self.listcli.get_children())
        self.Nome_entry.insert(END, '%')
        nome = self.Nome_entry.get()
        self.cursor.execute("""
        SELECT cod, nome_cliente, Telefone, Esp, Esp1, Esp2, Esp3, Esp4, Esp5,
                                    Malha, Malha1, Malha2, Malha3, Malha4, Malha5,
                                    Valor, Valor1, Valor2, Valor3, Valor4, valor5,
                                    Uni, Uni1, Uni2, Uni3, Uni4, Uni5, Data1, Vendedor, Entre FROM clientes
        WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC
        """ % nome)
        buscanomecli = self.cursor.fetchall()
        for i in buscanomecli:
            self.listcli.insert("", END, values=i)
        self.LimparTela()
        self.desconecta()

    def orcamento(self):
        # Variaveis orçamento
        self.quant = self.Quant_entry.get()
        self.quant1 = self.Quant_entry1.get()
        self.quant2 = self.Quant_entry2.get()
        self.quant3 = self.Quant_entry3.get()
        self.quant4 = self.Quant_entry4.get()
        self.quant5 = self.Quant_entry5.get()

        self.Valor = self.Valor_entry.get()
        self.Valor1 = self.Valor_entry1.get()
        self.Valor2 = self.Valor_entry2.get()
        self.Valor3 = self.Valor_entry3.get()
        self.Valor4 = self.Valor_entry4.get()
        self.Valor5 = self.Valor_entry5.get()

        # Convertendo de str Para Float
        if self.quant == "":
            self.quant = 0
        else:
            self.quant = float(self.quant)

        if self.Valor == "":
            self.Valor = 0
        else:
            self.Valor = float(self.Valor)
        # Convertendo a primeira entry
        if self.quant1 == "":
            self.quant1 = 0
        else:
            self.quant1 = float(self.quant1)

        if self.Valor1 == "":
            self.Valor1 = 0
        else:
            self.Valor1 = float(self.Valor1)
        # Convertendo a segunda entry
        if self.quant2 == "":
            self.quant2 = 0
        else:
            self.quant2 = float(self.quant2)

        if self.Valor2 == "":
            self.Valor2 = 0
        else:
            self.Valor2 = float(self.Valor2)
        # Convertendo a terceira entry
        if self.quant3 == "":
            self.quant3 = 0
        else:
            self.quant3 = float(self.quant3)

        if self.Valor3 == "":
            self.Valor3 = 0
        else:
            self.Valor3 = float(self.Valor3)
        # Convertendo a quarta entry
        if self.quant4 == "":
            self.quant4 = 0
        else:
            self.quant4 = float(self.quant4)

        if self.Valor4 == "":
            self.Valor4 = 0
        else:
            self.Valor4 = float(self.Valor4)
        # Convertendo a quinta entry

        if self.quant5 == "":
            self.quant5 = 0
        else:
            self.quant5 = float(self.quant5)

        if self.Valor5 == "":
            self.Valor5 = 0
        else:
            self.Valor5 = float(self.Valor5)

        # Efetuando Calculos
        self.x = float(self.quant)
        self.y = float(self.Valor)

        self.tot = self.x*self.y
        self.tot = float(self.tot)

        # Calculo label 1
        self.x1 = float(self.quant1)
        self.y1 = float(self.Valor1)

        self.tot1 = self.x1*self.y1
        self.tot1 = float(self.tot1)

        # Calculo Label2
        self.x2 = float(self.quant2)
        self.y2 = float(self.Valor2)

        self.tot2 = self.x2*self.y2
        self.tot2 = float(self.tot2)

        # Calculo label 3
        self.x3 = float(self.quant3)
        self.y3 = float(self.Valor3)

        self.tot3 = self.x3*self.y3
        self.tot3 = float(self.tot3)

        # Calculo Label 4
        self.x4 = float(self.quant4)
        self.y4 = float(self.Valor4)

        self.tot4 = self.x4*self.y4
        self.tot4 = float(self.tot4)

        # Calculo Label 5
        self.x5 = float(self.quant5)
        self.y5 = float(self.Valor5)

        self.tot5 = self.x5*self.y5
        self.tot5 = float(self.tot5)

        self.Total = self.tot+self.tot1+self.tot2+self.tot3+self.tot4+self.tot5

        # deliberando labels
        self.resp["text"] = self.tot
        self.resp1["text"] = self.tot1
        self.resp2["text"] = self.tot2
        self.resp3["text"] = self.tot3
        self.resp4["text"] = self.tot4
        self.resp5["text"] = self.tot5
        self.respt["text"] = self.Total

    def TotRest(self):
        self.Entrada1 = self.Entrada.get()

        self.Total2 = self.Total

        if self.Entrada1 == "":
            self.Entrada1 = 0
        else:
            self.Entrada1 = float(self.Entrada1)

        self.resto = self.Total2-self.Entrada1
        self.Falta = self.resto
        self.resptEntrada["text"] = self.resto

    def LimpaOrçamento(self):
        self.Quant_entry.delete(0, END)
        self.Quant_entry1.delete(0, END)
        self.Quant_entry2.delete(0, END)
        self.Quant_entry3.delete(0, END)
        self.Quant_entry4.delete(0, END)
        self.Quant_entry5.delete(0, END)
        self.Valor_entry.delete(0, END)
        self.Entrada.delete(0, END)

        self.Valor_entry1.delete(0, END)
        self.Valor_entry2.delete(0, END)
        self.Valor_entry3.delete(0, END)
        self.Valor_entry4.delete(0, END)
        self.Valor_entry5.delete(0, END)

        self.Esp_entry.delete(0, END)
        self.Esp_entry1.delete(0, END)
        self.Esp_entry2.delete(0, END)
        self.Esp_entry3.delete(0, END)
        self.Esp_entry4.delete(0, END)
        self.Esp_entry5.delete(0, END)

        self.malha_entry1.delete(0, END)
        self.malha_entry.delete(0, END)
        self.malha_entry2.delete(0, END)
        self.malha_entry3.delete(0, END)
        self.malha_entry4.delete(0, END)
        self.malha_entry5.delete(0, END)

        self.resp["text"] = '0.0'
        self.resp1["text"] = '0.0'
        self.resp2["text"] = '0.0'
        self.resp3["text"] = '0.0'
        self.resp4["text"] = '0.0'
        self.resp5["text"] = '0.0'
        self.respt["text"] = '0.0'
        self.resptEntrada["text"] = "R$00.00"

    def VariaveisPdf(self):
        self.orcamento()
        self.TotRest()
        self.Entrada3 = str(self.Entrada1)
        self.res = str(self.resto)
        self.too = str(self.tot)
        self.too1 = str(self.tot1)
        self.too2 = str(self.tot2)
        self.too3 = str(self.tot3)
        self.too4 = str(self.tot4)
        self.too5 = str(self.tot5)
        self.too6 = str(self.Total)
        self.Vendedor = self.NomeVendedor.get()

    def printCliente(self):

        webbrowser.open("Orçamento.pdf")

    def GerarData(self):
        # Data de hoje
        self.Data = self.Date2.get()
        self.Data1 = self.Data
        self.data_e_hora_atuais = datetime.now()
        self.data_e_hora_em_texto = self.data_e_hora_atuais.strftime(
                "%d/%m/%Y")
        if self.Data1 == "":
            self.today_date = date.today()
            self.td = timedelta(10)
            self.Daten = self.td+self.today_date
            self.Datent = self.Daten.strftime(
                "%d/%m/%Y")
            self.Datent2 = self.Datent
        else:
            self.Datent = str(self.Date2.get())
            self.Datent2 = self.Datent

    def Gerarelatorio(self):
        # Variaveis
        self.orcamento()
        self.TotRest()
        self.VariaveisPdf()
        self.variaveis()
        self.GerarData()

        self.c = canvas.Canvas("Orçamento.pdf", pagesize=A4)
        # Linhas verticais1
        self.c.rect(75, 655, 1, 60)

        self.c.rect(197, 494, 1, 159)

        self.c.rect(327, 494, 1, 159)

        self.c.rect(410, 494, 1, 159)

        self.c.rect(485, 494, 1, 159)

        # Linhas horizontais 1
        self.c.rect(10, 720, 570, 2,)
        self.c.rect(10, 654, 570, 1, fill=True)
        self.c.rect(10, 715, 570, 1,)
        self.c.rect(10, 720, 570, 2,)

        self.c.rect(10, 700, 570, 15)
        self.c.rect(10, 685, 570, 15)
        self.c.rect(10, 670, 570, 15)
        self.c.rect(10, 655, 570, 15)
        self.c.rect(480, 700, 100, 15)
        self.c.rect(480, 685, 100, 15)

        # orçamento1
        self.c.rect(10, 635, 570, 20)
        self.c.rect(10, 615, 570, 20)
        self.c.rect(10, 595, 570, 20)
        self.c.rect(10, 575, 570, 20)
        self.c.rect(10, 555, 570, 20)
        self.c.rect(10, 535, 570, 20)
        self.c.rect(10, 515, 570, 20)
        self.c.rect(10, 495, 570, 20)
        self.c.rect(485, 475, 95, 20)
        self.c.rect(485, 455, 95, 20)
        self.c.rect(10, 470, 120, 1, fill=True)
        self.c.rect(150, 470, 120, 1, fill=True)
        # Copia
        self.c.rect(10, 440, 570, 2,)

        # Area de informações da empressa
        self.c.drawInlineImage('Logo.png', 15, 735, 160, 100)
        self.c.setFont("Helvetica-Bold", 15)
        self.c.drawString(250, 702, "Cliente")
        self.c.drawString(210, 810, "MALHARIA EXCLUSIVA DESIGN DIGITAL")
        self.c.setFont("Helvetica-Bold", 13)
        self.c.drawString(210, 790, 'CNPJ 33.130.885/0001-00')
        self.c.drawString(210, 775, "exclusiva.digital001@gmail.com //")
        self.c.drawString(420, 775, " Tel:(94) 98104-3199")
        self.c.drawString(210, 760, "Rua Betel N 123A - Jardim Marilucy")
        self.c.drawString(
            210, 745, "Prox. Ao Templo central da Assembleia de Deus")

        self.c.setFont("Helvetica-Bold", 17)
        self.c.drawString(40, 450, "Cliente")
        self.c.drawString(160, 450, self.Vendedor)
        self.c.drawString(40, 150, "Cliente")
        self.c.drawString(160, 150, self.Vendedor)
        self.c.drawString(490, 638, "Valor")
        self.c.setFont("Helvetica-Bold", 15)
        self.c.drawString(417, 477, "Entrada ")
        self.c.drawString(417, 457, "A pagar ")
        self.c.drawString(417, 497, "Subtotal")
        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(330, 637, "Valor Unitário")
        self.c.drawString(417, 637, "Quantidade")
        self.c.drawString(450, 702, "Data")
        self.c.drawString(360, 687, "Previsão de Entrega")
        self.c.setFont("Helvetica-Bold", 14)
        self.c.drawString(12, 638, "Descrição")
        self.c.drawString(200, 638, "Malha")
        self.c.setFont("Helvetica-Bold", 14)
        # $$
        self.c.drawString(488, 617, "R$")
        self.c.drawString(488, 597, "R$")
        self.c.drawString(488, 577, "R$")
        self.c.drawString(488, 557, "R$")
        self.c.drawString(488, 537, "R$")
        self.c.drawString(488, 517, "R$")
        self.c.drawString(488, 497, "R$")
        self.c.drawString(488, 477, "R$")
        self.c.drawString(488, 457, "R$")

        self.c.drawString(483, 702, self.data_e_hora_em_texto)
        self.c.drawString(483, 687, self.Datent)

        self.codigorel = self.codigo_entry.get()
        self.nomerel = self.Nome_entry.get()
        self.fonerel = self.Tel_entry.get()

        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(12, 687, "Nº Pedido: ")
        self.c.drawString(12, 672, "Nome: ")
        self.c.drawString(12, 657, "Telefone: ")

        self.c.setFont("Helvetica", 12)
        self.c.drawString(80, 687, self.codigorel)
        self.c.drawString(80, 672, self.nomerel)
        self.c.drawString(80, 657, self.fonerel)
        # Descrição
        self.c.drawString(12, 617, self.Esp)
        self.c.drawString(12, 597, self.Esp1)
        self.c.drawString(12, 577, self.Esp2)
        self.c.drawString(12, 557, self.Esp3)
        self.c.drawString(12, 537, self.Esp4)
        self.c.drawString(12, 517, self.Esp5)

        # Malha
        self.c.drawString(200, 617, self.malha)
        self.c.drawString(200, 597, self.malha1)
        self.c.drawString(200, 577, self.malha2)
        self.c.drawString(200, 557, self.malha3)
        self.c.drawString(200, 537, self.malha4)
        self.c.drawString(200, 517, self.malha5)

        # Valor Unitario
        self.c.drawString(331, 617, self.Valor)
        self.c.drawString(331, 597, self.Valor1)
        self.c.drawString(331, 577, self.Valor2)
        self.c.drawString(331, 557, self.Valor3)
        self.c.drawString(331, 537, self.Valor4)
        self.c.drawString(331, 517, self.Valor5)

        # quantidade
        self.c.drawString(418, 617, self.quant)
        self.c.drawString(418, 597, self.quant1)
        self.c.drawString(418, 577, self.quant2)
        self.c.drawString(418, 557, self.quant3)
        self.c.drawString(418, 537, self.quant4)
        self.c.drawString(418, 517, self.quant5)

        self.c.drawString(540, 617, self.too)
        self.c.drawString(540, 597, self.too1)
        self.c.drawString(540, 577, self.too2)
        self.c.drawString(540, 557, self.too3)
        self.c.drawString(540, 537, self.too4)
        self.c.drawString(540, 517, self.too5)
        self.c.drawString(540, 497, self.too6)
        self.c.drawString(540, 477, self.Entrada3)
        self.c.drawString(540, 457, self.res)
        # Copia
        self.c.rect(10, 440, 570, 2,)
        # verticais
        self.c.rect(75, 370, 1, 60)

        self.c.rect(197, 494, 1, 159)

        self.c.rect(327, 494, 1, 159)

        self.c.rect(410, 494, 1, 159)

        self.c.rect(485, 494, 1, 159)
        # Linhas horizontais 1
        self.c.rect(10, 430, 570, 1,)

        self.c.rect(10, 415, 570, 15)
        self.c.rect(10, 400, 570, 15)
        self.c.rect(10, 385, 570, 15)
        self.c.rect(10, 370, 570, 15)
        self.c.rect(480, 415, 100, 15)
        self.c.rect(480, 400, 100, 15)
        self.c.setFont("Helvetica-Bold", 15)
        self.c.drawString(250, 417, "Cliente")
        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(12, 402, "Nº Pedido: ")
        self.c.drawString(12, 387, "Nome: ")
        self.c.drawString(12, 372, "Telefone: ")
        self.c.drawString(450, 417, "Data")
        self.c.drawString(360, 402, "Previsão de Entrega")
        self.c.drawString(483, 417, self.data_e_hora_em_texto)
        self.c.drawString(483, 402, self.Datent)
        self.c.setFont("Helvetica", 12)
        self.c.drawString(80, 402, self.codigorel)
        self.c.drawString(80, 387, self.nomerel)
        self.c.drawString(80, 372, self.fonerel)

        # orçamento2
        self.c.rect(197, 210, 1, 159)

        self.c.rect(327, 210, 1, 159)

        self.c.rect(410, 210, 1, 159)

        self.c.rect(485, 210, 1, 159)
        # horizontais
        self.c.rect(10, 350, 570, 20)
        self.c.rect(10, 368, 570, 1, fill=True)
        self.c.rect(10, 330, 570, 20)
        self.c.rect(10, 310, 570, 20)
        self.c.rect(10, 290, 570, 20)
        self.c.rect(10, 270, 570, 20)
        self.c.rect(10, 250, 570, 20)
        self.c.rect(10, 230, 570, 20)
        self.c.rect(10, 210, 570, 20)
        self.c.rect(485, 190, 95, 20)
        self.c.rect(485, 170, 95, 20)
        self.c.rect(10, 170, 120, 1, fill=True)
        self.c.rect(150, 170, 120, 1, fill=True)
        self.c.setFont("Helvetica-Bold", 14)
        self.c.drawString(12, 352, "Descrição")
        self.c.drawString(200, 352, "Malha")
        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(330, 352, "Valor Unitário")
        self.c.drawString(417, 352, "Quantidade")
        self.c.setFont("Helvetica-Bold", 17)
        self.c.drawString(490, 352, "Valor")
        self.c.setFont("Helvetica-Bold", 15)
        self.c.drawString(417, 212, "Entrada ")
        self.c.drawString(417, 192, "A pagar ")
        self.c.drawString(417, 172, "Subtotal")
        # Variaveis
        # Copia
        self.c.drawString(488, 172, "R$")
        self.c.drawString(488, 332, "R$")
        self.c.drawString(488, 312, "R$")
        self.c.drawString(488, 292, "R$")
        self.c.drawString(488, 272, "R$")
        self.c.drawString(488, 252, "R$")
        self.c.drawString(488, 232, "R$")
        self.c.drawString(488, 212, "R$")
        self.c.drawString(488, 192, "R$")
        self.c.setFont("Helvetica", 12)
        self.c.drawString(12, 332, self.Esp)
        self.c.drawString(12, 312, self.Esp1)
        self.c.drawString(12, 292, self.Esp2)
        self.c.drawString(12, 272, self.Esp3)
        self.c.drawString(12, 252, self.Esp4)
        self.c.drawString(12, 232, self.Esp5)

        self.c.drawString(200, 332, self.malha)
        self.c.drawString(200, 312, self.malha1)
        self.c.drawString(200, 292, self.malha2)
        self.c.drawString(200, 272, self.malha3)
        self.c.drawString(200, 252, self.malha4)
        self.c.drawString(200, 232, self.malha5)

        self.c.drawString(331, 332, self.Valor)
        self.c.drawString(331, 312, self.Valor1)
        self.c.drawString(331, 292, self.Valor2)
        self.c.drawString(331, 272, self.Valor3)
        self.c.drawString(331, 252, self.Valor4)
        self.c.drawString(331, 232, self.Valor5)

        self.c.drawString(418, 332, self.quant)
        self.c.drawString(418, 312, self.quant1)
        self.c.drawString(418, 292, self.quant2)
        self.c.drawString(418, 272, self.quant3)
        self.c.drawString(418, 252, self.quant4)
        self.c.drawString(418, 232, self.quant5)

        self.c.drawString(540, 332, self.too)
        self.c.drawString(540, 312, self.too1)
        self.c.drawString(540, 292, self.too2)
        self.c.drawString(540, 272, self.too3)
        self.c.drawString(540, 252, self.too4)
        self.c.drawString(540, 232, self.too5)
        self.c.drawString(540, 212, self.too6)
        self.c.drawString(540, 192, self.Entrada3)
        self.c.drawString(540, 172, self.res)

        self.c.rect(28, 550, 550, 5, fill=False, stroke=False)

        # self.c.showPage()
        self.c.save()

        os.startfile("orçamento.pdf")

    def VarieaveisLo(self):
        self.Cadastro1 = self.Ent_usuario.get()
        self.Cadastro2 = self.Ent_usuario2.get()
        self.Senhac1 = self.Ent_senha2.get()
        self.Senhac2 = self.Ent_senha3.get()
        self.Senhal = self.Ent_senha.get()
        
    def Conect(self):
        self.conm = sqlite3.connect("login.db")
        self.cursor1 = self.conm.cursor()

    def Desconect(self):
        self.conm.close()
        print('Desconectando ao banco de dados')

    def Tabela(self):
        self.Conect()
        print("Conectando ao banco de senhas")
        self.cursor1.execute("CREATE TABLE IF NOT EXISTS login (nome text, senha text)")
        self.conm.commit()
        print("Banco de dados da senha criado")
        self.Desconect()

    def Cadastro(self):
        self.VarieaveisLo()
        self.Tabela()
        self.Conect()
        if self.Senhac1 == self.Senhac2:
            self.cursor1.execute("INSERT INTO login(nome, senha) VALUES(?,?)",(self.Cadastro2, self.Senhac1))
            self.aviso["text"] = "Cadastro com sucesso "  
        else:
            self.aviso["text"] = "Senhas diferentes"

        self.conm.commit()
        self.Desconect()

    def login(self):
        self.VarieaveisLo()
        self.Conect()

    def Calendario(self):
        self.Calendario1 = Calendar(self.frame4, fg="gray",bg="Blue",
            font=("verdana", '9', 'bold'), locale='pt_br')
        self.Calendario1.place(relx=0.15,rely=0.1)
        self.calDataInit = Button(self.frame4,text="Inserir Data",bd=3, bg="#F2360C", fg="#400D02",
                                font=("verdana", 9, "bold"),
            command= self.printf_cal)
        self.calDataInit.place(relx=0.30,rely=0.55,relheight=0.10,relwidth=0.15)

    def printf_cal(self):
        DataIn = self.Calendario1.get_date()
        self.Calendario1.destroy()
        self.Date.delete(0, END)
        self.Date.insert(END,DataIn)
        self.calDataInit.destroy()

    def Calendario2(self):
        self.Calendario2 = Calendar(self.frame3, fg="gray",bg="Blue",
            font=("verdana", '9', 'bold'), locale='pt_br')
        self.Calendario2.place(relx=0.15,rely=0.1)
        self.calDataInit = Button(self.frame3,text="Inserir Data",bd=3, bg="#F2360C", fg="#400D02",
                                font=("verdana", 9, "bold"),
            command= self.printf_cal2)
        self.calDataInit.place(relx=0.45,rely=0.53,relheight=0.10,relwidth=0.15)

    def printf_cal2(self):
        DataIn = self.Calendario2.get_date()
        self.Calendario2.destroy()
        self.Date2.delete(0, END)
        self.Date2.insert(END,DataIn)
        self.calDataInit.destroy()    

class Aplication(funcs, Validadores):
    def __init__(self):
        self.root = root

        self.tela()
        #self.Janela2()
        self.frames_da_tela()
        self.validenu()
        self.Botoes()
        self.orcamento()
        self.list()
        self.calendarop()
        self.montatabela()
        self.TabelaTexto()
        self.select()
        self.select2()
        self.menus()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro do Cliente")
        self.root.configure(background='#400D02')
        lado, cima = (root.winfo_screenwidth()), (root.winfo_screenheight())
        self.root.geometry('%dx%d+0+0' % (lado, cima))
        self.root.resizable(True, True,)
        self.root.minsize(width=720, height=500)

    def frames_da_tela(self):
        self.frame1 = Frame(
            self.root, bd=4, highlightbackground="#BFAC95", highlightthickness=3)
        self.frame1.place(relx=0.01, rely=0.01, relwidth=0.50, relheight=0.5)

        self.frame2 = Frame(
            self.root, bd=4, highlightbackground="#BFAC95", highlightthickness=3)
        self.frame2.place(relx=0.01, rely=0.52, relwidth=0.50, relheight=0.45)

        self.frame3 = Frame(
            self.root, bd=4, highlightbackground="#BFAC95", highlightthickness=3)
        self.frame3.place(relx=0.52, rely=0.01, relwidth=0.47, relheight=0.50)  

        self.frame4 = Frame(
            self.root, bd=4, highlightbackground="#BFAC95", highlightthickness=3)
        self.frame4.place(relx=0.52, rely=0.52, relwidth=0.47, relheight=0.45)  

    def Botoes(self):
        self.abas = ttk.Notebook(self.frame1)
        self.aba1 = Frame(self.abas)
        self.aba1.configure(background="gray")
        self.abas.add(self.aba1, text="Cadastro Cliente")
        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        self.canvas = Canvas(self.aba1, bd=0, bg="orange", highlightbackground="gray",
                             highlightthickness=3)
        self.canvas.place(relx=0.0001, rely=0.79, relwidth=0.3,
                          relheight=0.17)
        # Botão Limpar
        self.bt_limpar = Button(self.aba1, text="Limpar", bd=3, bg="#F2360C", fg="#400D02",
                                font=("verdana", 9, "bold"), command=self.LimparTela)
        self.bt_limpar.place(relx=0.001, rely=0.80,
                             relwidth=0.1, relheight=0.15)

        # Botao Buscar
        self.bt_Buscar = Button(self.aba1, text="buscar", bd=3, bg="#F2360C", fg="#400D02",
                                font=("verdana", 9, "bold"), command=self.Busca)
        self.bt_Buscar.place(relx=0.90, rely=0.01,
                             relwidth=0.1, relheight=0.15)
        # Botão Novo
        self.bt_Novo = Button(self.aba1, text="Novo", bd=3, bg="#F2360C", fg="#400D02",
                              font=("verdana", 9, "bold"), command=self.add_cliente)
        self.bt_Novo.place(relx=0.2, rely=0.80, relwidth=0.1, relheight=0.15)
        # Botão Alterar
        self.bt_Alterar = Button(self.aba1, text="Alterar", bd=3, bg="#F2360C", fg="#400D02",
                                 font=("verdana", 9, "bold"), command=self.alterar)
        self.bt_Alterar.place(relx=0.10, rely=0.80,
                              relwidth=0.1, relheight=0.15)
        # Botao Apagar
        self.bt_Apagar = Button(self.aba1, text="Apagar", bd=3, bg="#F2360C", fg="#400D02",
                                font=("verdana", 9, "bold"), command=self.Deleta)
        self.bt_Apagar.place(relx=0.90, rely=0.85,
                             relwidth=0.1, relheight=0.15)

        # criacação label
        self.Lb_codigo = Label(self.aba1, text="Código do Pedido",
                               bg="#595645", fg="white", bd=5)
        self.Lb_codigo.place(relx=0.001, rely=0.01, relwidth=0.20)

        self.codigo_entry = Entry(self.aba1, validate="key", validatecommand=self.vdm2,
                                  bd=3, bg="#BFAC95")
        self.codigo_entry.place(relx=0.001, rely=0.10, relwidth=0.10)

        self.Lb_Nome = Label(self.aba1, text="Nome",
                             bg="#595645", fg="white", bd=5)
        self.Lb_Nome.place(relx=0.001, rely=0.25, relwidth=0.20)

        self.Nome_entry = Entry(self.aba1, bd=2, bg="#BFAC95")
        self.Nome_entry.place(relx=0.001, rely=0.35, relwidth=0.50)

        self.Lb_Tel = Label(self.aba1, text="Telefone",
                            bg="#595645", fg="white", bd=5)
        self.Lb_Tel.place(relx=0.001, rely=0.50, relwidth=0.1)

        self.Tel_entry = Entry(self.aba1, validate="key",
                               validatecommand=self.vdm2, bd=2, bg="#BFAC95")
        self.Tel_entry.place(relx=0.001, rely=0.60, relwidth=0.20)

        # Criação da area do orçamento
        self.Bt_Calcular = Button(self.frame3, text="Calcular", bd=3, bg="#F2360C", fg="#400D02",
                                  font=("verdana", 9, "bold"), command=self.orcamento)
        self.Bt_Calcular.place(relx=0.66, rely=0.80,
                               relheight=0.15, relwidth=0.15)

        self.Bt_LimparOr = Button(self.frame3, text="Limpar", bd=3, bg="#F2360C", fg="#400D02",
                                  font=("verdana", 9, "bold"), command=self.LimpaOrçamento)
        self.Bt_LimparOr.place(relx=0.46, rely=0.80,
                               relheight=0.15, relwidth=0.15)

        self.Bt_Imprimir = Button(self.frame3, text="Imprimir", bd=3, bg="#F2360C", fg="#400D02",
                                  font=("verdana", 9, "bold"), command=self.Gerarelatorio)
        self.Bt_Imprimir.place(relx=0.30, rely=0.80,
                               relheight=0.15, relwidth=0.15)

        self.restentr = Button(self.frame3, text="Entrada", bd=3, bg="#F2360C", fg="#400D02",
                               font=("verdana", 9, "bold"), command=self.TotRest)
        self.restentr.place(relx=0.82, rely=0.80,
                            relheight=0.15, relwidth=0.15)

        # resposta
        self.resp = Label(self.frame3, text="00.00", bg="#595645",
                          fg="white", bd=5, font=("verdana", 12, "bold"))
        self.resp.place(relx=0.66, rely=0.10, relheight=0.08, relwidth=0.15)

        self.resp1 = Label(self.frame3, text="00.00", bg="#595645",
                           fg="white", bd=5, font=("verdana", 12, "bold"))
        self.resp1.place(relx=0.66, rely=0.20, relheight=0.08, relwidth=0.15)

        self.resp2 = Label(self.frame3, text="00.00", bg="#595645",
                           fg="white", bd=5, font=("verdana", 12, "bold"))
        self.resp2.place(relx=0.66, rely=0.30, relheight=0.08, relwidth=0.15)

        self.resp3 = Label(self.frame3, text="00.00", bg="#595645",
                           fg="white", bd=5, font=("verdana", 12, "bold"))
        self.resp3.place(relx=0.66, rely=0.40, relheight=0.08, relwidth=0.15)

        self.resp4 = Label(self.frame3, text="00.00", bg="#595645",
                           fg="white", bd=5, font=("verdana", 12, "bold"))
        self.resp4.place(relx=0.66, rely=0.50, relheight=0.08, relwidth=0.15)

        self.resp5 = Label(self.frame3, text="00.00", bg="#595645",
                           fg="white", bd=5, font=("verdana", 12, "bold"))
        self.resp5.place(relx=0.66, rely=0.60, relheight=0.08, relwidth=0.15)

        self.respt = Label(self.frame3, text="00.00", bg="#595645",
                           fg="white", bd=5, font=("verdana", 12, "bold"))
        self.respt.place(relx=0.66, rely=0.70, relheight=0.08, relwidth=0.15)

        self.resptEntrada = Label(self.frame3, text="R$00.00", bg="#595645",
                                  fg="white", bd=5, font=("verdana",12, "bold"))
        self.resptEntrada.place(relx=0.82, rely=0.70,
                                relheight=0.08, relwidth=0.15)

        # Topicos Labels
        self.Lb_Quanti = Label(self.frame3, text="Quantidade ",
                               bg="#595645", fg="white", bd=5, font=("verdana", 10, "bold"))
        self.Lb_Quanti.place(relx=0.50, rely=0.001,
                             relheight=0.08, relwidth=0.15)

        self.Lb_valor = Label(self.frame3, text="Valor ", bg="#595645",
                              fg="white", bd=5, font=("verdana", 10, "bold"))
        self.Lb_valor.place(relx=0.34, rely=0.001,
                            relheight=0.08, relwidth=0.15)

        self.Lb_espec = Label(self.frame3, text="Especificação",
                              bg="#595645", fg="white", bd=5, font=("verdana", 10, "bold"))
        self.Lb_espec.place(relx=0.02, rely=0.001,
                            relheight=0.08, relwidth=0.15)

        self.Lb_Malha = Label(self.frame3, text="Malha", bg="#595645",
                              fg="white", bd=5, font=("verdana", 10, "bold"))
        self.Lb_Malha.place(relx=0.18, rely=0.001,
                            relheight=0.08, relwidth=0.15)

        self.Lb_Total = Label(self.frame3, text="Total", bg="#595645",
                              fg="white", bd=5, font=("verdana", 10, "bold"))
        self.Lb_Total.place(relx=0.66, rely=0.001,
                            relheight=0.08, relwidth=0.15)

        # especificações Entrys
        self.Esp_entry = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.Esp_entry.place(relx=0.02, rely=0.10,
                             relheight=0.08, relwidth=0.15)
        
        self.Esp_entry1 = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.Esp_entry1.place(relx=0.02, rely=0.20,
                              relheight=0.08, relwidth=0.15)

        self.Esp_entry2 = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.Esp_entry2.place(relx=0.02, rely=0.30,
                              relheight=0.08, relwidth=0.15)

        self.Esp_entry3 = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.Esp_entry3.place(relx=0.02, rely=0.40,
                              relheight=0.08, relwidth=0.15)

        self.Esp_entry4 = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.Esp_entry4.place(relx=0.02, rely=0.50,
                              relheight=0.08, relwidth=0.15)

        self.Esp_entry5 = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.Esp_entry5.place(relx=0.02, rely=0.60,
                              relheight=0.08, relwidth=0.15)

        # Valor Entrys
        self.Valor_entry = Entry(
            self.frame3, bd=2, validate="key", validatecommand=self.vdm2, bg="#BFAC95")
        self.Valor_entry.place(relx=0.34, rely=0.10,
                               relheight=0.08, relwidth=0.15)

        self.Valor_entry1 = Entry(
            self.frame3, validate="key", validatecommand=self.vdm2, bd=2, bg="#BFAC95")
        self.Valor_entry1.place(relx=0.34, rely=0.20,
                                relheight=0.08, relwidth=0.15)

        self.Valor_entry2 = Entry(
            self.frame3, validate="key", validatecommand=self.vdm2, bd=2, bg="#BFAC95")
        self.Valor_entry2.place(relx=0.34, rely=0.30,
                                relheight=0.08, relwidth=0.15)

        self.Valor_entry3 = Entry(
            self.frame3, validate="key", validatecommand=self.vdm2, bd=2, bg="#BFAC95")
        self.Valor_entry3.place(relx=0.34, rely=0.40,
                                relheight=0.08, relwidth=0.15)

        self.Valor_entry4 = Entry(
            self.frame3, validate="key", validatecommand=self.vdm2, bd=2, bg="#BFAC95")
        self.Valor_entry4.place(relx=0.34, rely=0.50,
                                relheight=0.08, relwidth=0.15)

        self.Valor_entry5 = Entry(
            self.frame3, bd=2, validate="key", validatecommand=self.vdm2, bg="#BFAC95")
        self.Valor_entry5.place(relx=0.34, rely=0.60,
                                relheight=0.08, relwidth=0.15)

        self.Entrada = Entry(self.frame3, bd=2, validate="key",
                             validatecommand=self.vdm2, bg="#BFAC95")
        self.Entrada.place(relx=0.82, rely=0.60,
                           relheight=0.08, relwidth=0.15)

        self.Entra = Label(self.frame3, text="Entrada", bg="#595645",
                           fg="white", bd=5, font=("verdana", 10, "bold"))
        self.Entra.place(relx=0.82, rely=0.50,
                         relheight=0.08, relwidth=0.15)

        # Quantidade entrys
        self.Quant_entry = Entry(
            self.frame3, validate="key", validatecommand=self.vdm2, bd=2, bg="#BFAC95")
        self.Quant_entry.place(relx=0.50, rely=0.10,
                               relheight=0.08, relwidth=0.15)

        self.Quant_entry1 = Entry(
            self.frame3, validate="key", validatecommand=self.vdm2, bd=2, bg="#BFAC95")
        self.Quant_entry1.place(relx=0.50, rely=0.20,
                                relheight=0.08, relwidth=0.15)

        self.Quant_entry2 = Entry(
            self.frame3, validate="key", validatecommand=self.vdm2, bd=2, bg="#BFAC95")
        self.Quant_entry2.place(relx=0.50, rely=0.30,
                                relheight=0.08, relwidth=0.15)

        self.Quant_entry3 = Entry(
            self.frame3, validate="key", validatecommand=self.vdm2, bd=2, bg="#BFAC95")
        self.Quant_entry3.place(relx=0.50, rely=0.40,
                                relheight=0.08, relwidth=0.15)

        self.Quant_entry4 = Entry(
            self.frame3, bd=2, validate="key", validatecommand=self.vdm2, bg="#BFAC95")
        self.Quant_entry4.place(relx=0.50, rely=0.50,
                                relheight=0.08, relwidth=0.15)

        self.Quant_entry5 = Entry(
            self.frame3, validate="key", validatecommand=self.vdm2, bd=2, bg="#BFAC95")
        self.Quant_entry5.place(relx=0.50, rely=0.60,
                                relheight=0.08, relwidth=0.15)

        # Malha Entrys
        self.malha_entry = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.malha_entry.place(relx=0.18, rely=0.10,
                               relheight=0.08, relwidth=0.15)

        self.malha_entry1 = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.malha_entry1.place(relx=0.18, rely=0.20,
                                relheight=0.08, relwidth=0.15)

        self.malha_entry2 = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.malha_entry2.place(relx=0.18, rely=0.30,
                                relheight=0.08, relwidth=0.15)

        self.malha_entry3 = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.malha_entry3.place(relx=0.18, rely=0.40,
                                relheight=0.08, relwidth=0.15)

        self.malha_entry4 = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.malha_entry4.place(relx=0.18, rely=0.50,
                                relheight=0.08, relwidth=0.15)

        self.malha_entry5 = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.malha_entry5.place(relx=0.18, rely=0.60,
                                relheight=0.08, relwidth=0.15)

        self.Prazo = Label(self.frame3, text="Prazo de Entrega", bg="#595645",
                           fg="white", bd=5, font=("verdana", 10, "bold"))
        self.Prazo.place(relx=0.02, rely=0.70,
                         relheight=0.08, relwidth=0.20)

        self.PrazoEntrega = Button(self.frame3,text="Data", bd=3, bg="#F2360C", fg="#400D02",
                                font=("verdana", 12, "bold"), command=self.Calendario2)
        self.PrazoEntrega.place(relx=0.02, rely=0.80,
                                relheight=0.08, relwidth=0.20)

        self.Date2= Entry(self.frame3, bd=2, bg="#BFAC95")
        self.Date2.place(relx=0.02, rely=0.90, relheight=0.08, relwidth=0.20)

        self.Vendedor = Label(self.frame3, text="Vededor", bg="#595645",
                           fg="white", bd=5, font=("verdana", 12, "bold"))
        self.Vendedor.place(relx=0.82, rely=0.001, relheight=0.08, relwidth=0.15)

        self.NomeVendedor = Entry(self.frame3, bd=2, bg="#BFAC95")
        self.NomeVendedor.place(relx=0.82, rely=0.10, relheight=0.08, relwidth=0.15)

        self.In_text = Button(self.frame4,text="Inserir Anotação", bd=3, bg="#F2360C", fg="white",
                                font=("verdana", 12, "bold"),command=self.Add_texto)
        self.In_text.place(relx=0.60, rely=0.10,
                                relheight=0.05, relwidth=0.30)

    def list(self):
        self.listcli = ttk.Treeview(
            self.frame2, height=3, column=("col1", "col2", "col3"))
        self.listcli.heading("#0", text="")
        self.listcli.heading("#1", text="Codigo")
        self.listcli.heading("#2", text="Nome")
        self.listcli.heading("#3", text="Telefone")

        self.listcli.column("#0", width=1)
        self.listcli.column("#1", width=50)
        self.listcli.column("#2", width=200)
        self.listcli.column("#3", width=200)

        self.listcli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.barra = Scrollbar(self.frame2, orient="vertical")
        self.listcli.configure(yscroll=self.barra.set)
        self.barra.place(relx=0.96, rely=0.01, relwidth=0.04, relheight=0.85)
        self.listcli.bind('<Double-1>', self.doubleclic)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit(): self.root.destroy()
        menubar.add_cascade(label='Opções', menu=filemenu)
        menubar.add_cascade(label='Relatórios', menu=filemenu2)
        filemenu.add_cascade(label="Sair", command=quit)
        # filemenu2.add_cascade(label="Fazer Loguin", command=self.Janela2)
        filemenu2.add_cascade(label="Ficha Cliente",
                              command=self.Gerarelatorio)

    def Janela2(self):
        self.root2 = Toplevel()
        self.root2.title("Loguin")
        self.root2.configure(background=("#D92D07"))
        self.root2.geometry("300x400")
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

        self.framelo = Frame(
                self.root2, bd=4, highlightbackground="#400D02", highlightthickness=3)
        self.framelo.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.96)
        self.BotoesLo()

    def BotoesLo(self):
        self.abas =ttk.Notebook(self.framelo)
        self.abaslo1 =Frame(self.abas)
        self.aba2 =Frame(self.abas)
        self.abaslo1.configure(background="#BFAC95")
        self.aba2.configure(background="#BFAC95")
        self.abas.add(self.abaslo1, text="Login")
        self.abas.add(self.aba2, text="Cadastro ")
        self.abas.place(relx=0, rely=0,relwidth=0.98,relheight=0.98)

        self.tit = Label(self.abaslo1,bg='#400D02',bd=1)
        self.tit.place(relx=0.02,rely=0.15,relheight=0.02, relwidth=0.96)

        self.lb_Barra= Label(self.abaslo1,text="Login",foreground='#400D02',font=("Dotum", 20, "bold"),bd=3, bg="#BFAC95" )
        self.lb_Barra.place(relx=0.01, rely=0.30,relheight=0.10,relwidth=0.40)

        self.lb_Usuario = Label(self.abaslo1,text="Usuário *",foreground='#400D02',font=("Dotum", 14, "bold"),bd=3, bg="#BFAC95" )
        self.lb_Usuario.place(relx=0.01, rely=0.20,relheight=0.07,relwidth=0.35)

        self.Ent_usuario = Entry(self.abaslo1, bd=2, bg="#F2F2F2")
        self.Ent_usuario.place(relx=0.01,rely=0.28,relheight=0.07,relwidth=0.80)

        self.lb_senha= Label(self.abaslo1,text="Senha *",foreground='#400D02',font=("Dotum", 14, "bold"),bd=3, bg="#BFAC95" )
        self.lb_senha.place(relx=0.001, rely=0.40,relheight=0.07,relwidth=0.33)

        self.Ent_senha = Entry(self.abaslo1, bd=2, bg="#F2F2F2")
        self.Ent_senha.place(relx=0.01,rely=0.48,relheight=0.07,relwidth=0.80)

        self.bt_login = Button(self.abaslo1, text="login", bd=3, bg="#F2360C", fg="#400D02",
                                 font=("Dotum", 16, "bold"))
        self.bt_login.place(relx=0.50,rely=0.60,relheight=0.10,relwidth=0.30)
     
       

        #Botões cadastro
        self.lb_Barra2= Label(self.aba2,text="Cadastro",foreground='#400D02',font=("Dotum", 20, "bold"),bd=3, bg="#BFAC95" )
        self.lb_Barra2.place(relx=0.001, rely=0.30,relheight=0.10,relwidth=0.60)

        self.tit1 = Label(self.aba2,bg='#400D02',bd=1)
        self.tit1.place(relx=0.02,rely=0.15,relheight=0.02, relwidth=0.96)

        self.lb_Usuario2 = Label(self.aba2,text="Usuário *",foreground='#400D02',font=("Dotum", 14, "bold"),bd=3, bg="#BFAC95" )
        self.lb_Usuario2.place(relx=0.01, rely=0.20,relheight=0.07,relwidth=0.35)

        self.Ent_usuario2 = Entry(self.aba2, bd=2, bg="#F2F2F2")
        self.Ent_usuario2.place(relx=0.01,rely=0.28,relheight=0.07,relwidth=0.80)

        self.lb_senha2= Label(self.aba2,text="Senha *",foreground='#400D02',font=("Dotum", 14, "bold"),bd=3, bg="#BFAC95" )
        self.lb_senha2.place(relx=0.001, rely=0.40,relheight=0.07,relwidth=0.33)

        self.Ent_senha2 = Entry(self.aba2, bd=2, bg="#F2F2F2")
        self.Ent_senha2.place(relx=0.01,rely=0.48,relheight=0.07,relwidth=0.80)

        self.lb_senha3= Label(self.aba2,text="Confirmar Senha *",foreground='#400D02',font=("Dotum", 14, "bold"),bd=3, bg="#BFAC95" )
        self.lb_senha3.place(relx=0.001, rely=0.60,relheight=0.07,relwidth=0.68)

        self.Ent_senha3 = Entry(self.aba2, bd=2, bg="#F2F2F2")
        self.Ent_senha3.place(relx=0.01,rely=0.68,relheight=0.07,relwidth=0.80)

        self.bt_login2 = Button(self.aba2, text="Cadastro", bd=3, bg="#F2360C", fg="#400D02",
                                 font=("Dotum", 16, "bold"),command=self.Cadastro)
        self.bt_login2.place(relx=0.40,rely=0.80,relheight=0.10,relwidth=0.40)

        self.aviso= Label(self.aba2,text="",foreground='#400D02',font=("Dotum", 14, "bold"),bd=3, bg="#BFAC95")
        self.aviso.place(relx=0.001, rely=0.90,relheight=0.07,relwidth=0.90)

    def validenu(self):
        self.vdm2 = (self.root.register(self.Numeros), "%P")

    def calendarop(self):
        self.bt_date = Button(self.frame4, text="Data", bd=3, bg="#F2360C", fg="white",
                                font=("verdana", 12, "bold"), command=self.Calendario)
        self.bt_date.place(relx=0.02, rely=0.01,
                             relwidth=0.10, relheight=0.08) 

        self.Limpa2= Button(self.frame4, text="Limpa Tela", bd=3, bg="#F2360C", fg="white",
                                font=("verdana", 10, "bold"), command=self.LimparTela2)
        self.Limpa2.place(relx=0.15, rely=0.08,
                             relwidth=0.15, relheight=0.08) 

        self.Apaga= Button(self.frame4, text="Apagar", bd=3, bg="#F2360C", fg="white",
                                font=("verdana", 10, "bold"), command=self.Deleta2)
        self.Apaga.place(relx=0.30, rely=0.08,
                             relwidth=0.15, relheight=0.08) 

        self.Date = Entry(self.frame4, bd=2, bg="#BFAC95")
        self.Date.place(relx=0.02, rely=0.12, relwidth=0.10)

        self.Cod2_Entry = Entry(self.frame4, bd=2, bg="#BFAC95")
        self.Cod2_Entry.place(relx=0.14, rely=0.02, relwidth=0.05)


        self.Notes = Entry(self.frame4, bd=2, bg="#BFAC95")
        self.Notes.place(relx=0.20, rely=0.02, relwidth=0.80,relheight=0.05)

        self.listcli2 = ttk.Treeview(
        self.frame4, height=3, column=("col1", "col2","col3"))
        self.listcli2.heading("#0", text="")
        self.listcli2.heading("#1", text="cod")
        self.listcli2.heading("#2", text="Data")
        self.listcli2.heading("#3", text="Titulo")
        
        self.listcli2.column("#0", width=0)
        self.listcli2.column("#1", width=10)
        self.listcli2.column("#2", width=80)
        self.listcli2.column("#3", width=600)

        self.listcli2.place(relx=0.01, rely=0.18, relwidth=0.95, relheight=0.70)

        self.barra = Scrollbar(self.frame4, orient="vertical")
        self.listcli2.configure(yscroll=self.barra.set)
        self.barra.place(relx=0.96, rely=0.01, relwidth=0.04, relheight=0.85)
        self.listcli2.bind('<Double-1>', self.doubleclic2)





Aplication()
