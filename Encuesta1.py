from tkinter import Tk, Label, Frame, BOTH, Button, Radiobutton, TOP, StringVar
from tkinter import ttk

BASE = 480
ALTURA = 400


def respuestas():
    resultado = (
        respuestapregunta1.get()
        + respuestapregunta2.get()
        + respuestapregunta3.get()
        + respuestapregunta3.get()
        + respuestapregunta4.get()
        + respuestapregunta5.get()
        + respuestapregunta6.get()
        + respuestapregunta7.get()
        + respuestapregunta8.get()
        + respuestapregunta9.get()
        + respuestapregunta10.get()
    )


# ----------------------
# VENTANA PRINCIPAL
# ----------------------
ventana_principal = Tk()
ventana_principal.title("Cuestionario multiple")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="gray")
ventana_principal.geometry("600x600")

# ----------------------
# FRAME RESPUESTAS
# ----------------------
frame_respuestas = Frame(ventana_principal)
frame_respuestas.config(bg="white", width=480, height=400)
frame_respuestas.pack(fill=BOTH, padx=10, pady=10)

# ----------------------
# CASILLAS DE RESPUESTA
# ----------------------
respuestapregunta1 = StringVar()

respuesta11 = Radiobutton(
    frame_respuestas, text="A", variable=respuestapregunta1, value=0
)
respuesta11.grid(row=1, column=1)
respuesta21 = Radiobutton(
    frame_respuestas, text="B", variable=respuestapregunta1, value=0
)
respuesta21.grid(row=1, column=2)
respuesta31 = Radiobutton(
    frame_respuestas, text="C", variable=respuestapregunta1, value=0
)
respuesta31.grid(row=1, column=3)
respuesta41 = Radiobutton(
    frame_respuestas, text="D", variable=respuestapregunta1, value=1
)
respuesta41.grid(row=1, column=4)
respuesta51 = Radiobutton(
    frame_respuestas, text="E", variable=respuestapregunta1, value=0
)
respuesta51.grid(row=1, column=5)

respuestapregunta2 = StringVar()

respuesta12 = Radiobutton(
    frame_respuestas, text="A", variable=respuestapregunta2, value=0
)
respuesta12.grid(row=2, column=1)
respuesta22 = Radiobutton(
    frame_respuestas, text="B", variable=respuestapregunta2, value=1
)
respuesta22.grid(row=2, column=2)
respuesta32 = Radiobutton(
    frame_respuestas, text="C", variable=respuestapregunta2, value=0
)
respuesta32.grid(row=2, column=3)
respuesta42 = Radiobutton(
    frame_respuestas, text="D", variable=respuestapregunta2, value=0
)
respuesta42.grid(row=2, column=4)
respuesta52 = Radiobutton(
    frame_respuestas, text="E", variable=respuestapregunta2, value=0
)
respuesta52.grid(row=2, column=5)

respuestapregunta3 = StringVar()

respuesta13 = Radiobutton(
    frame_respuestas, text="A", variable=respuestapregunta3, value=0
)
respuesta13.grid(row=3, column=1)
respuesta23 = Radiobutton(
    frame_respuestas, text="B", variable=respuestapregunta3, value=0
)
respuesta23.grid(row=3, column=2)
respuesta33 = Radiobutton(
    frame_respuestas, text="C", variable=respuestapregunta3, value=0
)
respuesta33.grid(row=3, column=3)
respuesta43 = Radiobutton(
    frame_respuestas, text="D", variable=respuestapregunta3, value=1
)
respuesta43.grid(row=3, column=4)
respuesta53 = Radiobutton(
    frame_respuestas, text="E", variable=respuestapregunta3, value=0
)
respuesta53.grid(row=3, column=5)

respuestapregunta4 = StringVar()

respuesta14 = Radiobutton(
    frame_respuestas, text="A", variable=respuestapregunta4, value=0
)
respuesta14.grid(row=4, column=1)
respuesta24 = Radiobutton(
    frame_respuestas, text="B", variable=respuestapregunta4, value=0
)
respuesta24.grid(row=4, column=2)
respuesta34 = Radiobutton(
    frame_respuestas, text="C", variable=respuestapregunta4, value=1
)
respuesta34.grid(row=4, column=3)
respuesta44 = Radiobutton(
    frame_respuestas, text="D", variable=respuestapregunta4, value=0
)
respuesta44.grid(row=4, column=4)
respuesta54 = Radiobutton(
    frame_respuestas, text="E", variable=respuestapregunta4, value=0
)
respuesta54.grid(row=4, column=5)

respuestapregunta5 = StringVar()

respuesta15 = Radiobutton(
    frame_respuestas, text="A", variable=respuestapregunta5, value=0
)
respuesta15.grid(row=5, column=1)
respuesta25 = Radiobutton(
    frame_respuestas, text="B", variable=respuestapregunta5, value=0
)
respuesta25.grid(row=5, column=2)
respuesta35 = Radiobutton(
    frame_respuestas, text="C", variable=respuestapregunta5, value=1
)
respuesta35.grid(row=5, column=3)
respuesta45 = Radiobutton(
    frame_respuestas, text="D", variable=respuestapregunta5, value=0
)
respuesta45.grid(row=5, column=4)
respuesta55 = Radiobutton(
    frame_respuestas, text="E", variable=respuestapregunta5, value=0
)
respuesta55.grid(row=5, column=5)

respuestapregunta6 = StringVar()

respuesta16 = Radiobutton(
    frame_respuestas, text="A", variable=respuestapregunta6, value=0
)
respuesta16.grid(row=6, column=1)
respuesta26 = Radiobutton(
    frame_respuestas, text="B", variable=respuestapregunta6, value=0
)
respuesta26.grid(row=6, column=2)
respuesta36 = Radiobutton(
    frame_respuestas, text="C", variable=respuestapregunta6, value=0
)
respuesta36.grid(row=6, column=3)
respuesta46 = Radiobutton(
    frame_respuestas, text="D", variable=respuestapregunta6, value=1
)
respuesta46.grid(row=6, column=4)
respuesta56 = Radiobutton(
    frame_respuestas, text="E", variable=respuestapregunta6, value=0
)
respuesta56.grid(row=6, column=5)

respuestapregunta7 = StringVar()

respuesta17 = Radiobutton(
    frame_respuestas, text="A", variable=respuestapregunta7, value=1
)
respuesta17.grid(row=7, column=1)
respuesta27 = Radiobutton(
    frame_respuestas, text="B", variable=respuestapregunta7, value=0
)
respuesta27.grid(row=7, column=2)
respuesta37 = Radiobutton(
    frame_respuestas, text="C", variable=respuestapregunta7, value=0
)
respuesta37.grid(row=7, column=3)
respuesta47 = Radiobutton(
    frame_respuestas, text="D", variable=respuestapregunta7, value=0
)
respuesta47.grid(row=7, column=4)
respuesta57 = Radiobutton(
    frame_respuestas, text="E", variable=respuestapregunta7, value=0
)
respuesta57.grid(row=7, column=5)

respuestapregunta8 = StringVar()

respuesta18 = Radiobutton(
    frame_respuestas, text="A", variable=respuestapregunta8, value=0
)
respuesta18.grid(row=8, column=1)
respuesta28 = Radiobutton(
    frame_respuestas, text="B", variable=respuestapregunta8, value=0
)
respuesta28.grid(row=8, column=2)
respuesta38 = Radiobutton(
    frame_respuestas, text="C", variable=respuestapregunta8, value=0
)
respuesta38.grid(row=8, column=3)
respuesta48 = Radiobutton(
    frame_respuestas, text="D", variable=respuestapregunta8, value=0
)
respuesta48.grid(row=8, column=4)
respuesta58 = Radiobutton(
    frame_respuestas, text="E", variable=respuestapregunta8, value=1
)
respuesta58.grid(row=8, column=5)

respuestapregunta9 = StringVar()

respuesta19 = Radiobutton(
    frame_respuestas, text="A", variable=respuestapregunta9, value=1
)
respuesta19.grid(row=9, column=1)
respuesta29 = Radiobutton(
    frame_respuestas, text="B", variable=respuestapregunta9, value=0
)
respuesta29.grid(row=9, column=2)
respuesta39 = Radiobutton(
    frame_respuestas, text="C", variable=respuestapregunta9, value=0
)
respuesta39.grid(row=9, column=3)
respuesta49 = Radiobutton(
    frame_respuestas, text="D", variable=respuestapregunta9, value=0
)
respuesta49.grid(row=9, column=4)
respuesta59 = Radiobutton(
    frame_respuestas, text="E", variable=respuestapregunta9, value=0
)
respuesta59.grid(row=9, column=5)

respuestapregunta10 = StringVar()

respuesta110 = Radiobutton(
    frame_respuestas, text="A", variable=respuestapregunta10, value=0
)
respuesta110.grid(row=10, column=1)
respuesta210 = Radiobutton(
    frame_respuestas, text="B", variable=respuestapregunta10, value=0
)
respuesta210.grid(row=10, column=2)
respuesta310 = Radiobutton(
    frame_respuestas, text="C", variable=respuestapregunta10, value=0
)
respuesta310.grid(row=10, column=3)
respuesta410 = Radiobutton(
    frame_respuestas, text="D", variable=respuestapregunta10, value=1
)
respuesta410.grid(row=10, column=4)
respuesta510 = Radiobutton(
    frame_respuestas, text="E", variable=respuestapregunta10, value=0
)
respuesta510.grid(row=10, column=5)
# ----------------------
# BOTÓN
# ----------------------
boton = Button(
    text="Calcular respuestas correctas",
    padx=10,
    fg="white",
    bg="grey",
    command=respuestas,
)
boton.pack(side="bottom", padx=10, pady=10)

# ----------------------
# RECOLECTAR DATOS
# ----------------------

ventana_principal.mainloop()