from Bibliotecas import *

# Para organizar os relatórios dosclientes:
class Relatorios():
# Criar o PDF:
    def printCliente(self):    
        webbrowser.open('Cliente.pdf')       # Função para abrir o navegador e abrir uma aba
# Exibir e salvar o PDF:
    def gerarRelatorio(self):
        self.c = canvas.Canvas('Cliente.pdf')
    # Comandos para alimentar o relatório em cada entrada dos clientes:
        self.codigoRel = self.codigo_entrada.get()      
        self.nomeRel = self.nome_entrada.get()
        self.telefoneRel = self.telefone_entrada.get()
        self.cidadeRel = self.cidade_entrada.get()
        
        self.c.setFont('Helvetica-Bold', 24)     # Estilo e tamanho do título do pdf
        self.c.drawString(200, 790, 'Ficha do cliente')    # Posicionamento do reportlab

        # Definindo fonte e tamanho de cada informação do cliente:
        self.c.setFont('Helvetica-Bold', 18)      
        self.c.drawString(50, 700, 'Código: ')
        self.c.drawString(50, 670, 'Telefone: ')
        self.c.drawString(50, 640, 'Cidade: ')
        self.c.drawString(50, 610, 'Nome: ')
        # Pega as informaçoes de cada input e coloca no PDF
        self.c.setFont('Helvetica', 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 670, self.nomeRel)
        self.c.drawString(150, 640, self.telefoneRel)
        self.c.drawString(150, 610, self.cidadeRel)

        # Para a criação de linhas, espaçamentos, molduras na tela (rect)
        self.c.rect(20, 550, 550, 5, fill=True, stroke=False)     # (x, y, w, h)
             # Se for "False" e "True", então o fundo será transparente, podendo ser feito moldura
        
        self.c.showPage()
        self.c.save()
        self.printCliente()    # Chama a função novamente para rodar o código
