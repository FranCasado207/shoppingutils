# shopping utils
Este package possibilita calcular o preco total de um "cart", usando um dicionário (contem exemplo no código)
Aplicar discontos a um "cart"
E verificar se existe disponibilidade de produtos no armazém (contém um dicionario armazém, que poderá servir como exemplo)

O módulo cart contem a função "calculate_total_price(cart)"; <br>
O módulo discount contem a função "applydiscount(cart,discount)"; <br>
O módulo inventory comtem a função "check_availability(cart,inventory)" <br>

<br><t>Variveis:<br>
cart = identificador do cart dentro de um dicionario <br>
discount = valor do desconto de 0% a 100% <br>
inventory = dicionario que contem todos os produtos <br>
<br>
<br>
<br>
<br>
<t>Requisitos
<br>
Para usar este package, necessita o python
<t>Instalação
<br>
Para instalar use este código no terminal:<br>
"pip install git+https://github.com/FranCasado207/shoppingutils"