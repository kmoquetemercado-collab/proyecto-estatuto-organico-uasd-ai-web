# 🎓 Chatbot UASD - Estatuto Orgánico

## 📋 Descripción del Proyecto

Aplicación web inteligente que utiliza **Inteligencia Artificial** para responder consultas relacionadas con el **Estatuto Orgánico de la Universidad Autónoma de Santo Domingo (UASD)**.

El chatbot permite que usuarios realicen preguntas en lenguaje natural y reciban respuestas claras, coherentes y fundamentadas en el contenido del Estatuto Orgánico de la UASD.

### ✨ Características Principales

- ✅ Interfaz moderna y responsiva (Móvil, Tablet, Desktop)
- ✅ Chatbot interactivo con IA generativa (OpenAI GPT-4o)
- ✅ Base de conocimiento integrada del Estatuto Orgánico
- ✅ 35+ preguntas sugeridas personalizadas
- ✅ Búsqueda semántica de información
- ✅ Historial de conversación
- ✅ Interfaz intuitiva y fácil de usar
- ✅ Manejo robusto de errores

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Node.js & Express.js** - Servidor web
- **OpenAI API** - Inteligencia Artificial y procesamiento de lenguaje natural
- **CORS** - Control de acceso entre dominios
- **Dotenv** - Gestión de variables de entorno

### Frontend
- **React 18** - Framework UI
- **Vite** - Empaquetador y servidor de desarrollo (rápido)
- **CSS3** - Estilos modernos y responsive
- **Axios** - Cliente HTTP

---

## 📁 Estructura del Proyecto

```
proyecto-estatuto-organico-uasd-ai-web/
├── server.js                           # Entrada principal del servidor
├── package.json                        # Dependencias del backend
├── .env.example                        # Variables de entorno (ejemplo)
├── .gitignore                          # Archivos a ignorar en Git
├── README.md                           # Este archivo
├── QUICK_START.md                      # Guía rápida
├── TECHNICAL_DOCUMENTATION.md          # Documentación técnica
│
├── middleware/
│   └── errorHandler.js                # Manejo centralizado de errores
│
├── utils/
│   ├── openaiClient.js                # Cliente de OpenAI con IA
│   ├── estatutoKnowledge.js           # Base de conocimiento
│   └── suggestedQuestions.js          # Preguntas sugeridas
│
├── routes/
│   └── chatRoutes.js                  # Rutas de la API
│
├── ESTATUTO-ORGANICO-UASD.pdf         # Documento oficial
│
└── frontend/                           # Aplicación React
    ├── package.json
    ├── vite.config.js
    ├── index.html
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── index.css
        └── components/
            ├── ChatContainer.jsx
            ├── ChatHeader.jsx
            ├── ChatInput.jsx
            ├── MessageList.jsx
            ├── Message.jsx
            └── SuggestedQuestions.jsx
```

---

## 🚀 Inicio Rápido

### Requisitos Previos
- **Node.js** v16+
- Cuenta de OpenAI con API Key
- Git

### Pasos (5 minutos)

```bash
# 1. Clonar
git clone https://github.com/kmoquetemercado-collab/proyecto-estatuto-organico-uasd-ai-web.git
cd proyecto-estatuto-organico-uasd-ai-web

# 2. Crear .env
echo "OPENAI_API_KEY=tu_clave_aqui" > .env
echo "NODE_ENV=development" >> .env
echo "PORT=5000" >> .env
echo "FRONTEND_URL=http://localhost:5173" >> .env

# 3. Instalar dependencias
npm install
cd frontend && npm install && cd ..

# 4. Ejecutar (en 2 terminales)
# Terminal 1:
npm start

# Terminal 2:
cd frontend && npm run dev

# 5. Abrir navegador
# http://localhost:5173
```

📖 **Ver [QUICK_START.md](./QUICK_START.md) para más detalles**

---

## 📚 Documentación

- **[README.md](./README.md)** - Descripción completa del proyecto
- **[QUICK_START.md](./QUICK_START.md)** - Guía rápida de instalación
- **[TECHNICAL_DOCUMENTATION.md](./TECHNICAL_DOCUMENTATION.md)** - Documentación técnica detallada

---

## 📡 API Endpoints

### Chat
```http
POST /api/chat/message
GET  /api/chat/suggestions
POST /api/chat/feedback
GET  /api/chat/health
```

Ver documentación técnica para detalles completos.

---

## 🎨 Características

### 1. Chat Interactivo
- Preguntas en lenguaje natural
- Respuestas contextualizadas
- Historial de conversación

### 2. Preguntas Sugeridas
- 35+ preguntas preelaboradas
- Agrupadas por categoría
- Actualización dinámica

### 3. IA Inteligente
- OpenAI GPT-4o-mini
- Base de conocimiento integrada
- Búsqueda semántica

### 4. Diseño Responsivo
- Mobile-first
- Tema moderno con gradientes
- Animaciones suaves

---

## 🔍 Solución de Problemas

| Problema | Solución |
|----------|----------|
| OPENAI_API_KEY no configurada | Crea `.env` con tu clave |
| Puerto 5000 en uso | Cambia `PORT` en `.env` |
| Módulos no encontrados | Ejecuta `npm install` |
| API no responde | Verifica que backend está corriendo |
| Frontend no conecta | Revisa proxy en `vite.config.js` |

---

## 📝 Preguntas Sugeridas Incluidas

El chatbot tiene **35+ preguntas** en categorías:

- 📖 Información General
- 🏢 Estructura Organizacional
- 👔 Órganos de Gobierno
- 👨‍💼 Rector y Autoridades
- 🏛️ Facultades y Escuelas
- 👨‍🏫 Personal Docente
- 👨‍🎓 Estudiantes
- 🔬 Funciones Sustantivas
- 🤝 Bienestar Universitario
- ⚖️ Régimen Disciplinario
- 💰 Patrimonio

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/nueva-feature`)
3. Commit (`git commit -am 'Agrega feature'`)
4. Push (`git push origin feature/nueva-feature`)
5. Abre Pull Request

---

## 📄 Licencia

MIT License - Ver detalles en LICENSE

---

## 👤 Autor

**Kimberly Moquete Mercado**
- Matrícula: 100573552
- Universidad: UASD
- Asignatura: Laboratorio de Lenguaje de Programación III – Web
- Profesor: Radhames Silverio González

---

## 🔗 Enlaces Útiles

- [Estatuto Orgánico UASD](https://postgrado.uasd.edu.do/wp-content/uploads/2024/06/ESTATUTO-ORGANICO-UASD.pdf)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [React Docs](https://react.dev)
- [Express.js Guide](https://expressjs.com)
- [Node.js Docs](https://nodejs.org)

---

**¡Gracias por usar el Chatbot UASD!** 🎓✨

v1.0.0 • Mayo 2026
