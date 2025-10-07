import streamlit as st

# 🔹 CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Portafolio - Elmer & Luis",
    page_icon="💻",
    layout="wide"
)

# 🔹 ESTILO CLARO AZUL PASTEL
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom right, #f4f9ff, #e8f0fe);
    color: #1a237e;
    font-family: 'Poppins', sans-serif;
}

/* 🔹 Quitar márgenes */
header, .block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

/* 🔹 Barra de navegación clara */
nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.2rem 3rem;
    background-color: #bbdefb;
    color: #0d47a1;
    border-bottom: 2px solid #90caf9;
    position: sticky;
    top: 0;
    z-index: 999;
}
nav h1 {
    font-size: 1.4rem;
    font-weight: 700;
    color: #0d47a1;
}
nav a {
    color: #0d47a1;
    text-decoration: none;
    margin-left: 2rem;
    font-weight: 500;
    transition: 0.3s;
}
nav a:hover {
    color: #1565c0;
}

/* 🔹 Sección principal */
.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 5rem 8rem;
    background-color: white;
    border-radius: 16px;
    margin: 3rem auto;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.hero-text h2 {
    font-size: 2.5rem;
    color: #0d47a1;
}
.hero-text p {
    margin-top: 1rem;
    color: #1a237e;
    font-size: 1.1rem;
    max-width: 600px;
}
.hero-buttons {
    margin-top: 2rem;
}
.hero-buttons a {
    background-color: #42a5f5;
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    margin-right: 1rem;
    transition: 0.3s;
}
.hero-buttons a:hover {
    background-color: #1e88e5;
}

/* 🔹 Secciones */
.section {
    padding: 4rem 8rem;
}
.section h3 {
    color: #0d47a1;
    margin-bottom: 1.5rem;
    font-size: 1.8rem;
}
.project {
    background-color: white;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.project h4 {
    color: #0d47a1;
    margin-bottom: 0.5rem;
}
.project p {
    color: #1a237e;
    font-size: 0.95rem;
}
.project a {
    display: inline-block;
    margin-top: 0.8rem;
    background-color: #42a5f5;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-weight: 600;
    text-decoration: none;
}
.project a:hover {
    background-color: #1e88e5;
}

/* 🔹 Footer claro */
footer {
    background-color: #bbdefb;
    text-align: center;
    padding: 2rem;
    color: #0d47a1;
    font-size: 0.9rem;
    border-top: 3px solid #90caf9;
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
    <p>Explora nuestros proyectos y experiencias en el desarrollo de software, sistemas expertos y aplicaciones web. Nuestro objetivo es combinar tecnología y creatividad para ofrecer soluciones modernas y accesibles.</p>
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

# 🔹 CONTACTO
st.markdown("""
<div class="section" id="contacto">
  <h3>📬 Contacto</h3>
  <p>¿Quieres colaborar o conocer más? Escríbenos:</p>
  <p><strong>Elmer:</strong> <a href="mailto:elmerhernandez@correo.com" style="color:#1e88e5;">elmerhernandez@correo.com</a></p>
  <p><strong>Luis:</strong> <a href="mailto:luisLopez@correo.com" style="color:#1e88e5;">luisLopez@correo.com</a></p>
</div>
""", unsafe_allow_html=True)

# 🔹 FOOTER
st.markdown("""
<footer>
  © 2025 Elmer Hernandez & Luis Lopez | Portafolio Digital
</footer>
""", unsafe_allow_html=True)
