# importar a Nossa biblioteca  ------------------------------------------------------------------
from tkinter import * # importar O tkinter Completo
import random # importar a Radom para Gerar sennhas aliatorias
import string # importar a Biblioteca string para Ligar a Função criar senha
from tkinter import messagebox # importar a messagebox
#------------------------------------------------------------------------------------------------
# implementar As Nossas Funçoes -----------------------------------------------------------------
# Função para Gerar Senha -----------------------------------------------------------------------
def gerar_senha():  # Vai Ligar Com O botão Gerar Front end Comand= gerar_senha 
    tamanho = int(Chars.get())  
    # Obter o número de caracteres desejado
    caracteres = string.ascii_letters + string.digits + string.punctuation  
    # Letras, dígitos e caracteres especiais
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))  
    # Gerar a senha
    Esenha.delete(0, END)  
    # Limpar o campo de senha anterior
    Esenha.insert(0, senha)  
    # Inserir a nova senha no campo Esenha
#-------------------------------------------------------------------------------------------------
# função Limpar Senha ----------------------------------------------------------------------------
def limpar(): # Vai Ligar Com Botão Limpar No frontEnd comand = Limpar
    Esenha.delete(0, END)  # Limpar o campo de senha
    Chars.delete(0, END) # Elemina Os valores De chars
    Chars.insert(0, 0) # insere O valor Zero No SpinBox
    Aumentar.set(value=0) # Inser o Valor do Scale a Zero
#------------------------------------------------------------------------------------------------
# Função que vai Conectar a Função ajustar_senha ------------------------------------------------
def criar_senha(tamanho): # Vai ligar Com a Função Ajustar Backend
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))
#------------------------------------------------------------------------------------------------
# função ajustar Senha --------------------------------------------------------------------------
def ajustar_senha(event=None): # Vai ligar Com Scale Aumentar No frontend
    tamanho_atual = len(Esenha.get())
    novo_tamanho = Aumentar.get()  # Supondo que 'Aumentar' é o seu Scale widget
    if novo_tamanho > tamanho_atual:
        # Adiciona caracteres à senha existente para alcançar o novo tamanho
        senha_atual = Esenha.get() + criar_senha(novo_tamanho - tamanho_atual)
        Esenha.delete(0, END)
        Esenha.insert(0, senha_atual)
    elif novo_tamanho < tamanho_atual:
        # Reduz a senha existente para o novo tamanho
        senha_atual = Esenha.get()[:novo_tamanho]
        Esenha.delete(0, END)
        Esenha.insert(0, senha_atual)
#-------------------------------------------------------------------------------------------------
# função para Copiar Senha -----------------------------------------------------------------------
def copiar_senha(): # Vai Ligar Com o Botão Ligar No frontEnd com o Comand=copiar_senha
    janela.clipboard_clear()  # Limpar a área de transferência
    janela.clipboard_append(Esenha.get())  # Copiar a senha para a área de transferência
#------------------------------------------------------------------------------------------------- 
# Função para fechar o aplicativo ----------------------------------------------------------------
def fechar_app(): # Vai Ligar Com o Botão Ligar No frontEnd com o Comand=fechar-app
    resposta = messagebox.askquestion("Fechar", "Tem certeza que deseja fechar o aplicativo?")
    if resposta == "yes":
        janela.destroy()
#------------------------------------------------------------------------------------------------               
#-Fim Backend-------------------------------------------------------------------------------------
# criar as Nossa Cores a Usar --------------------------------------------------------------------
co0='#ffffff' # cor Branco para O fundo e iniciar a Janela
co1='#ffffed' # Amarelo Claro para a Entry
co2='#fff5f2' # Laranja Claro para Os Botões
co3='#f7f8f7' # cinza Claro cor Fundo Aumentar
#----------------------------------------------------------------------------------------------
# Configurar a Janela -------------------------------------------------------------------------
janela = Tk() # Criar a janela e chamar a Biblioteca Tkinter
janela.geometry('600x130+100+100') # Dar uma Geometria a Minha Janela 
janela.resizable(0,0) # defenir se a Nossa janela  pode ou nao ser Maximizada Pelo Utilizador
janela.title('Gerador Senhas Completo ') # dar Um titulo a Nossa Janela
janela.config(bg=co0) # dar uma cor do fundo a Nossa Janela
#----------------------------------------------------------------------------------------------
# implementar O fronte end --------------------------------------------------------------------
#-Inicio---------------------------------------------------------------------------------------
Esenha = Entry(janela, bg=co1, font=('arial 14'), width=52) 
# criar a Entry colocar dentro do master igual a  Esenha = Entry( janela)
# Configurar O nossa Cor do Fundo que é Igual a bg= co1
# Defenir a Fonte e tamanho  que o Nosso Componente Vai usar igual a font=('arial 14')
# Defenir a Nossa Lagura que é Igual a width=52
Esenha.place(x=10, y=10)
# Posicionar a Nossa Entry igual a Esenha.place(x=10, y=10)
# X igual a Posição e y igual a linha 
#-Fim-------------------------------------------------------------------------------------------
#-inicio----------------------------------------------------------------------------------------
Chars = Spinbox(janela, from_=0,to=10, font=('arial 16'), width=3, bg=co1)
# criar O Spinbox e Defenir O master igual a Chars = Spinbox(janela)
# defenir os caracteres de inicio e Fim igual a from_=0,to=10
# defenir a Fonte  e tamanho que o Nosso SpinBox vai Usar igual font=('arial 14')
# defenir a largura que o nosso SpinBox vai ter igual a width=3
# defenir a Cor de fundo Do nosso Spinbox igual a  bg=co1
Chars.place(x=10, y=40) # posicionar O Spinbox  com o sistema Place (x=10, y= 40),
# X igual a Posição e y igual a linha 
#-Fim--------------------------------------------------------------------------------------------
#-Inicio-----------------------------------------------------------------------------------------
BGerar= Button(janela, text='Gerar Senha', font=('arial 10'), relief=RAISED, overrelief=RIDGE, bg=co2, command=gerar_senha)
# criar o Botão Gerar Senha igual a BGerar= Button()
# defenir o seu texto que o botão vai ter igual a text='Gerar Senha'
# defenir a fonte e tamanho que o nosso Botão vai Usar igual a font=('arial 10')
# defenir estilos igual a relief=RAISED, overrelief=RIDGE,
# defenir a nossa cor do fundo do botão bg=co2
# No fim para Ligar O botão Com a Função e so passar O comando igual a eo nome de def command=gerar_senha 
BGerar.place(x=70, y=40) # posicionar O Botão o sistema Place BGerar.place(x=70, y=40),
# X igual a Posição e y igual a linha 
#-Fim--------------------------------------------------------------------------------------------
#-Inicio-----------------------------------------------------------------------------------------
BLimpar= Button(janela, text='Limpar Senha', font=('arial 10'), relief=RAISED, overrelief=RIDGE, bg=co2, command=limpar)
# criar o Botão Limpar Senha igual a BLimpar= Button()
# defenir o seu texto que o botão vai ter igual a text='Limpar Senha'
# defenir a fonte e tamanho que o nosso Botão vai Usar igual a font=('arial 10')
# defenir estilos igual a relief=RAISED, overrelief=RIDGE,
# defenir a nossa cor do fundo do botão bg=co2
# No fim para Ligar O botão Com a Função e so passar O comando igual a eo nome de def command=Limpar 
BLimpar.place(x=160, y=40) # posicionar O Botão o sistema Place BLimpar.place(x=160, y=40),
# X igual a Posição e y igual a linha 
#-Fim----------------------------------------------------------------------------------------------
#-Inicio-------------------------------------------------------------------------------------------
Bcopiar= Button(janela, text='Copiar Senha', font=('arial 10'), relief=RAISED, overrelief=RIDGE, bg=co2, command=copiar_senha)
# criar o Botão Copiar Senha igual a BCopiar= Button()
# defenir o seu texto que o botão vai ter igual a text='Copiar Senha'
# defenir a fonte e tamanho que o nosso Botão vai Usar igual a font=('arial 10')
# defenir estilos igual a relief=RAISED, overrelief=RIDGE,
# defenir a nossa cor do fundo do botão bg=co2
Bcopiar.place(x=255, y=40) # posicionar O Botão o sistema Place BCopiar.place(x=255, y=40),
# X igual a Posição e y igual a linha 
#-Fim---------------------------------------------------------------------------------------------
#-Inicio------------------------------------------------------------------------------------------
BFechar= Button(janela, text='Fechar App', font=('arial 10'), relief=RAISED, overrelief=RIDGE, bg=co2, command=fechar_app)
# criar o Botão FecharApp igual a BFechar= Button()
# defenir o seu texto que o botão vai ter igual a text='Fechar App'
# defenir a fonte e tamanho que o nosso Botão vai Usar igual a font=('arial 10')
# defenir estilos igual a relief=RAISED, overrelief=RIDGE,
# defenir a nossa cor do fundo do botão bg=co2
# no fim Vamos Ligar O nossa def com o botão atarves de Comand=fechar-app
BFechar.place(x=349, y=40) # posicionar O Botão o sistema Place BFechar.place(x=255, y=40),
# X igual a Posição e y igual a linha 
#-Fim--------------------------------------------------------------------------------------------
#-inicio-----------------------------------------------------------------------------------------
Aumentar = Scale(janela, orient=HORIZONTAL, bg=co3, length=570, from_=0, to=54, command=ajustar_senha)
# criar um Scale bar para aumentar Os cracteres Iniciais e colocar O master Igual a Aumentar = Scale(janela)
# Dar uma Orientação ao Scale igual a orient=HORIZONTAL,
# aumentar a Largura ao Scale igual a length=570
# confugurar Uma Cor de Fundo ao Scale igual a bg=co3
# Defenir o valor de Inicio e Fim de Aumentar igual a from_=0, to=54
# No fim para Ligar O Scale Com a Função e so passar O comando igual a e o nome de def command=Limpar 
Aumentar.place(x=10, y=73) # Posicionar O Scale com o Sistema Place igual a Aumentar.place(x=10, y=73)
#-Fim--------------------------------------------------------------------------------------------
# inicio do Componente = inicio
# Fim do componente = Fim
#-Fim Fronte end---------------------------------------------------------------------------------
# Iniciar a nossa janela ------------------------------------------------------------------------
janela.mainloop()
#------------------------------------------------------------------------------------------------