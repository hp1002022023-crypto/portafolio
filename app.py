import streamlit as st

# 🔹 CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Portafolio - Elmer & Luis",
    page_icon="💻",
    layout="wide"
)

# 🔹 ESTILO CON FONDO CELESTE Y VERDE DEGRADADO
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #a8edea, #fed6e3, #b9fbc0, #a0e7e5);
    background-attachment: fixed;
    color: #083d77;
    font-family: 'Poppins', sans-serif;
}

/* Quitar márgenes */
header, .block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

/* 🔹 Barra de navegación */
nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.2rem 3rem;
    background: rgba(255, 255, 255, 0.8);
    color: #083d77;
    border-bottom: 2px solid #8ad0c1;
    position: sticky;
    top: 0;
    z-index: 999;
    backdrop-filter: blur(10px);
}
nav h1 {
    font-size: 1.4rem;
    font-weight: 700;
    color: #045d56;
}
nav a {
    color: #045d56;
    text-decoration: none;
    margin-left: 2rem;
    font-weight: 500;
    transition: 0.3s;
}
nav a:hover {
    color: #028090;
}

/* 🔹 Hero principal */
.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 5rem 8rem;
    background-color: rgba(255, 255, 255, 0.85);
    border-radius: 16px;
    margin: 3rem auto;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.hero-text h2 {
    font-size: 2.5rem;
    color: #045d56;
}
.hero-text p {
    margin-top: 1rem;
    color: #0b3954;
    font-size: 1.1rem;
    max-width: 600px;
}
.hero-buttons {
    margin-top: 2rem;
}
.hero-buttons a {
    background-color: #00afb9;
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    margin-right: 1rem;
    transition: 0.3s;
}
.hero-buttons a:hover {
    background-color: #007f86;
}

/* 🔹 Secciones */
.section {
    padding: 4rem 8rem;
}
.section h3 {
    color: #045d56;
    margin-bottom: 1.5rem;
    font-size: 1.8rem;
}
.project {
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.project h4 {
    color: #045d56;
    margin-bottom: 0.5rem;
}
.project p {
    color: #0b3954;
    font-size: 0.95rem;
}
.project a {
    display: inline-block;
    margin-top: 0.8rem;
    background-color: #00afb9;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-weight: 600;
    text-decoration: none;
}
.project a:hover {
    background-color: #007f86;
}

/* 🔹 Footer */
footer {
    background-color: rgba(255, 255, 255, 0.8);
    text-align: center;
    padding: 2rem;
    color: #045d56;
    font-size: 0.9rem;
    border-top: 3px solid #8ad0c1;
    backdrop-filter: blur(10px);
}
</style>
""", unsafe_allow_html=True)

# 🔹 NAVBAR
st.markdown("""
<nav>
  <h1>Portafolio Digital</h1>
  <div>
    <a href="#inicio">Inicio</a>
    <a href="#proyectos">Proyectos</a>
    <a href="#contacto">Contacto</a>
  </div>
</nav>
""", unsafe_allow_html=True)

# 🔹 HERO
st.markdown("""
<div class="hero" id="inicio">
  <div class="hero-text">
    <h2>Portafolio de Elmer & Luis</h2>
    <p>Explora nuestros proyectos y experiencias en el desarrollo de software, sistemas expertos y aplicaciones web. Buscamos unir tecnología, innovación y creatividad para mejorar el aprendizaje y la productividad.</p>
    <div class="hero-buttons">
      <a href="#proyectos">Ver proyectos</a>
      <a href="#contacto">Contacto</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# 🔹 PROYECTOS
st.markdown("""
<div class="section" id="proyectos">
  <h3>🌿 Proyectos</h3>

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

# 🔹 CONTACTO
st.markdown("""
<div class="section" id="contacto">
  <h3>📬 Contacto</h3>
  <p>¿Quieres colaborar o conocer más? Escríbenos:</p>
  <p><strong>Elmer:</strong> <a href="mailto:elmerhernandez@correo.com" style="color:#007f86;">elmerhernandez@correo.com</a></p>
  <p><strong>Luis:</strong> <a href="mailto:luisLopez@correo.com" style="color:#007f86;">luisLopez@correo.com</a></p>
</div>
""", unsafe_allow_html=True)

# 🔹 FOOTER
st.markdown("""
<footer>
  © 2025 Elmer Hernandez & Luis Lopez | Portafolio Educativo Digital
</footer>
""", unsafe_allow_html=True)
