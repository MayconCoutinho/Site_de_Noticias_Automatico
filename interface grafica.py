import tkinter
from tkinter import*
import link_site

# Janela -> formato, nome, dimenções 

window = tkinter.Tk()
window.title('Notícias')
window.minsize('15','10')

# Botão -> Codigo
button_EN = Button(window, text='    EN    ', command= lambda : link_site.abri_site(link_site.Sites('EN')))
button_Tec = Button(window, text='    Tec    ', command= lambda : link_site.abri_site(link_site.Sites('Tec')))
button_Mundial = Button(window, text='    Mundial    ', command= lambda : link_site.abri_site(link_site.Sites('Mundial')))
button_Pais = Button(window, text='    Pais    ', command= lambda : link_site.abri_site(link_site.Sites('Pais')))
button_Estado = Button(window, text='    Estado    ', command= lambda : link_site.abri_site(link_site.Sites('Estado')))
button_Municipio = Button(window, text='    Município    ', command= lambda : link_site.abri_site(link_site.Sites('Municipio')))
button_Generalista = Button(window, text='    Generalista    ', command= lambda : link_site.abri_site(link_site.Sites('Generalista')))



# Posição do botão 
button_EN.pack(side = LEFT)
button_Tec.pack(side= LEFT)
button_Mundial.pack(side= LEFT)
button_Pais.pack(side= LEFT)
button_Estado.pack(side= LEFT)
button_Municipio.pack(side= LEFT)
button_Generalista.pack(side= LEFT)



# loop 
window.mainloop()