import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de página
st.set_page_config(
    page_title="Graficador de Funciones Polinómicas",
    page_icon="📈",
    layout="wide"
)

# Estilos CSS
st.markdown("""
<style>
.main-title{
    text-align:center;
    color:#1E88E5;
    font-size:40px;
    font-weight:bold;
}
.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<p class="main-title">📈 Graficador de Funciones Polinómicas</p>',
            unsafe_allow_html=True)

st.markdown('<p class="subtitle">Visualización interactiva de funciones polinómicas mediante sliders</p>',
            unsafe_allow_html=True)

st.divider()

# Sidebar
st.sidebar.header("⚙️ Configuración")

grado = st.sidebar.slider(
    "Seleccionar grado del polinomio",
    min_value=1,
    max_value=5,
    value=3
)

st.sidebar.subheader("Coeficientes")

coeficientes = []

for i in range(grado, -1, -1):
    coef = st.sidebar.slider(
        f"Coeficiente x^{i}",
        min_value=-10.0,
        max_value=10.0,
        value=1.0 if i == grado else 0.0,
        step=0.1
    )
    coeficientes.append(coef)

# Crear ecuación
ecuacion = ""

for i, c in enumerate(coeficientes):
    potencia = grado - i

    if c == 0:
        continue

    signo = "+" if c > 0 else ""

    if potencia > 1:
        ecuacion += f"{signo}{c:.1f}x^{potencia} "
    elif potencia == 1:
        ecuacion += f"{signo}{c:.1f}x "
    else:
        ecuacion += f"{signo}{c:.1f}"

if ecuacion.startswith("+"):
    ecuacion = ecuacion[1:]

# Área principal
col1, col2 = st.columns([3, 1])

with col2:
    st.subheader("📌 Función")

    st.latex(f"f(x)={ecuacion}")

    try:
        raices = np.roots(coeficientes)

        st.subheader("🎯 Raíces")

        for r in raices:
            if abs(r.imag) < 1e-6:
                st.write(f"{r.real:.4f}")
            else:
                st.write(f"{r:.4f}")

    except:
        st.warning("No se pueden calcular raíces.")

with col1:

    xmin = st.slider("Valor mínimo de X", -50, 0, -10)
    xmax = st.slider("Valor máximo de X", 0, 50, 10)

    x = np.linspace(xmin, xmax, 1000)
    y = np.polyval(coeficientes, x)

    fig, ax = plt.subplots(figsize=(10,6))

    ax.plot(
        x,
        y,
        linewidth=3,
        label="f(x)"
    )

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    ax.grid(True, linestyle='--', alpha=0.6)

    ax.set_title(
        "Gráfica de la Función Polinómica",
        fontsize=16,
        fontweight='bold'
    )

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    ax.legend()

    st.pyplot(fig)

st.divider()

st.info("""
### Instrucciones
1. Selecciona el grado del polinomio.
2. Ajusta los coeficientes usando los sliders.
3. Observa cómo cambia la gráfica en tiempo real.
4. Consulta las raíces calculadas automáticamente.
""")
