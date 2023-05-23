from sistema import *
import os
import time

"""
Cafe = gramas 
leite = ml
chcolate = gramas 
copos = unidades 
agua = ml
"""
QuantidadeDeCafe = 1000
QuantidadeDeleite = 1000
QuantidadeDechocolate = 1000
QuantidadeDeCopos = 50
QuantidadeDeAgua = 1000
cafeteira = Cafeteira(QuantidadeDeCafe, QuantidadeDeleite, QuantidadeDechocolate, QuantidadeDeCopos, QuantidadeDeAgua)

while True:
    cafeteira.displayMoney()
    try:
        valor = float(input("Valor para adicionar na maquina: R$")) or float(0)
        
    except ValueError:
        valor = 0
    cafeteira.addmoney(valor=0)
    cafeteira.displayMoney()

    escolha = cafeteira.escolhaBebidas()

    if escolha == 0:
        cafeteira.display = f'{cafeteira.cafePo=}-{cafeteira.leite=}-{cafeteira.chocolate=}-{cafeteira.copos=}-{cafeteira.agua=}'
        cafeteira.exibir_display()
        time.sleep(5)
        continue
    if escolha == 999:
        break


    tem_ingredientes_e_copos = False 
    if escolha == 1:
        tem_ingredientes_e_copos = cafeteira.verificaCafeExpresso()

    elif escolha == 2:
        if cafeteira.money < CAFE2:
            cafeteira.display = "compra inválida: efetue um deposito"
            cafeteira.exibir_display()
            continue
        tem_ingredientes_e_copos = cafeteira.verificaCafeLongo()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= CAFE2
        
    elif escolha == 3:
        if cafeteira.money < CAFE3:
            continue
        tem_ingredientes_e_copos = cafeteira.verificaCafePingado()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= CAFE3

    elif escolha == 4:
        if cafeteira.money < CAFE4:
            continue
        tem_ingredientes_e_copos = cafeteira.verificaCapuchino()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= CAFE4

    elif escolha == 5:
        if cafeteira.money < CAFE5:
            continue
        tem_ingredientes_e_copos = cafeteira.verificaCapChoc()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= CAFE5

    elif escolha == 6:
        if cafeteira.money < CAFE6:
            continue
        tem_ingredientes_e_copos = cafeteira.verificahocolate()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= CAFE6

    elif escolha == 7:
        if cafeteira.money < CAFE7:
            continue
        tem_ingredientes_e_copos = cafeteira.verificaCafeComChocolate()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= CAFE7

    elif escolha == 8:
        if cafeteira.money < CAFE8:
            continue
        tem_ingredientes_e_copos = cafeteira.verificaChocolateComLeite()
        if tem_ingredientes_e_copos == True:
            cafeteira.money -= CAFE8

    tem_ingredientes_e_copos = cafeteira.verificaCopos()

    # elif escolha == 9:
    #     if cafeteira.money < CAFE:
    #         continue
    #     cafeteira.money -= CAFE


    if tem_ingredientes_e_copos == True:
        os.system("cls")
        cafeteira.dispensadorCopos()
        if str(escolha) in "1234567":
            cafeteira.aquecendoIngredientes()
        cafeteira.moerCafe()
        cafeteira.servirCafe()

        if cafeteira.money > 0:
            cafeteira.devolvendoTroco()
            cafeteira.exibir_display()
            time.sleep(3)


    elif tem_ingredientes_e_copos == False:

        if cafeteira.money > 0:
            cafeteira.devolverDinheiroNaoUsado()
            cafeteira.exibir_display()
            time.sleep(3)
            cafeteira.limparJanela()

    cafeteira.limparJanela()
    cafeteira.encerramento()