##todos os carrinhos
dicionarioCart = {
    1:[
     { 
     'produto':'banana',
     'preco':2
     },
     {
     'produto':'pessego',
     'preco':2 
     },
     {
     'produto':'pessego',
     'preco':2 
     }
     ]
}
##armazem
dicionarioArmazem = {
     'banana':1,
     'pessego':1
}

def check_availability(cart,inventory):
    quantidadesCart={}
    vezes = 0
    for y in dicionarioCart[cart]:
        produto = y
        if y['produto'] not in quantidadesCart:
            
            quantidadesCart[y['produto']] = 1
        else:
            quantidadesCart[y['produto']] = quantidadesCart.get(y['produto']) +1
    for x,y in quantidadesCart.items():
        if dicionarioArmazem[x]<=y:
            vezes +=1
        else:
            vezes +=0
        if vezes >0:
            return False
        else:
            return True

if __name__ == '__main__':
    print(check_availability(1,dicionarioArmazem))

