# Abre sites de Noticias em Portuquês ou Inglês 


def Sites(Sigla): # Com a Sigla 'BR' ou 'EN' retornar a url dos sites correspondete a Nacionalidade da sigla 

    # Cadastramento dos Sites EN

    site_EN = [

    'https://www.bbc.com/',
    'https://www.nytimes.com/']

    # Sites de Tecnologias

    site_Tec = [
        
        'https://www.tomshardware.com/',
        'https://olhardigital.com.br/editorias/noticias/'

        ] 

    # Cadastro de sites mundiais

    site_Mundial = [

        'https://br.sputniknews.com/'

        ]

    site_Pais = [


        'https://g1.globo.com/',  
        'https://g1.globo.com/economia/agronegocios/',

        ]

    site_Estado = [

        
        'http://g1.globo.com/espirito-santo/agronegocios/',
        'https://g1.globo.com/es/espirito-santo/'
        
        ]

    site_Municipio = [

        'https://www.agazeta.com.br/tema/itapemirim',
        'https://g1.globo.com/es/espirito-santo/cidade/itapemirim/',
        'https://www.itapemirim.es.gov.br/'

        ]

    site_Generalista = [
        
        'https://www.cnnbrasil.com.br/',
        'https://manchetesdodia.com/'   
             
        ]


    # Comfirmação de qual é a Sigla posta e retorna a lista correspondete 
    if Sigla == 'EN':
        return site_EN
    elif Sigla == 'Tec':
        return site_Tec
    elif Sigla == 'Mundial':
        return site_Mundial
    elif Sigla == 'Pais':
        return site_Pais
    elif Sigla == 'Estado':
        return site_Estado
    elif Sigla == 'Municipio':
        return site_Municipio
    elif Sigla == 'Generalista':
        return site_Generalista
    else:
        return print('Erro!')
        

def abri_site(sites): # Abre as url no navegador 

    import webbrowser # importando webbrowser 
    for abrir in sites: # Loop para abri todos sites da Lista
        webbrowser.open(abrir, new=0, autoraise=True) 


