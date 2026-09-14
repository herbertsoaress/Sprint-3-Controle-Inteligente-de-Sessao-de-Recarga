from machine import Pin
from time import sleep

# LEDs
led_verde = Pin(13, Pin.OUT)
led_amarelo = Pin(15, Pin.OUT)
led_vermelho = Pin(14, Pin.OUT)

# Valor configurável do protótipo
# Limite definido pelo grupo para o protótipo educacional.
# O enunciado não estabelece uma potência mínima específica.
POTENCIA_MINIMA_RECARGA = 1000


def desligar_leds():
    led_verde.value(0)
    led_amarelo.value(0)
    led_vermelho.value(0)


def controlar_recarga(geracao, consumo):
    disponivel = geracao - consumo

    desligar_leds()

    if disponivel <= 0:
        status = "RECARGA BLOQUEADA"
        led_vermelho.value(1)

    elif disponivel < POTENCIA_MINIMA_RECARGA:
        status = "RECARGA REDUZIDA"
        led_amarelo.value(1)

    else:
        status = "RECARGA AUTORIZADA"
        led_verde.value(1)

    print("----------------------------")
    print("GERACAO:", geracao, "W")
    print("CONSUMO:", consumo, "W")
    print("DISPONIVEL:", disponivel, "W")
    print("STATUS:", status)

    return disponivel, status


# Cenários fornecidos pela Sprint
cenarios = [
    (4000, 1500),
    (1800, 1500),
    (1000, 1800)
]


for geracao, consumo in cenarios:
    controlar_recarga(geracao, consumo)
    sleep(3)

# ==========================================
# FASE 2 - ADICIONADO POR: @Renan_Mano
# ==========================================

sleep(1) # Pausa pequena após os testes da Fase 1

# 1. Demonstração de representação de dados
dado_exemplo = POTENCIA_MINIMA_RECARGA
print("\n--- FASE 2: REPRESENTACAO DE DADOS ---")
print("Dado escolhido: Potencia Minima de Recarga")
print("Decimal:    ", dado_exemplo)
print("Binario:    ", bin(dado_exemplo))
print("Hexadecimal:", hex(dado_exemplo))