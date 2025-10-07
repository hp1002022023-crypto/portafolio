import streamlit as st

# 🔹 CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Portafolio - Elmer & Luis",
    page_icon="💻",
    layout="wide"
)

# 🔹 ESTILO LIMPIO EN TONOS AZULES
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom right, #e6f0ff, #f7faff);
    color: #0d1b2a;
    font-family: 'Poppins', sans-serif;
}

/* 🔹 Eliminar padding innecesario */
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
    background-color: #0d47a1;
    color: white;
    position: sticky;
    top: 0;
    z-index: 999;
}
nav h1 {
    font-size: 1.3rem;
    color: #fff;
    margin: 0;
}
nav a {
    color: #e3f2fd;
    text-decoration: none;
    margin-left: 2rem;
    font-weight: 500;
    transition: 0.3s;
}
nav a:hover {
    color: #bbdefb;
}

/* 🔹 Sección principal (Hero) */
.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 5rem 8rem;
    background-color: #ffffffcc;
    border-radius: 12px;
    margin: 3rem auto;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}
.hero-text {
    flex: 1;
}
.hero-text h2 {
    font-size: 2.5rem;
    color: #0d47a1;
}
.hero-text p {
    margin-top: 1rem;
    color: #333;
    font-size: 1.1rem;
    max-width: 600px;
}
.hero-buttons {
    margin-top: 2rem;
}
.hero-buttons a {
    background-color: #0d47a1;
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    margin-right: 1rem;
    transition: 0.3s;
}
.hero-buttons a:hover {
    background-color: #1565c0;
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
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.project h4 {
    color: #0d47a1;
    margin-bottom: 0.5rem;
}
.project p {
    color: #333;
    font-size: 0.95rem;
}
.project a {
    display: inline-block;
    margin-top: 0.8rem;
    background-color: #0d47a1;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-weight: 600;
    text-decoration: none;
}
.project a:hover {
    background-color: #1565c0;
}

/* 🔹 Footer */
footer {
    background-color: #0d47a1;
    text-align: center;
    padding: 2rem;
    color: #e3f2fd;
    font-size: 0.9rem;
    border-top: 3px solid #bbdefb;
}
</style>
""", unsafe_allow_html=True)

# 🔹 NAVBAR
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

# 🔹 HERO
st.markdown("""
<div class="hero" id="inicio">
  <div class="hero-text">
    <h2>Portafolio Digital de Elmer & Luis</h2>
    <p>Un espacio donde compartimos nuestros proyectos, aprendizajes y experiencias en el desarrollo de software y sistemas inteligentes. Inspirados en la innovación educativa y tecnológica.</p>
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
  <p><strong>Elmer:</strong> <a href="mailto:elmerhernandez@correo.com" style="color:#0d47a1;">elmerhernandez@correo.com</a></p>
  <p><strong>Luis:</strong> <a href="mailto:luisLopez@correo.com" style="color:#0d47a1;">luisLopez@correo.com</a></p>
</div>
""", unsafe_allow_html=True)

# 🔹 FOOTER
st.markdown("""
<footer>
  © 2025 Elmer Hernandez & Luis Lopez | Portafolio Educativo Digital
</footer>
""", unsafe_allow_html=True)
