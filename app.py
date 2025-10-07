import streamlit as st

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Portafolio - Elmer & Luis",
    page_icon="💻",
    layout="wide"
)

# 🔹 ESTILOS CON FONDO PASTEL
st.markdown("""
<style>
body {
    background-color: #e6f2ff;  /* Fondo pastel azul suave */
    color: #1e1e1e;
    font-family: 'Poppins', sans-serif;
}

header, .block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.2rem 3rem;
    background-color: #d6eaff;
    border-bottom: 2px solid #b3d1ff;
    position: sticky;
    top: 0;
    z-index: 999;
}
nav h1 {
    font-size: 1.3rem;
    color: #005f99;
    margin: 0;
}
nav a {
    color: #004466;
    text-decoration: none;
    margin-left: 2rem;
    font-weight: 500;
    transition: color 0.3s ease;
}
nav a:hover {
    color: #0099cc;
}

.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 6rem 8rem;
}
.hero-text {
    flex: 1;
}
.hero-text h2 {
    font-size: 2.5rem;
    color: #00334d;
}
.hero-text p {
    margin-top: 1rem;
    color: #333;
    font-size: 1.2rem;
    max-width: 600px;
}
.hero-buttons {
    margin-top: 2rem;
}
.hero-buttons a {
    background-color: #0099cc;
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    margin-right: 1rem;
    transition: 0.3s;
}
.hero-buttons a:hover {
    background-color: #0077aa;
}

.section {
    padding: 5rem 8rem;
}
.section h3 {
    color: #005f99;
    margin-bottom: 1.5rem;
    font-size: 1.8rem;
}
.project {
    background-color: #f0f8ff;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.project h4 {
    color: #00334d;
    margin-bottom: 0.5rem;
}
.project p {
    color: #333;
    font-size: 0.95rem;
}
.project a {
    display: inline-block;
    margin-top: 0.8rem;
    background-color: #0099cc;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-weight: 600;
    text-decoration: none;
}
.project a:hover {
    background-color: #0077aa;
}

footer {
    background-color: #d6eaff;
    text-align: center;
    padding: 2rem;
    border-top: 2px solid #b3d1ff;
    color: #004466;
}
</style>
""", unsafe_allow_html=True)

# 🔹 NAVEGACIÓN
st.markdown("""
<nav>
  <h1>Portafolio</h1>
  <div>
    <a href="#inicio">Inicio</a>
    <a href="#proyectos">Proyectos</a>
    <a href="#contacto">Contacto</a>
  </div>
</nav>
""", unsafe_allow_html=True)

# 🔹 SECCIÓN HERO
st.markdown("""
<div class="hero" id="inicio">
  <div class="hero-text">
    <h2>Desarrolladores con aspiraciones en Sistemas Expertos</h2>
    <p>Enfocados en crear soluciones tecnológicas modernas e intuitivas que faciliten la vida del usuario. Combinamos conocimiento en desarrollo de software y APIs para construir herramientas eficientes, inteligentes y orientadas al futuro.</p>
    <div class="hero-buttons">
      <a href="#proyectos">Ver proyectos</a>
      <a href="#contacto">Contactar</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# 🔹 SECCIÓN PROYECTOS
st.markdown("""
<div class="section" id="proyectos">
  <h3>🌐 Proyectos</h3>

  <div class="project">
    <h4>Aplicación del Clima</h4>
    <p>Consulta el clima en tiempo real por departamento utilizando una API meteorológica.</p>
    <a href="https://r76cmuruexwpv3rmkmnmrc.streamlit.app/">Ver proyecto</a>
  </div>

  <div class="project">
    <h4>Música según tu Sentimiento</h4>
    <p>Selecciona tu estado de ánimo y descubre canciones relacionadas mediante una API musical.</p>
    <a href="https://app-musica-bxue6qn7avgh2ykdxgbtrq.streamlit.app/">Ver proyecto</a>
  </div>

  <div class="project">
    <h4>Bolsa de Valores</h4>
    <p>Consulta información bursátil en tiempo real, sigue el comportamiento de acciones y visualiza gráficos interactivos mediante una API financiera.</p>
    <a href="https://bolsa-de-valores-db5pbjxa7z22iyjlegpmng.streamlit.app/">Ver proyecto</a>
  </div>
</div>
""", unsafe_allow_html=True)

# 🔹 SECCIÓN CONTACTO
st.markdown("""
<div class="section" id="contacto">
  <h3>📬 Contacto</h3>
  <p>¿Quieres colaborar o conocer más? Escríbenos o visita nuestras redes:</p>
  <p><strong>Correo:</strong> <a href="mailto:elmerhernandez@correo.com" style="color:#0099cc;">elmerhernandez@correo.com</a></p>
  <p><strong>Correo:</strong> <a href="mailto:luisLopez@correo.com" style="color:#0099cc;">luisLopez@correo.com</a></p>
</div>
""", unsafe_allow_html=True)

# 🔹 FOOTER
st.markdown("""
<footer>
  © 2025 Elmer Hernandez & Luis Lopez | Portafolio personal
</footer>
""", unsafe_allow_html=True)
