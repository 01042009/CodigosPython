import time
import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Conteo regresivo ---
segundos = 10
while segundos > 0:
    clear()
    print(f"Despegue en {segundos}...")
    time.sleep(1)
    segundos -= 1

# --- Definición del cohete ---
rocket = [
    "   /^\\   ",
    "   |-|   ",
    "  /___\\  ",
    "  |   |  ",
    "  |NSS|  ",
    " /|___|\\ ",
    "   / \\   ",
]

# --- Despegue: cohete sube una vez ---
height = 15
for step in range(height):
    clear()
    print("\n" * (height - step))
    for line in rocket:
        print(line)
    print("   ***   ")
    print("   ***   ")
    time.sleep(0.2)

# Mensaje de despegue
clear()


# --- Animación de cielo estrellado con cohete fijo en el centro ---
width, sky_height = 60, 20   # tamaño del "cielo"
iterations = 50              # cuadros de parpadeo

rocket_h = len(rocket)
rocket_w = len(rocket[0])
pad_x = (width - rocket_w) // 2
pad_y = (sky_height - rocket_h) // 2

for _ in range(iterations):
    clear()
    # Generar cielo vacío
    sky = []
    for _ in range(sky_height):
        row = []
        for _ in range(width):
            if random.random() < 0.05:
                row.append(random.choice(['*', '+', '·']))
            else:
                row.append(' ')
        sky.append(row)

    # Superponer el cohete en el centro
    for i, line in enumerate(rocket):
        for j, ch in enumerate(line):
            sky[pad_y + i][pad_x + j] = ch

    # Imprimir todo el cielo con cohete
    for row in sky:
        print("".join(row))

    time.sleep(0.3)

# --- Pantalla final ---
clear()
# Generar último cielo
sky = []
for _ in range(sky_height):
    row = []
    for _ in range(width):
        if random.random() < 0.05:
            row.append(random.choice(['*', '+', '·']))
        else:
            row.append(' ')
    sky.append(row)
# Superponer cohete
for i, line in enumerate(rocket):
    for j, ch in enumerate(line):
        sky[pad_y + i][pad_x + j] = ch

for row in sky:
    print("".join(row))

print("\n     Que las estrellas te acompañen… ✨")