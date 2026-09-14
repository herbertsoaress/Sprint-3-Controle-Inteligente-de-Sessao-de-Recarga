# ChargeGrid Intelligence — Controle Inteligente de Sessão de Recarga
### Sprint 3 — Arquitetura de Computadores | FIAP

Protótipo educacional inspirado no conceito de gerenciamento inteligente de energia do **GoodWe Smart Energy Controller**, simulando uma sessão de recarga (ex.: veículo elétrico) usando **Raspberry Pi Pico + MicroPython**, rodando no simulador **Wokwi**.

## Integrantes
| Nome | RM |
|---|---|
| @Furin | — |
| Herbert Richers | — |
| @Renan_Mano | — |

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
- **Simulador:** [Wokwi](https://wokwi.com/)
- **Saída:** LEDs (verde/amarelo/vermelho) + Monitor Serial

## Estrutura do repositório

```
├── main.py           # Código-fonte do protótipo (Wokwi)
├── diagram.json       # Diagrama de ligação dos componentes no Wokwi
├── README.md          # Este arquivo
└── entrega_final.txt  # Nomes, RMs, link do vídeo e do repositório
```

## Vídeo de demonstração

📺 [Link do vídeo no YouTube (não listado)](#)

## Relação com a disciplina

O protótipo relaciona diretamente os conteúdos de **sistemas numéricos, representação de dados, processadores, memória e sistemas de entrada e saída**, mostrando como um controlador embarcado processa dados reais (geração e consumo de energia) para tomar decisões automatizadas — o mesmo princípio usado por sistemas de gerenciamento inteligente de energia como o GoodWe Smart Energy Controller.
