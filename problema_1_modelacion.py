
!pip install streamlit

import streamlit as st
import random

def problem_modelacion_streamlit():
  #Definimos nuestras variables
  #Selección de nombres
  nombres_1 = ["Juan", "Maria", "Pablo", "Rosa", "Jose", "Sofia", "Alejandro", "Valentina"]
  nom1 = random.choice(nombres_1)
  nombres_2 = ["Diego", "Fernanda", "Rivelino", "Nathalia", "Luis", "Karla", "Gael"]
  nom2 = random.choice(nombres_2)
  #Selección de relación entre el dinero de cada persona
  op = ["la mitad", "el doble", "el triple"]
  rel = random.choice(op)

  # Selección de cantidades
  if rel == "la mitad":
    a = 3*(random.randint(25, 35))
    b = 3*(random.randint(5, 8))
    c = (a + b)
    e = int(c/3)
    d = int(2*e)
    f = int(e-b)
  elif rel == "el doble":
    a = 3*(random.randint(25, 35))
    b = 3*(random.randint(5, 8))
    c = (a + b)
    d = int(c/3)
    e = int(2*d)
    f = int(e-b)
  elif rel == "el triple":
    a = 4*(random.randint(20, 30))
    b = 4*(random.randint(5, 8))
    c = (a + b)
    d = int(c/4)
    e = int(3*d)
    f = int(e-b)

  # Planteamiento del problema
  st.write(f"{nom1} y {nom2} tienen ${a} pesos en conjunto; si al dinero de {nom2} se le sumaran ${b} pesos, entonces {nom2} tendría {rel} del dinero de {nom1}.")
  st.write(f"¿Cuánto dinero tienen {nom1} y {nom2} respectivamente?")

  # Planteamos las opciones de respuesta
  # Numeros en los que van a variar las respuestas
  r1 = random.choice([i for i in range(0,4)])
  r2 = random.choice([i for i in range(0,4) if i not in [r1]])
  r3 = random.choice([i for i in range(0,4) if i not in [r1, r2]])
  r4 = random.choice([i for i in range(0,4) if i not in [r1, r2, r3]])

  options = [
      f"{nom1} tiene ${d - r1} pesos y {nom2} tiene ${f + r1} pesos.",
      f"{nom1} tiene ${d + r2} pesos y {nom2} tiene ${f - r2} pesos.",
      f"{nom1} tiene ${d - r3} pesos y {nom2} tiene ${f + r3} pesos.",
      f"{nom1} tiene ${d + r4} pesos y {nom2} tiene ${f - r4} pesos.",
      "Ninguna de las anteriores."
  ]
  st.write("\nOpciones de respuesta:")

  answer = st.radio("Elige tu respuesta:", options)

  # Definimos condiciones para dar la solución
  if st.button("Verificar Respuesta"):
    correct = False
    if answer == options[0] and r1 == 0:
      correct = True
    elif answer == options[1] and r2 == 0:
      correct = True
    elif answer == options[2] and r3 == 0:
      correct = True
    elif answer == options[3] and r4 == 0:
      correct = True
    elif answer == options[4] and all([r1 != 0, r2 != 0, r3 != 0, r4 != 0]):
        correct = True


    if correct:
      st.success("¡Correcto!")
    else:
      st.error("Incorrecto.")

  if st.button("Mostrar Solución"):
    st.write("\nSolución:")
    st.write(f"Si {nom2} tuviera ${b} pesos más, el dinero de {nom1} y {nom2} sumarian ${c} pesos en total.")

    # Soluciones especificas dependiendo el problema
    if rel == "la mitad":
      st.write(f"El dinero se debe dividir en tres partes iguales de donde {nom1} tendrá dos de ellas y {nom2} la otra.")
    elif rel == "el doble":
      st.write(f"El dinero se debe dividir en tres partes iguales de donde {nom1} tendrá una de ellas y {nom2} las otras dos.")
    elif rel == "el triple":
      st.write(f"El dinero se debe dividir en cuatro partes iguales de donde {nom1} tendrá una de ellas y {nom2} las otras tres.")

    st.write(f"Dejando así que {nom1} tiene ${d} pesos y {nom2} tiene ${e} pesos.")
    st.write(f"Sin embargo, esto es dentro de la situación hipotetica de que {nom2} tiene ${b} pesos más, por lo que en realidad {nom2} tiene ${f} pesos.")
    st.write(f"\n\nRespuesta: {nom1} tiene ${d} pesos y {nom2} tiene ${f} pesos.")

st.title("Generador de Problemas de Modelación")
problem_modelacion_streamlit()
