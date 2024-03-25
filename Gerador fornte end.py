# importar a Nossa biblioteca  ------------------------------------------------------------------
from tkinter import *
#------------------------------------------------------------------------------------------------
# implementar As Nossas Funçoes -----------------------------------------------------------------











#----------------------------------------------------------------------------------------------
# criar as Nossa Cores a Usar -----------------------------------------------------------------
co0='#ffffff' # cor Branco para O fundo e iniciar a Janela
co1='#ffffed' # Amarelo Claro para a Entry
co2='#fff5f2' # Laranja Claro para Os Botões
co3='#f7f8f7' # cinza Claro cor Fundo Aumentar
#----------------------------------------------------------------------------------------------
# Configurar a Janela -------------------------------------------------------------------------
janela = Tk() # Criar a janela e chamar a Biblioteca Tkinter
janela.geometry('600x130+100+100') # Dar uma Geometria a Minha Janela 
janela.resizable(0,0) # defenir se a Nossa janela  pode ou nao ser Maximizada Pelo Utilizador
janela.title('Gerador Senhas Fronte end ') # dar Um titulo a Nossa Janela
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
BGerar= Button(janela, text='Gerar Senha', font=('arial 10'), relief=RAISED, overrelief=RIDGE, bg=co2)
# criar o Botão Gerar Senha igual a BGerar= Button()
# defenir o seu texto que o botão vai ter igual a text='Gerar Senha'
# defenir a fonte e tamanho que o nosso Botão vai Usar igual a font=('arial 10')
# defenir estilos igual a relief=RAISED, overrelief=RIDGE,
# defenir a nossa cor do fundo do botão bg=co2
BGerar.place(x=70, y=40) # posicionar O Botão o sistema Place BGerar.place(x=70, y=40),
# X igual a Posição e y igual a linha 
#-Fim--------------------------------------------------------------------------------------------
#-Inicio-----------------------------------------------------------------------------------------
BLimpar= Button(janela, text='Limpar Senha', font=('arial 10'), relief=RAISED, overrelief=RIDGE, bg=co2)
# criar o Botão Limpar Senha igual a BLimpar= Button()
# defenir o seu texto que o botão vai ter igual a text='Limpar Senha'
# defenir a fonte e tamanho que o nosso Botão vai Usar igual a font=('arial 10')
# defenir estilos igual a relief=RAISED, overrelief=RIDGE,
# defenir a nossa cor do fundo do botão bg=co2
BLimpar.place(x=160, y=40) # posicionar O Botão o sistema Place BLimpar.place(x=160, y=40),
# X igual a Posição e y igual a linha 
#-Fim----------------------------------------------------------------------------------------------
#-Inicio-------------------------------------------------------------------------------------------
Bcopiar= Button(janela, text='Copiar Senha', font=('arial 10'), relief=RAISED, overrelief=RIDGE, bg=co2)
# criar o Botão Copiar Senha igual a BCopiar= Button()
# defenir o seu texto que o botão vai ter igual a text='Copiar Senha'
# defenir a fonte e tamanho que o nosso Botão vai Usar igual a font=('arial 10')
# defenir estilos igual a relief=RAISED, overrelief=RIDGE,
# defenir a nossa cor do fundo do botão bg=co2
Bcopiar.place(x=255, y=40) # posicionar O Botão o sistema Place BCopiar.place(x=255, y=40),
# X igual a Posição e y igual a linha 
#-Fim---------------------------------------------------------------------------------------------
#-Inicio------------------------------------------------------------------------------------------
BFechar= Button(janela, text='Fechar App', font=('arial 10'), relief=RAISED, overrelief=RIDGE, bg=co2)
# criar o Botão FecharApp igual a BFechar= Button()
# defenir o seu texto que o botão vai ter igual a text='Fechar App'
# defenir a fonte e tamanho que o nosso Botão vai Usar igual a font=('arial 10')
# defenir estilos igual a relief=RAISED, overrelief=RIDGE,
# defenir a nossa cor do fundo do botão bg=co2
BFechar.place(x=349, y=40) # posicionar O Botão o sistema Place BFechar.place(x=255, y=40),
# X igual a Posição e y igual a linha 
#-Fim--------------------------------------------------------------------------------------------
#-inicio-----------------------------------------------------------------------------------------
Aumentar = Scale(janela, orient=HORIZONTAL, bg=co3, length=570)
# criar um Scale bar para aumentar Os cracteres Iniciais e colocar O master Igual a Aumentar = Scale(janela)
# Dar uma Orientação ao Scale igual a orient=HORIZONTAL,
# aumentar a Largura ao Scale igual a length=570
# confugurar Uma Cor de Fundo ao Scale igual a bg=co3
Aumentar.place(x=10, y=73) # Posicionar O Scale com o Sistema Place igual a Aumentar.place(x=10, y=73)
#-Fim--------------------------------------------------------------------------------------------
# inicio do Componente = inicio
# Fim do componente = Fim
#-Fim Fronte end---------------------------------------------------------------------------------
# Iniciar a nossa janela ------------------------------------------------------------------------
janela.mainloop()
#------------------------------------------------------------------------------------------------