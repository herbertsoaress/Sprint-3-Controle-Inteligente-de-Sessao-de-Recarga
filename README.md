# ChargeGrid Intelligence — Controle Inteligente de Sessão de Recarga
### Sprint 3 — Arquitetura de Computadores | FIAP

Protótipo educacional inspirado no conceito de gerenciamento inteligente de energia do **GoodWe Smart Energy Controller**, simulando uma sessão de recarga (ex.: veículo elétrico) usando **Raspberry Pi Pico + MicroPython**, rodando no simulador **Wokwi**.

## Integrantes
| Nome | RM |
|---|---|
| Gabriel Barbosa Furin | 572941 |
| Gabriel de Almeida Santos | 569395 |
| Herbert Soares de Jesus | 571507 |
| Lucas Kiodi Moraca | 571004 |
| Renan Fracalossi Mano da Silva | 569610 |

## Objetivo

Demonstrar, na prática, a relação entre **entrada de dados, processamento, memória e saída**, aplicando conceitos de Arquitetura de Computadores. O sistema recebe/simula dados de geração e consumo de energia, calcula a energia disponível e determina o estado da sessão de recarga, sinalizando o resultado por meio de LEDs.

```
Energia disponível = Geração - Consumo
```

## Estados do sistema

| Estado | Condição | LED |
|---|---|---|
| 🟢 Recarga autorizada | Energia disponível suficiente | Verde |
| 🟡 Recarga reduzida | Energia disponível limitada (abaixo do mínimo configurado) | Amarelo |
| 🔴 Recarga bloqueada | Energia disponível insuficiente (≤ 0) | Vermelho |

O limite mínimo de recarga (`POTENCIA_MINIMA_RECARGA`) é um valor configurável definido pelo grupo para fins didáticos, já que o enunciado não especifica uma potência mínima exata.

## Como funciona (entrada → processamento → saída)

1. **Entrada (E):** os dados de geração e consumo de energia são fornecidos ao sistema (simulados via lista de cenários no código).
2. **Processamento:** o Raspberry Pi Pico executa a função `controlar_recarga()`, que calcula a energia disponível e compara com o limite mínimo para definir o status da sessão.
3. **Memória:** valores de geração, consumo, energia disponível e status ficam armazenados em variáveis durante a execução do programa.
4. **Saída (S):** o estado da sessão é exibido no Monitor Serial e sinalizado fisicamente pelos LEDs (verde, amarelo, vermelho).

## Representação de dados

Como exigido na Fase 2, o sistema demonstra a representação de um dado (potência mínima de recarga) em decimal, binário e hexadecimal:

```
Decimal:     1000
Binário:     0b1111101000
Hexadecimal: 0x3e8
```

## Cenários de teste

| Geração (W) | Consumo (W) | Energia disponível (W) | Status |
|---|---|---|---|
| 4000 | 1500 | 2500 | RECARGA AUTORIZADA |
| 1800 | 1500 | 300 | RECARGA REDUZIDA |
| 1000 | 1800 | -800 | RECARGA BLOQUEADA |

## Tecnologias

- **Hardware simulado:** Raspberry Pi Pico
- **Linguagem:** MicroPython
- **Simulador:** [Wokwi](https://wokwi.com/projects/474519316567678977/)
- **Saída:** LEDs (verde/amarelo/vermelho) + Monitor Serial

## Estrutura do repositório

```
├── main.py           # Código-fonte do protótipo (Wokwi)
├── diagram.json       # Diagrama de ligação dos componentes no Wokwi
├── README.md          # Este arquivo
└── entrega_final.txt  # Nomes, RMs, link do vídeo e do repositório
```

## Vídeo de demonstração

📺 [Link do vídeo no YouTube (não listado)](https://youtu.be/wlZk4Mj5Nsk)

## Relação com a disciplina

O funcionamento do protótipo aplica os seguintes conceitos da disciplina de Arquitetura de Computadores:

* **Entrada de Dados (Input):** os valores de *geração* e *consumo* atuam como dados de entrada do sistema, simulando a leitura de sensores reais.
* **Processamento (CPU):** a ULA (Unidade Lógica e Aritmética) do Raspberry Pi Pico realiza o cálculo da energia disponível (Geração - Consumo) e utiliza instruções de desvio condicional (`if/elif/else`) para definir o estado da recarga.
* **Memória:** a memória Flash do microcontrolador armazena o código-fonte (instruções). Durante a execução, a memória RAM armazena temporariamente os valores das variáveis para manipulação do processador.
* **Saída (Output/E/S):** o resultado processado é enviado aos periféricos de saída através dos pinos GPIO (acionando fisicamente os LEDs) e via comunicação serial (exibindo os dados no terminal).
* **Representação de Dados:** embora o código-fonte apresente números em decimal, a CPU manipula e processa todas as informações e instruções estritamente em formato binário — daí a demonstração de um dos valores do sistema também em binário e hexadecimal.

Assim, o protótipo mostra como um controlador embarcado processa dados reais (geração e consumo de energia) para tomar decisões automatizadas — o mesmo princípio usado por sistemas de gerenciamento inteligente de energia como o GoodWe Smart Energy Controller.
