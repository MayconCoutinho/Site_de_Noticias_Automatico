# Abre sites de Noticias em Portuquês ou Inglês 


def Sites(Sigla): # Com a Sigla 'BR' ou 'EN' retornar a url dos sites correspondete a Nacionalidade da sigla 

    # Cadastramento dos Sites EN

    site_EN = [

    'https://www.bbc.com/',

    'https://www.newyorker.com/',

    'https://www.economist.com/',

    'https://www.nytimes.com/']

    # Sites de Tecnologias

    site_Tec = [
        
        'https://www.tomshardware.com/',
        'https://www.profissionaisti.com.br/',
        'https://tecnoblog.net/',
        'https://www.tecmundo.com.br/',
        'https://www.techtudo.com.br/',
        'https://gizmodo.uol.com.br/',
        'https://olhardigital.com.br/editorias/noticias/'

        ] 

    # Cadastro de sites mundiais

    site_Mundial = [

        'https://g1.globo.com/ciencia/',
        'https://g1.globo.com/meio-ambiente/',
        'https://g1.globo.com/turismo-e-viagem/',
        'https://g1.globo.com/tecnologia/',
        'https://forbes.com.br/',
        'https://pt.euronews.com/',
        'https://br.sputniknews.com/'

        ]

    site_Pais = [

        'https://otrabalhador.com/',
        'https://g1.globo.com/',  
        'https://g1.globo.com/economia/agronegocios/',

        ]

    site_Estado = [

        'https://g1.globo.com/es/espirito-santo/',
        'http://g1.globo.com/espirito-santo/agronegocios/',
        'http://g1.globo.com/espirito-santo/concursos-e-emprego/'
        
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


