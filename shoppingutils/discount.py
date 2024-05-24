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

dicionarioDisconto = {}

def apply_discount(cart,discount):
    dicionarioDisconto = dicionario
    for y in dicionarioDisconto[cart]:
        y['preco'] = (y.get('preco')-y.get('preco')*(discount/100))
    return dicionarioDisconto
        

if __name__ == '__main__':
    print(apply_discount(1,2))