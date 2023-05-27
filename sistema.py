import os
import time

precos_cafes = {
    "CAFE1": 0,
    "CAFE2": 0.50,
    "CAFE3": 0.75,
    "CAFE4": 1.00,
    "CAFE5": 1.25,
    "CAFE6": 1.50,
    "CAFE7": 1.75,
    "CAFE8": 2.00,
}
reservatorios = {
    "QuantidadeDeCafe": 1000,
    "QuantidadeDeleite": 1000,
    "QuantidadeDechocolate": 1000,
    "QuantidadeDeCopos": 50,
    "QuantidadeDeAgua": 1000,
}

class Cafeteira:
    def __init__(self, cafe=0, leite=0, chocolate=0, copos=0, agua=0, money=00.00) -> None: 

        self.cafePo: float = cafe
        self.leite: float = leite
        self.chocolate: float = chocolate
        self.copos: float = copos
        self.agua: float = agua 
        self.money: float = money   

    def exibir_display(self, mensagem):
        if mensagem == "valor":
            self.display = f'RS:{self.money:.2f}'
        else:
            self.display = mensagem
        cafe1 = f'1-Café expresso-R${precos_cafes["CAFE1"]:.2f}'
        cafe2 = f'2-Café longo-R${precos_cafes["CAFE2"]:.2f}'
        cafe3 = f'3-Café pingado-R${precos_cafes["CAFE3"]:.2f}'
        cafe4 = f'4-Capuchino-R${precos_cafes["CAFE4"]:.2f}'
        cafe5 = f'5-Cap-choc-R${precos_cafes["CAFE5"]:.2f}'
        cafe6 = f'6-Chocate-R${precos_cafes["CAFE6"]:.2f}'
        cafe7 = f'7-Café com chocoollate-R${precos_cafes["CAFE7"]:.2f}'
        cafe8 = f'8-Chocolate-com leite R${precos_cafes["CAFE8"]:.2f}'
        desligar = f'999- para desligar a maquina'
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
        print(f"║{desligar.center(53)}║")
        print("╚═════════════════════════════════════════════════════╝")

    def dispensadorCopos(self):
        self.exibir_display('Dispensando um copo')
        self._timeClean(5)

    def aquecendoIngredientes(self):
        self.exibir_display("esquentando os ingredientes") 
        self._timeClean(5)

    def moerCafe(self):
        self.exibir_display("Moendo o café")
        self._timeClean(5)
    
    def servirCafe(self):
        self.exibir_display("Servindo café...")
        self._timeClean(5)
        self.exibir_display("Café servido✓")
        self._timeClean(5)

    def devolvendoTroco(self):
        self.exibir_display(f'Devolvendo o seu troco de R${self.money:.2f}')
        self._timeClean(5)
        self.money = 0
    
    def devolverDinheiroNaoUsado(self):
        self.exibir_display(f'Devolvendo o se dinhiero R${self.money:.2f}')
        self._timeClean(5)
        self.exibir_display('valor')
        self._timeClean()
        self.money = 0

    def naoTemIngredientes(self):
        self.exibir_display('Ingrendientes em falta✕')
        self._timeClean(5)
    
    def encerramento(self):
        self.exibir_display('Obrigado por usar nosso serviço!')
        self._timeClean(5)

    def _timeClean(self, segundos=0):
        time.sleep(segundos)
        os.system('cls')

    def addmoney(self, valor=0):
        self.money += valor

    def mostarReservatorio(self):
        print('Café: ', self.cafePo)
        print('Leite: ', self.leite)
        print('Água: ', self.agua)
        print('Chocolate: ', self.chocolate)
        print('Copos: ', self.copos)
        self._timeClean(10)
            
    def falta_dinheiro(self):
        self.exibir_display("compra inválida: valor insuficiente")
        self._timeClean(5)

    def falta_igredientes(self):
        self.exibir_display("compra inválida: Falta ingredientes")
        self._timeClean(5)
        self.exibir_display("contate o gerente para reabastecer")
        self._timeClean(5)

    def desligando(self):
        self.exibir_display("Desligando...")
        self._timeClean(5)
        self.exibir_display(" ")
        self._timeClean(5)
#######################VERIFICADO ATÉ AQUI##################################
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
        else:
            return False
        
################################################################
