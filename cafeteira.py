from sistemas import Cafeteira, reservatorios, precos_cafes

"""
Cafe = gramas 
leite = ml
chcolate = gramas 
copos = unidades 
agua = ml
"""

cafeteira = Cafeteira( reservatorios["QuantidadeDeCafe"], reservatorios["QuantidadeDeleite"], reservatorios["QuantidadeDechocolate"], reservatorios["QuantidadeDeCopos"], reservatorios["QuantidadeDeAgua"])

while True:
    cafeteira.exibir_display('valor')
    try:
        valor = float(input("Valor para adicionar na maquina: R$"))
        
    except ValueError:
        valor = 0

    cafeteira.addmoney(valor)
    cafeteira._timeClean()
    cafeteira.exibir_display('valor')

    escolha = input("Digite o valor de sua bebida: ")
    cafeteira._timeClean()
    try:
        escolha = int(escolha)
    except ValueError:
        cafeteira.exibir_display('Por favor digite um valor válido')
        cafeteira._timeClean(5)
        continue
    if 9 < escolha <998:
        cafeteira.exibir_display('Por favor digite um valor válido')
        cafeteira._timeClean(5)
        continue

    if escolha == 0:
        cafeteira.mostarReservatorio()
        continue

    if escolha == 999:
        if cafeteira.money > 0:
            cafeteira.devolverDinheiroNaoUsado()
        cafeteira.encerramento()
        cafeteira.desligando()
        break

##############VERIFICADO ATÉ AQUI###############################

    tem_ingredientes_e_copos = False 

    if escolha == 1:
        tem_ingredientes_e_copos = cafeteira.verificaCafeExpresso()
        tem_ingredientes_e_copos = cafeteira.verificaCopos()

    elif escolha == 2:
        if cafeteira.money < precos_cafes["CAFE2"]:
            cafeteira.falta_dinheiro()
            continue
        tem_ingredientes_e_copos = cafeteira.verificaCafeLongo()
        tem_ingredientes_e_copos = cafeteira.verificaCopos()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= precos_cafes["CAFE2"]
        
    elif escolha == 3:
        if cafeteira.money < precos_cafes["CAFE3"]:
            cafeteira.falta_dinheiro()
            continue
        tem_ingredientes_e_copos = cafeteira.verificaCafePingado()
        tem_ingredientes_e_copos = cafeteira.verificaCopos()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= precos_cafes["CAFE3"]

    elif escolha == 4:
        if cafeteira.money < precos_cafes["CAFE4"]:
            cafeteira.falta_dinheiro()
            continue
        tem_ingredientes_e_copos = cafeteira.verificaCapuchino()
        tem_ingredientes_e_copos = cafeteira.verificaCopos()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= precos_cafes["CAFE4"]


    elif escolha == 5:
        if cafeteira.money < precos_cafes["CAFE5"]:
            cafeteira.falta_dinheiro()
            continue
        tem_ingredientes_e_copos = cafeteira.verificaCapChoc()
        tem_ingredientes_e_copos = cafeteira.verificaCopos()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= precos_cafes["CAFE5"]

    elif escolha == 6:
        if cafeteira.money < precos_cafes["CAFE6"]:
            cafeteira.falta_dinheiro()
            continue
        tem_ingredientes_e_copos = cafeteira.verificahocolate()
        tem_ingredientes_e_copos = cafeteira.verificaCopos()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= precos_cafes["CAFE6"]

    elif escolha == 7:
        if cafeteira.money < precos_cafes["CAFE7"]:
            cafeteira.falta_dinheiro()
            continue
        tem_ingredientes_e_copos = cafeteira.verificaCafeComChocolate()
        tem_ingredientes_e_copos = cafeteira.verificaCopos()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= precos_cafes["CAFE7"]

    elif escolha == 8:
        if cafeteira.money < precos_cafes["CAFE8"]:
            cafeteira.falta_dinheiro()
            continue
        tem_ingredientes_e_copos = cafeteira.verificaChocolateComLeite()
        tem_ingredientes_e_copos = cafeteira.verificaCopos()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= precos_cafes["CAFE8"]

    if tem_ingredientes_e_copos == True:
        cafeteira._timeClean()
        cafeteira.dispensadorCopos()
        if str(escolha) in "1234567":
            cafeteira.aquecendoIngredientes()
        cafeteira.moerCafe()
        cafeteira.servirCafe()

        if cafeteira.money > 0:
            cafeteira.devolvendoTroco()

    if tem_ingredientes_e_copos == False:
        cafeteira.falta_igredientes()
        if cafeteira.money > 0:
            cafeteira.devolverDinheiroNaoUsado()
        cafeteira.encerramento()
        cafeteira.desligando()
        break

    cafeteira.encerramento()
    