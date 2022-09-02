from cProfile import label
from tkinter import *
from tkinter import Tk, ttk
from turtle import left
from PIL import Image,ImageTk
#cores
c01 ="#f5eeee"#branco
c02 ="#f2f055"#amarelo
c03 ="#84c7e2"#azul claro
c04 = "#03c78a"#verde
c05 ="#ff0000"#vermelho
c06="#da6523"#laranja
c07 ="#040404"#preto

# criando janela
janela = Tk()
janela.title("Orçamento")
janela.geometry('250x400')
janela.configure(bg=c01)
janela.resizable(width=False,height=False)
style = ttk.Style(janela)
style.theme_use('clam')


#Frames

framecima = Frame(janela,width=300,height=50,bg=c01,relief='flat')
framecima.grid(row=0,column=0)

framemeio = Frame(janela,width=300,height=90,bg=c01,relief='flat')
framemeio.grid(row=1,column=0)

framebaixo = Frame(janela,width=300,height=290,bg=c01,relief='flat')
framebaixo.grid(row=2,column=0)





#logo
app_= Label(framecima,text='Orçamento',compound=LEFT,padx=5,anchor=NW,font=('verdana 20'), relief=FLAT,bg=c01,fg=c07)
app_.place(x=0,y=0)


#abrindo imagem
img =Image.open("log.png")
img = img.resize((35,35))
img=ImageTk.PhotoImage(img)

app_logo= Label(framecima,image=img,compound=LEFT,padx=5,anchor=NW,font=('verdana 20'), relief=FLAT,bg=c01,fg=c07)
app_logo.place(x=160,y=0)

app_linha= Label(framecima,width=295,anchor=NW,font=('verdana 1'), relief=FLAT,bg=c07,fg=c01)
app_linha.place(x=0,y=47)

#função Calcular
def calcular():
    
    renda = float(e_valor.get())
    n50= renda * 0.50
    n30 = renda * 0.30
    n20 = renda * 0.20
    l_necessidades['text']=(f'R${n50:,.2f}')
    l_gastos['text']=(f'R${n30:,.2f}')
    l_investimendo['text']=(f'R${n20:,.2f}')
   


#Meio
app_= Label(framemeio,text='Renda mensal? ',anchor=NW,font=('ivy 10'), relief=FLAT,bg=c01,fg=c07)
app_.place(x=7,y=15)
 
e_valor =Entry(framemeio,width=10,  font=('ivy 14'), relief='solid',justify='center')
e_valor.place(x=10,y=40)

bnt_valor =Button(framemeio,command=calcular,text='Calcular'.upper(),font=('ivy 9'),anchor=NW, overrelief=RIDGE,bg=c04,fg=c07)
bnt_valor.place(x=150,y=40)

#baixo

app_= Label(framebaixo,text='Seus números de: 50%, 30%, 20%',width=35 ,anchor=NW,font=('verdana 10'), relief=FLAT,bg=c04,fg=c07)
app_.place(x=0,y=0)

# necessidades

l_necessidades= Label(framebaixo,text='Necessidades 50%'.upper(),width=35,
anchor=NW,font=('verdana 10'), relief=FLAT,bg=c01,fg=c07)
l_necessidades.place(x=10,y=40)
l_necessidades= Label(framebaixo,width=22,
anchor=NW,font=('verdana 12'), relief=FLAT,bg=c04,fg=c07)
l_necessidades.place(x=10,y=75)

#gastos
l_gastos= Label(framebaixo,text='Gastos 30%'.upper(),width=35,
anchor=NW,font=('verdana 10'), relief=FLAT,bg=c01,fg=c07)
l_gastos.place(x=10,y=115)

l_gastos= Label(framebaixo,width=22,
anchor=NW,font=('verdana 12'), relief=FLAT,bg=c04,fg=c07)
l_gastos.place(x=10,y=145)

#Investimento
l_investimendo= Label(framebaixo,text='Investimento 20%'.upper(),width=35,
anchor=NW,font=('verdana 10'), relief=FLAT,bg=c01,fg=c07)
l_investimendo.place(x=10,y=185)

l_investimendo= Label(framebaixo,width=22,
anchor=NW,font=('verdana 12'), relief=FLAT,bg=c04,fg=c07)
l_investimendo.place(x=10,y=215)

janela.mainloop()
