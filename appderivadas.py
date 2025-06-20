import streamlit as st
import sympy as sp

# Variables simbólicas
x = sp.Symbol('x')

# Lista de ejercicios con funciones y explicaciones paso a paso
ejercicios = [
    {
        'funcion': sp.sin(x),
        'respuesta': sp.diff(sp.sin(x), x),
        'pasos': "Paso 1: Identifica la función como sin(x)\nPaso 2: Aplica la regla d/dx[sin(x)] = cos(x)"
    },
    {
        'funcion': x**2,
        'respuesta': sp.diff(x**2, x),
        'pasos': "Paso 1: Es una potencia\nPaso 2: Aplica d/dx[x^n] = n*x^(n-1)\nResultado: 2*x"
    },
    {
        'funcion': sp.exp(x),
        'respuesta': sp.diff(sp.exp(x), x),
        'pasos': "Paso 1: La función es exponencial\nPaso 2: d/dx[e^x] = e^x"
    },
    {
        'funcion': sp.ln(x),
        'respuesta': sp.diff(sp.ln(x), x),
        'pasos': "Paso 1: La función es logarítmica\nPaso 2: d/dx[ln(x)] = 1/x"
    },
    {
        'funcion': x * sp.sin(x),
        'respuesta': sp.diff(x * sp.sin(x), x),
        'pasos': "Paso 1: Identifica como un producto u = x, v = sin(x)\n"
                 "Paso 2: Aplica la regla del producto: u'v + uv'\n"
                 "Paso 3: Derivada de x = 1, derivada de sin(x) = cos(x)\n"
                 "Resultado: sin(x) + x*cos(x)"
    }
]

# Estado actual del ejercicio (usando session_state para conservarlo entre interacciones)
if 'indice' not in st.session_state:
    st.session_state.indice = 0
if 'mostrar_pasos' not in st.session_state:
    st.session_state.mostrar_pasos = False

st.title("🧠 Practica Interactiva: Derivadas con Streamlit")

# Mostrar el ejercicio actual
ej = ejercicios[st.session_state.indice]
st.subheader(f"📝 Ejercicio {st.session_state.indice + 1} de {len(ejercicios)}")
st.latex(f"f(x) = {sp.latex(ej['funcion'])}")

# Entrada del usuario
respuesta_usuario = st.text_input("Escribe la derivada de f(x):")

if st.button("Verificar"):
    try:
        derivada_usuario = sp.sympify(respuesta_usuario)
        if sp.simplify(derivada_usuario - ej['respuesta']) == 0:
            st.success("✅ ¡Correcto!")
        else:
            st.error("❌ Incorrecto. Intenta de nuevo o haz clic en 'Ver solución paso a paso'.")
    except Exception as e:
        st.warning(f"⚠️ Error al interpretar tu derivada: {e}")

if st.button("Ver solución paso a paso"):
    st.session_state.mostrar_pasos = True

if st.session_state.mostrar_pasos:
    st.info(f"📘 Pasos para derivar:\n\n{ej['pasos']}")

if st.button("Siguiente ejercicio"):
    if st.session_state.indice < len(ejercicios) - 1:
        st.session_state.indice += 1
        st.session_state.mostrar_pasos = False
        st.experimental_rerun()
    else:
        st.balloons()
        st.success("🎉 ¡Has completado todos los ejercicios!")