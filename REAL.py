import turtle

# Función para dibujar

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
    if panel == 0:
        dibujar_dibujo_panel_1()
    elif panel == 1:
        dibujar_dibujo_panel_2()
    elif panel == 2:
        dibujar_dibujo_panel_3()
    elif panel == 3:
        dibujar_dibujo_panel_4()
    elif panel == 4:
        dibujar_dibujo_panel_5()

# Función para borrar el panel anterior
def borrar_panel():
    pen.clear()

# Funciones para dibujar los dibujos específicos para cada panel
def dibujar_dibujo_panel_1():
    # Dibujar el gato
    t = turtle.Turtle()
    t.speed(2)
    t.color("black")
    centro_x = 0
    centro_y = -100
    t.penup()
    t.goto(centro_x, centro_y -50)
    t.pendown()
    t.begin_fill()
    t.fillcolor("gray")
    t.circle(50) 
    t.end_fill()
    t.penup()
    t.goto(centro_x - 17.5, centro_y + 10)  
    t.pendown()
    t.begin_fill()
    t.fillcolor("white")
    t.circle(10) 
    t.end_fill()
    t.penup()
    t.goto(centro_x + 17.5, centro_y + 10) 
    t.pendown()
    t.begin_fill()
    t.fillcolor("white")
    t.circle(10)  
    t.end_fill()
    t.penup()
    t.goto(centro_x - 17.5, centro_y + 10) 
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.circle(5) 
    t.end_fill()
    t.penup()
    t.goto(centro_x + 17.5, centro_y + 10) 
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.circle(5)  
    t.end_fill()
    t.penup()
    t.goto(centro_x, centro_y - 15) 
    t.pendown()
    t.begin_fill()
    t.fillcolor("pink")
    t.circle(5)  
    t.end_fill()
    t.penup()
    t.goto(centro_x, centro_y - 15) 
    t.pendown()
    t.setheading(240)
    t.forward(25)  
    t.penup()
    t.goto(centro_x, centro_y - 15)  
    t.pendown()
    t.setheading(300)
    t.forward(25)  

def dibujar_dibujo_panel_2():
    # Dibujar árbol
    def dibujar_arbol(t, longitud, nivel):
        if nivel == 0:
            return
        t.forward(longitud)
        t.left(45)
        dibujar_arbol(t, longitud * 0.6, nivel - 1)
        t.right(90)
        dibujar_arbol(t, longitud * 0.6, nivel - 1)
        t.left(45)
        t.backward(longitud)

    t = turtle.Turtle()
    t.speed(0)  
    t.color("green")  
    t.penup()
    t.goto(-150, -100) 
    t.pendown()
    t.setheading(90)
    t.width(10)  
    t.backward(25)  
    t.width(3)  
    dibujar_arbol(t, 50, 7)  
    t.hideturtle()

def dibujar_dibujo_panel_3():
    # Dibujar casa
    t = turtle.Turtle()
    t.speed(2)
    t.color("black")
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    t.begin_fill()
    t.fillcolor("lightblue")  
    for _ in range(4):
        t.forward(100)  
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-50, 50)
    t.pendown()
    t.begin_fill()
    t.fillcolor("brown")  
    t.goto(0, 100) 
    t.goto(50, 50) 
    t.goto(-50, 50)  
    t.end_fill()
    t.penup()
    t.goto(-20, -50)
    t.pendown()
    t.begin_fill()
    t.fillcolor("red")  
    for _ in range(2):
        t.forward(40)  
        t.left(90)
        t.forward(70)  
        t.left(90)
    t.end_fill()
    t.hideturtle()

def dibujar_dibujo_panel_4():
    # Dibujar conejo
    t = turtle.Turtle()
    t.speed(2)
    t.color("black")
    t.penup()
    t.goto(-75, -100)  
    t.pendown()
    t.begin_fill()
    t.fillcolor("gray")
    t.circle(50) 
    t.end_fill()
    t.penup()
    t.goto(-92.5, -40) 
    t.pendown()
    t.begin_fill()
    t.fillcolor("white")
    t.circle(10)  
    t.end_fill()
    t.penup()
    t.goto(-57.5, -40)  
    t.pendown()
    t.begin_fill()
    t.fillcolor("white")
    t.circle(10)  
    t.end_fill()
    t.penup()
    t.goto(-92.5, -40)  
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.circle(5)  
    t.end_fill()
    t.penup()
    t.goto(-57.5, -40)  
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.circle(5)  
    t.end_fill()
    t.penup()
    t.goto(-75, -65)  
    t.pendown()
    t.begin_fill()
    t.fillcolor("pink")
    t.circle(5)  
    t.end_fill()
    t.penup()
    t.goto(-75, -65) 
    t.pendown()
    t.setheading(240)
    t.forward(25)  
    t.penup()
    t.goto(-75, -65) 
    t.pendown()
    t.setheading(300)
    t.forward(25)  

def dibujar_dibujo_panel_5():
    # Dibujar sol
    t = turtle.Turtle()
    t.speed(2)
    t.color("yellow")
    t.penup()
    t.goto(0, 200) 
    t.pendown()
    t.begin_fill() 
    for _ in range(20):  
        t.forward(100)  
        t.backward(100) 
        t.right(10)  
    t.end_fill()  

# Solicitar el nombre del usuario
user_name = turtle.textinput("Nombre", "¿Cuál es tu nombre?")
# Solicitar el color favorito del usuario
user_color = turtle.textinput("Color Favorito", "¿Cuál es tu color favorito?")
# Solicitar la edad del usuario
user_age = turtle.textinput("Color Favorito", "¿Cuál es tu edad?")

# Lista de narrativas de cada panel
narrativas=[
    "Una soleada mañana, el gato "+user_name+" de "+user_age+" años de edad se despertó con mucha curiosidad.\n Decidió explorar más allá del jardín donde siempre jugaba.",
    "Se adentró en el bosque, profundo, y junto a un árbol descubrió una casa misteriosa.",
    "Dentro de la casa, "+user_name+" encontró una puerta de madera. Sin dudarlo, la abrió\n y se encontró con un mundo mágico lleno de colores, entre ellos su color \nfavorito el "+user_color+" y criaturas sorprendentes.",
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



# Mantener la ventana abierta
window.mainloop()
