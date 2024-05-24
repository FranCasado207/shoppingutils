##todos os carrinhos
dicionario = {
    1:[
     { 
     'produto':'banana',
     'preco':2
     },
     {
     'produto':'pessego',
     'preco':2 
     }
     ]
}




def calculate_total_price(cart):
    soma = 0
    for y in dicionario[cart]:
        soma += y['preco']
    return soma

if __name__ == '__main__':
    print(calculate_total_price(1))