from PySimpleGUI import PySimpleGUI as sg
import link_site

# Layout

sg.theme('DarkBrown1') 

layout = [

    [sg.Button('Tecnologia', size= 30, font= 'Calibri')],
    [sg.Button('Mundial', size= 30, font= 'Calibri')],
    [sg.Button('Pais', size= 30, font= 'Calibri')],
    [sg.Button('Estado', size= 30, font= 'Calibri')],
    [sg.Button('Municipio', size= 30, font= 'Calibri')],
    [sg.Button('English', size= 30, font= 'Calibri')],
    [sg.Button('Generalista', size= 30, font= 'Calibri')]


]


# Janela

janela = sg.Window('Notícias', layout, background_color= "#000000")

# Ler os eventos


while True:

    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'English':
        link_site.abri_site(link_site.Sites('EN'))

    if evento == 'Tecnologia':
        link_site.abri_site(link_site.Sites('Tec'))

    elif evento == 'Mundial':
        link_site.abri_site(link_site.Sites('Mundial'))

    if evento == 'Pais':
        link_site.abri_site(link_site.Sites('Pais'))
    if evento == 'Estado':
        link_site.abri_site(link_site.Sites('Estado'))

    if evento == 'Municipio':
        link_site.abri_site(link_site.Sites('Municipio'))

    if evento == 'Generalista':
        link_site.abri_site(link_site.Sites('Generalista'))

        

