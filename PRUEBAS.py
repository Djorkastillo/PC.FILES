#Poyecto No.1
import turtle

# Función para dibujar

def dibujar_flor(t, colores):
    t.speed(0)  # Configurar la velocidad de dibujo
    for _ in range(2):  # Repetir dos veces para dibujar los pétalos
        for color in colores:  # Iterar sobre los colores de los pétalos
            t.color(color)
            t.begin_fill()  # Comenzar el relleno del pétalo
            t.circle(50, 180)  # Dibujar un arco de círculo
            t.left(90)  # Girar hacia la izquierda
            t.circle(50, 180)  # Dibujar otro arco de círculo
            t.end_fill()  # Finalizar el relleno del pétalo
            t.left(90)  # Girar hacia la izquierda para la siguiente iteración
        t.right(90)  # Girar hacia la derecha para la siguiente fila de pétalos
        t.penup()  # Levantar el lápiz
        t.forward(100)  # Moverse hacia adelante para la siguiente flor
        t.pendown()  # Bajar el lápiz
        t.right(180)  # Girar hacia la derecha para la siguiente fila de flores


# Función para dibujar el margen con título centrado
def draw_centered_margin_with_title(title):
    # Dibujar el margen
    pen.penup()
    pen.goto(-350, 200)
    pen.pendown()
    pen.pensize(3)
    pen.color("black")
    for _ in range(2):
        pen.forward(700)
        pen.right(90)
        pen.forward(400)
        pen.right(90)
    
    # Dibujar el título centrado
    pen.penup()
    pen.goto(0, 230)
    pen.pendown()
    pen.write(title, align="center", font=("Arial", 20, "bold"))

# Función para dibujar el texto centrado
def draw_centered_text(text):
    pen.penup()
    pen.goto(8, -270)
    pen.pendown()
    pen.write(text, align="center", font=("Arial", 12, "normal"))

# Función para cambiar al panel anterior
def panel_anterior():
    global panel_actual
    if panel_actual > 0:
        panel_actual -= 1
        dibujar_panel(panel_actual)

# Función para cambiar al siguiente panel
def panel_siguiente():
    global panel_actual
    if panel_actual < len(narrativas) - 1:
        panel_actual += 1
        dibujar_panel(panel_actual)
# Función para dibujar un panel específico
def dibujar_panel(panel):
    borrar_panel()
    draw_centered_margin_with_title(f"Panel {panel + 1}")
    draw_centered_text(narrativas[panel])

# Función para borrar el panel anterior
def borrar_panel():
    pen.clear()

# Solicitar el nombre del usuario
user_name = turtle.textinput("Nombre", "¿Cuál es tu nombre?")
# Solicitar el color favorito del usuario
user_color = turtle.textinput("Color Favorito", "¿Cuál es tu color favorito?")
# Solicitar la edad del usuario
user_age = turtle.textinput("Color Favorito", "¿Cuál es tu edad?")

# Lista de narrativas de cada panel
narrativas=[
        "Una soleada mañana, el gato "+user_name+" de "+user_age+" años de edad se despertó con mucha curiosidad.\n Decidió explorar más allá del jardín donde siempre jugaba.",
    "Se adentró en el bosque, profundo, y junto a un árbol descubrió una cueva misteriosa.",
    "Dentro de la cueva, "+user_name+" encontró una puerta de madera. Sin dudarlo, la abrió\n y se encontró con un mundo mágico lleno de colores, entre ellos su color \nfavorito el "+user_color+" y criaturas sorprendentes.",
    "Exploró cada rincón, haciendo nuevos amigos y aprendiendo lecciones \nvaliosas sobre amistad y valentía.",
    "Al final del día, regresó a casa con una sonrisa en su rostro y muchas historias\n que contar. A partir de ese día, "+user_name+" comprendió que la verdadera aventura\n está en explorar y descubrir cosas nuevas.",
]

# Función para borrar el panel anterior
def borrar_panel():
    pen.clear()
# Configuración de la ventana
window = turtle.Screen()
window.setup(width=800, height=600)
window.title("La Aventura del Gato")

# Configurar las teclas de flecha izquierda y derecha para cambiar de panel
window.listen()
window.onkeypress(panel_anterior, "Left")
window.onkeypress(panel_siguiente, "Right")

# Crear el objeto Turtle
pen = turtle.Turtle()
pen.speed(0)  # Velocidad máxima

# Panel actual
panel_actual = 0

# Dibujar el primer panel
dibujar_panel(panel_actual)

# Dibujar las flores
alex = turtle.Turtle()
alex.penup()
alex.goto(-25, -10)
dibujar_flor(alex, ["red", "orange", "yellow", "purple"])

# Mantener la ventana abierta
window.mainloop()