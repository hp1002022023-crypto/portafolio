import streamlit as st

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Portafolio - Elmer & Luis",
    page_icon="💻",
    layout="wide"
)

# 🔹 CSS CON FONDO DESDE GITHUB RAW
st.markdown("""
<style>
body {
    background-color: #0d1117;
    color: #f5f5f5;
    font-family: 'Poppins', sans-serif;

    /* 🔹 Fondo con marca de agua desde GitHub */
    background-image: url('https://raw.githubusercontent.com/hp1002022023-crypto/portafolio/main/imagenes/sistemas-expertos-2.jpeg');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    background-size: 500px;
    opacity: 0.98;
}

/* 🔹 Eliminamos el espacio de padding */
header, .block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

/* 🔹 Estilos de la barra de navegación */
nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.2rem 3rem;
    background-color: #0d1117;
    border-bottom: 1px solid #222;
    position: sticky;
    top: 0;
    z-index: 999;
}
nav h1 {
    font-size: 1.3rem;
    color: #00d4ff;
    margin: 0;
}
nav a {
    color: #cfcfcf;
    text-decoration: none;
    margin-left: 2rem;
    font-weight: 500;
    transition: color 0.3s ease;
}
nav a:hover {
    color: #00d4ff;
}

/* 🔹 Sección principal */
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
    color: white;
}
.hero-text p {
    margin-top: 1rem;
    color: #cfcfcf;
    font-size: 1.2rem;
    max-width: 600px;
}
.hero-buttons {
    margin-top: 2rem;
}
.hero-buttons a {
    background-color: #00d4ff;
    color: #0d1117;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    margin-right: 1rem;
    transition: 0.3s;
}
.hero-buttons a:hover {
    background-color: #00a3cc;
}

/* 🔹 Quitamos la imagen lateral */
.hero-img {
    display: none;
}

/* 🔹 Secciones */
.section {
    padding: 5rem 8rem;
}
.section h3 {
    color: #00d4ff;
    margin-bottom: 1.5rem;
    font-size: 1.8rem;
}
.project {
    background-color: #161b22;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}
.project h4 {
    color: white;
    margin-bottom: 0.5rem;
}
.project p {
    color: #cfcfcf;
    font-size: 0.95rem;
}
.project a {
    display: inline-block;
    margin-top: 0.8rem;
    background-color: #00d4ff;
    color: #0d1117;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-weight: 600;
    text-decoration: none;
}
.project a:hover {
    background-color: #00a3cc;
}

/* 🔹 Footer */
footer {
    background-color: #0d1117;
    text-align: center;
    padding: 2rem;
    border-top: 1px solid #222;
    color: #aaa;
}
</style>
""", unsafe_allow_html=True)

# 🔹 Navegación superior
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

# 🔹 Sección Hero
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
  <div class="hero-img">
    <img src="https://cdn.pixabay.com/photo/2023/03/19/14/16/artificial-intelligence-7861610_1280.jpg" alt="Sistemas Expertos">
  </div>
</div>
""", unsafe_allow_html=True)

# 🔹 Proyectos
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

# 🔹 Contacto
st.markdown("""
<div class="section" id="contacto">
  <h3>📬 Contacto</h3>
  <p>¿Quieres colaborar o conocer más? Escríbenos o visita nuestras redes:</p>
  <p><strong>Correo:</strong> <a href="mailto:elmerhernandez@correo.com" style="color:#00d4ff;">elmerhernandez@correo.com</a></p>
  <p><strong>Correo:</strong> <a href="mailto:luisLopez@correo.com" style="color:#00d4ff;">luisLopez@correo.com</a></p>
</div>
""", unsafe_allow_html=True)

# 🔹 Footer
st.markdown("""
<footer>
  © 2025 Elmer Hernandez & Luis Lopez | Portafolio personal
</footer>
""", unsafe_allow_html=True)
