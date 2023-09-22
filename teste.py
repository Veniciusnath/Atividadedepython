def velocidade_vertical(v0y, g, t):
    vy = v0y - g * t
    return vy

def velocidade_horizontal(v0x):
    vx = v0x
    return vx

def tempo_voo_maximo(v0y, g):
    t_max = v0y / g
    return t_max
velocidade_vertical_em_instante = velocidade_vertical
velocidade_horizontal_em_instante = velocidade_horizontal

print("Velocidade Vertical em","segundos:", velocidade_vertical_em_instante, "m/s")
print("Velocidade Horizontal em qualquer instante:", velocidade_horizontal_em_instante, "m/s")
def alcance_horizontal(v0x, t):
    t = 8
    R = v0x * t
    return R

componente_horizontal_velocidade_inicial = 100  
tempo_total_voo = 10  

distancia_horizontal = alcance_horizontal(componente_horizontal_velocidade_inicial, tempo_total_voo)
print("Distância Horizontal entre o Ponto de Lançamento e o Local da Queda:", distancia_horizontal, "metros")

v0x = 100  
v0y = 40   
g = 10    

# Calculando o tempo de voo total
t = (2 * v0y) / g

# Calculando o alcance horizontal
R = v0x * t

print("Tempo de Voo Total:", t, "segundos")
print("Alcance Horizontal:", R, "metros")

def alcance_vertical(v0, g):
    H = (v0 ** 2) / (2 * g)
    return H


velocidade_vertical_inicial = 40  
gravidade = 10 

alcance_vertical = alcance_vertical(velocidade_vertical_inicial, gravidade)
print("Alcance Vertical (Altura Máxima):", alcance_vertical, "metros")

# import math


massa = 0.5  
gravidade = 10  
velocidade_lancamento = 100  
#
velocidade_horizontal = velocidade_lancamento
velocidade_vertical = 0  # Lançamento horizontal

print("Velocidade Inicial:", velocidade_lancamento, "m/s")

def tempo_voo_por_segundo(i):

    i = 800 / 8  
    return i

print(f'Velocidado do objeto é:'  "M a cada segundo.")