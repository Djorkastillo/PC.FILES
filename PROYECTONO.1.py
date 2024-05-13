#Poyecto No.1
import turtle

# Configuración de la ventana
window = turtle.Screen()
window.setup(width=800, height=600)
window.title("Dibujando Cuentos")

# Creación del objeto Turtle
pen = turtle.Turtle()
pen.speed(0)  # Velocidad máxima

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
    pen.goto(0, 250)
    pen.pendown()
    pen.write(title, align="center", font=("Arial", 20, "bold"))

# Función para dibujar el cuento del Pez Dorado

def LA_AVENTURA_DE_():
    title = "La Aventura De El Gato",user_name
    narrative = ("Una soleada mañana, el gato Whiskers se despertó con mucha curiosidad.\n Decidió explorar más allá del jardín donde siempre jugaba. Se adentró en el bosque, \ndonde encontró un arroyo brillante y cristalino. Siguió el arroyo y descubrió\n una cueva misteriosa. Dentro de la cueva, Whiskers encontró una puerta de madera. \nSin dudarlo, la abrió y se encontró con un mundo mágico lleno de colores\n y criaturas sorprendentes. Exploró cada rincón, haciendo nuevos amigos y \naprendiendo lecciones valiosas sobre amistad y valentía. Al final del \ndía, regresó a casa con una sonrisa en su rostro y muchas historias que contar.\n A partir de ese día, Whiskers comprendió que la verdadera aventura está en explorar \ny descubrir cosas nuevas.")
    draw_centered_margin_with_title(title)
    
     # Dibujar el margen
    pen.penup()
    pen.goto(15, -200)
    pen.pendown()
    pen.write(narrative, align="center", font=("Arial", 12, "italic"))
    draw_centered_margin_with_title(title)

    

# Solicitar el nombre del usuario
user_name = turtle.textinput("Nombre Del Usuario", "¿Cómo te llamas?")
# Solicitar la edad del usuario

user_age = str(turtle.textinput("Edad Del Usuario", "¿Que edad tienes?"))

# Solicitar el color favorito del usuario
user_color = turtle.textinput("Color Favorito Del Usuario", "Entre rojo, azul, amarillo, verde y narajana\n¿Cuál es tu color favorito?")

# Ofrecer las opciones de cuento
story_choice = turtle.numinput("Cuento", f"Hola {user_name}!!! \nEscribe 1 para poder leer\nel mejor cuento del\nMUNDO", minval=1, maxval=3)

# Dibujar el cuento seleccionado
if story_choice == 1:
    LA_AVENTURA_DE_()

# Mantener la ventana abierta
window.mainloop()
