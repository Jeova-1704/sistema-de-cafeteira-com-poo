# Cafeteira Automática
 Este projeto implementa uma cafeteira automática em Python. A cafeteira é capaz de preparar várias bebidas diferentes, como café expresso, café longo, café pingado, cappuccino, cappuccino de chocolate e chocolate quente.
 
 ## Funcionalidades
 <li> Adicionar dinheiro à máquina de café </li>
 <li> Escolher uma bebida para preparar </li>
 <li> Verificar se há ingredientes suficientes para preparar a bebida escolhida </li>
 <li> Deduzir o valor da bebida do dinheiro adicionado </li>
 <li> Exibir o dinheiro disponível na máquina </li>
 <li> Exibir a quantidade de ingredientes restantes na cafeteira </li>
 
 # cafeteira.py
 O arquivo `cafeteira.py` é o programa principal da cafeteira automática. Ele importa o módulo `sistema` para acessar a classe `Cafeteira` e utiliza essa classe para simular o funcionamento da cafeteira.

O programa começa criando uma instância da classe `Cafeteira` com valores iniciais para a quantidade de café, leite, chocolate, copos e água disponíveis, e também o dinheiro inicial da máquina.

Em seguida, o programa entra em um loop infinito que exibe o dinheiro disponível na máquina e solicita ao usuário que insira um valor para adicionar à máquina. Isso simula o ato de inserir dinheiro na cafeteira para comprar as bebidas.

Após receber o valor inserido pelo usuário, o programa exibe um menu de opções para que o usuário escolha uma bebida. As opções são numeradas de 1 a 9, e cada número corresponde a uma bebida específica. A opção 0 permite ao usuário verificar a quantidade restante de ingredientes na cafeteira, e a opção 999 encerra o programa.

Dependendo da opção escolhida, o programa verifica se há ingredientes e copos suficientes para preparar a bebida selecionada. Se houver ingredientes suficientes, o programa realiza as etapas de preparação da bebida, como dispensar um copo, aquecer os ingredientes, moer o café e servir a bebida. O valor da bebida é deduzido do dinheiro disponível na máquina.

Se não houver ingredientes ou copos suficientes para a bebida escolhida, o programa exibe uma mensagem informando que a bebida não pode ser preparada.

Além disso, se houver dinheiro disponível na máquina e o usuário não escolher uma bebida, o programa devolve o dinheiro inserido. Isso simula a funcionalidade de devolver o troco caso o usuário mude de ideia antes de fazer a compra.

O programa também possui funcionalidades adicionais, como limpar a janela do console, exibir mensagens de encerramento e exibir a quantidade de dinheiro disponível na máquina.

# sistema.py
 O arquivo `sistema.py` contém a definição da classe `Cafeteira`, que representa a cafeteira automática. Essa classe encapsula o comportamento e os atributos relacionados à cafeteira.
 
 A classe `Cafeteira` possui os seguintes atributos:
 <li> `cafePo`- representa a quantidade de café em gramas disponível na cafeteira. </li>
 <li> `leite`- representa a quantidade de leite em ml disponível na cafeteira. </li>
 <li> `chocolate`- representa a quantidade de chocolate em gramas disponível na cafeteira. </li>
 <li> `copos`- representa a quantidade de copos disponíveis na cafeteira. </li>
 <li> `agua`- representa a quantidade de água em ml disponível na cafeteira. </li>
 <li> `money`- representa o dinheiro disponível na máquina. </li>
 
 Essa classe também possui vários métodos que implementam as funcionalidades da cafeteira:
 
 <li>`exibir_display()`: exibe o display da cafeteira, mostrando a quantidade de ingredientes e o dinheiro disponível. </li>
 <li> `dispensar_copo()`: verifica se há copos disponíveis e, se sim, decrementa a quantidade de copos. </li>
 <li> `aquecer_ingredientes()`: verifica a quantidade de água, café, leite e chocolate necessários para a bebida selecionada e decrementa a quantidade correspondente dos ingredientes disponíveis. </li>
 <li> `moe_cafe()`: verifica se há café suficiente e decrementa a quantidade necessária. </li>
 <li> `servir_bebida(valor_bebida)`: serve a bebida e incrementa o dinheiro disponível na máquina. </li>
 <li> `verificar_ingredientes(opcao_bebida)`: verifica se há ingredientes suficientes para a bebida selecionada. </li>
 <li> `verificar_copos()`: verifica se há copos disponíveis. </li>
 <li> `adicionar_ingrediente(opcao_ingrediente, quantidade)`: adiciona uma quantidade específica de um ingrediente à cafeteira. </li>
 <li> `adicionar_copos(quantidade)`: adiciona uma quantidade específica de copos à cafeteira. </li>
 <li> `adicionar_dinheiro(valor)`: adiciona um valor específico ao dinheiro disponível na máquina. </li>
 
 # Considerações finais
 O projeto da cafeteira automática utiliza os princípios da programação orientada a objetos (POO) e modularização para organizar e estruturar o código. A classe Cafeteira encapsula o comportamento da cafeteira e seus atributos, enquanto os métodos definidos nessa classe representam as funcionalidades e operações da cafeteira.

Com esse projeto, é possível simular o funcionamento de uma máquina de café automática, permitindo que o usuário escolha diferentes bebidas e interaja com a cafeteira. A estrutura modular do código facilita a manutenção e a extensão do sistema, permitindo que novas funcionalidades sejam adicionadas de forma modular e independente.

 
 
 ## Requisitos
 • Python 3.7 ou superior
 
 
 
 
