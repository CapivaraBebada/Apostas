from tkinter import *
# Para criar o balão de mensagem
from tkinter import ttk     
from tkinter import tix
# Biblioteca (em SQL) para acessar o banco de dados
import sqlite3      
# Biibliotecas para imprimir a ficha dos clientes cadastrados:
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
# Para chamar o navegador padrão do computador (google) quando for abrir a ficha do cliente em PDF:
import webbrowser
# Para criar uma caixa de mensagem:
from tkinter import messagebox
# Para criar calendário
from tkcalendar import Calendar, DateEntry      ## O cálculo das datas é feito de forma automática
