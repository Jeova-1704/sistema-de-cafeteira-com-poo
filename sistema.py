import os
import time

CAFE1 = 0
CAFE2 = 0.50
CAFE3 = 0.75
CAFE4 = 1.00
CAFE5 = 1.25
CAFE6 = 1.50
CAFE7 = 1.75
CAFE8 = 2.00
CAFE9 = 5.00

class Cafeteira:
    def __init__(self, cafe=0, leite=0, chocolate=0, copos=0, agua=0, money=00.00) -> None: 

        self.cafePo = cafe
        self.leite = leite
        self.chocolate = chocolate
        self.copos = copos
        self.agua = agua 
        self.money = money   
        self.display = f'RS:{self.money:.2f}'


    def exibir_display(self):
        cafe1 = f'1-Café expresso-R${CAFE1:.2f}'
        cafe2 = f'2-Café longo-R${CAFE2:.2f}'
        cafe3 = f'3-Café pingado-R${CAFE3:.2f}'
        cafe4 = f'4-Capuchino-R${CAFE4:.2f}'
        cafe5 = f'5-Cap-choc-R${CAFE5:.2f}'
        cafe6 = f'6-Chocate-R${CAFE6:.2f}'
        cafe7 = f'7-Café com chocoollate-R${CAFE7:.2f}'
        cafe8 = f'8-Chocolate-com leite R${CAFE8:.2f}'
        cafe9 = f''
        # 9-opção customizada-R${CAFE9:.2f}
        print("╔═════════════════════════════════════════════════════╗")
        print("║                   Maquina de café                   ║")
        print("╠═════════════════════════════════════════════════════╣")
        print(f"║{self.display.center(53)}║")
        print("╠═════════════════════════════════════════════════════╣")
        print(f"║{cafe1.center(27)} {cafe2.center(23)}  ║")
        print(f"║{cafe3.center(27)} {cafe4.center(21)}    ║")
        print(f"║{cafe5.center(23)} {cafe6.center(29)}║")
        print(f"║{cafe7.center(53)}║")
        print(f"║{cafe8.center(53)}║")
        print(f"║{cafe9.center(53)}║") 
        print("╚═════════════════════════════════════════════════════╝")




    def dispensadorCopos(self):
        self.display = 'Dispensando um copo'
        self.exibir_display()
        time.sleep(3)
        Cafeteira.limparJanela(self)


    def aquecendoIngredientes(self):
        self.display = "esquentando os ingredientes"
        self.exibir_display()
        time.sleep(5) 
        Cafeteira.limparJanela(self)

    def moerCafe(self):
        self.display = "Moendo o café"
        self.exibir_display()
        time.sleep(5)
        Cafeteira.limparJanela(self)
    
    def servirCafe(self):
        self.display = "Servindo café..."
        self.exibir_display()
        time.sleep(5)
        Cafeteira.limparJanela(self)
        self.display = "Café servido✓"
        self.exibir_display()
        time.sleep(5)
        Cafeteira.limparJanela(self)

################################################################
    def verificaCafeExpresso(self):
        if self.cafePo >= 75 and self.agua >= 150:
            self.cafePo -= 75
            self.agua-= 150
            return True        
    def verificaCafeLongo(self):
        if self.cafePo >= 20 and self.leite >= 60 and self.agua >= 60:
            self.cafePo -= 150
            self.leite -= 30
            self.agua -= 120
            return True
    def verificaCafePingado(self):
        if self.cafePo >= 10 and self.leite >= 100 and self.agua >= 40:
            self.cafePo -= 150
            self.leite -= 135
            self.agua -= 20
            return True
    def verificaCapuchino(self):
        if self.cafePo >= 20 and self.agua >= 30 and self.leite >= 100: 
            self.cafePo -= 150
            self.agua -= 30
            self.leite -= 100
            return True
    def verificaCapChoc(self):
        if self.cafePo >= 10 and self.leite >= 130 and self.chocolate >= 10:
            self.cafePo -= 100
            self.leite -= 150
            self.chocolate -= 150
            return True
    def verificaCafeComChocolate(self):
        if self.cafePo >= 40 and self.chocolate >= 100 and self.agua >= 130:
            self.cafePo -= 40
            self.agua -= 130
            self.chocolate -= 100
            return True
    def verificahocolate(self):
        if self.chocolate >=100 and self.agua >= 140:
            self.chocolate -= 100
            self.agua -= 140
            return True
    def verificaChocolateComLeite(self):
        if self.chocolate >= 80 and self.leite >= 140 :
            self.chocolate -= 80
            self.leite -= 140
            return True
    def verificaCopos(self):
        if self.copos > 0:
            self.copos -= 1
            return True
################################################################

    def devolvendoTroco(self):
        self.display = f'Devolvendo o seu troco de R${self.money:.2f}'
        self.money = 0
    
    def devolverDinheiroNaoUsado(self):
        self.display = f'Devolvendo o se dinhiero R${self.money:.2f}'
        time.sleep(3)
        self.money = 0
    
    def naoTemIngredientes(self):
        Cafeteira.limparJanela(self)
        self.display = 'Ingrendientes em falta✕'
        self.exibir_display()
        time.sleep(5)
        Cafeteira.limparJanela(self)
    
    def encerramento(self):
        self.display = 'Obrigado por usar nosso serviço!'
        self.exibir_display()
        time.sleep(3)
    
    def limparJanela(self):
        os.system('cls')
    
    def displayMoney(self):
        self.limparJanela()
        self.display = f'RS:{self.money:.2f}'
        self.exibir_display()
    
    def addmoney(self, valor):
        self.money += valor

    def escolhaBebidas(self):
        while True:
            escolha = input("Escolha a sua bebida: ")
            if escolha in '123456789990':
                return int(escolha)
            
    
    