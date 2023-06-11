#carregar os dados 
dados =[{"nome": "Brun","cidade":"Viana"},
        {"nome": "Adama","cidade":"Recife"}
        ]


#processar os dados 
template ="""
<html>
    <body>
        <lu>
            <li> {dados[nome]} </li>
            <li> {dados[cidade]} </li>
        </lu>
    </body>

</html>
"""

#renderizar os dados

for item in dados:
    print(template.format(dados=item))

    