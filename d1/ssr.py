#carregar os dados 
dados =[{"nome": "Brun","cidade":"Viana"},
        {"nome": "Adama","cidade":"Recife"}
        ]


#processar os dados 
template = """\ 
<html>
    <body>
        <lu>
            <li> {dados[Nome:]} </li>
            <li> {dados[Cidade:]} </li>
        </lu>
    </body>

</html>
"""

#renderizar os dados

for item in dados:
    print(template.format(dados=item))
    