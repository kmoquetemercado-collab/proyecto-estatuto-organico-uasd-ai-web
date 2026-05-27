# Documentación Técnica - Chatbot UASD

## 📊 Arquitectura del Sistema

### Diagrama General

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENTE (NAVEGADOR)                      │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                  FRONTEND (React)                          │ │
│  │                   Port: 5173                               │ │
│  │                                                             │ │
│  │  ┌─────────────────────────────────────────────────────┐  │ │
│  │  │          Componentes React                          │  │ │
│  │  │  - ChatContainer                                   │  │ │
│  │  │  - ChatHeader                                      │  │ │
│  │  │  - MessageList                                     │  │ │
│  │  │  - Message                                         │  │ │
│  │  │  - ChatInput                                       │  │ │
│  │  │  - SuggestedQuestions                              │  │ │
│  │  └─────────────────────────────────────────────────────┘  │ │
│  │                                                             │ │
│  │  Envía peticiones HTTP (Axios)                             │ │
│  └────────────────────────┬────────────────────────────────────┘ │
└─────────────────────────────┼──────────────────────────────────────┘
                              │
                HTTP GET/POST
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SERVIDOR (Node.js)                         │
│                        Port: 5000                               │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │            Express.js REST API                            │ │
│  │                                                             │ │
│  │  POST /api/chat/message                                   │ │
│  │  GET  /api/chat/suggestions                               │ │
│  │  POST /api/chat/feedback                                  │ │
│  │  GET  /api/chat/health                                    │ │
│  │                                                             │ │
│  └────────────────────────────────────────────────────────────┘ │
│                         │                                        │
│           ┌─────────────┼─────────────┐                         │
│           │             │             │                         │
│           ▼             ▼             ▼                         │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │  Middleware  │ │    Utils     │ │    Routes    │            │
│  │              │ │              │ │              │            │
│  │- CORS        │ │- OpenAI AI   │ │- chatRoutes  │            │
│  │- Error      │ │- Knowledge  │ │              │            │
│  │  Handler    │ │- Questions  │ │              │            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
│                         │                                        │
│           ┌─────────────┴─────────────┐                         │
│           │                           │                         │
│           ▼                           ▼                         │
│  ┌──────────────────────┐   ┌──────────────────────┐           │
│  │   OpenAI API         │   │   Base de Datos      │           │
│  │   (GPT-4o-mini)      │   │   (En Memoria)       │           │
│  │                      │   │                      │           │
│  │ - Procesamiento IA   │   │ - Estatuto Orgánico  │           │
│  │ - Embeddings         │   │ - Preguntas          │           │
│  │ - Generación Resp.   │   │                      │           │
│  └──────────────────────┘   └──────────────────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Flujo de Comunicación

### 1. Envío de Pregunta

```
USUARIO
   │
   ├─→ Escribe pregunta en el input
   │
   └─→ Presiona Enter o clickea el botón
         │
         ▼
    React (App.jsx)
         │
         ├─→ Valida que no esté vacío
         │
         └─→ Envía POST /api/chat/message
               │
               ▼
         Express Server (chatRoutes.js)
               │
               ├─→ Recibe: { question: "..." }
               │
               ├─→ Busca contexto en Knowledge Base
               │
               ├─→ Llama OpenAI API con contexto
               │
               ├─→ Recibe respuesta generada
               │
               └─→ Retorna: { success, question, response }
                     │
                     ▼
              React (ChatContainer.jsx)
                     │
                     ├─→ Agrega mensaje del usuario
                     │
                     ├─→ Agrega mensaje del bot
                     │
                     └─→ Renderiza en MessageList
```

---

## 🔧 Detalles Técnicos

### Frontend Stack

```javascript
// Dependencias Principales
- react: 18.2.0
- react-dom: 18.2.0
- axios: 1.6.2
- vite: 5.0.8

// Estructura de Carpetas
frontend/src/
├── components/       // Componentes React reutilizables
├── App.jsx          // Componente raíz
├── main.jsx         // Entrada a React
├── index.css        // Estilos globales
└── App.css          // Estilos específicos

// Patrones Utilizados
- Componentes funcionales con Hooks
- useState para estado local
- useEffect para efectos secundarios
- useRef para referencias al DOM
- CSS modulares por componente
```

### Backend Stack

```javascript
// Dependencias Principales
- express: 4.18.2
- cors: 2.8.5
- dotenv: 16.3.1
- openai: 4.26.0
- axios: 1.6.2

// Estructura de Carpetas
project/
├── server.js           // Entrada principal
├── middleware/         // Middleware Express
├── utils/             // Utilidades y lógica
├── routes/            // Rutas de API
└── package.json       // Configuración

// Patrones Utilizados
- MVC (Modelo-Vista-Controlador)
- Error handling centralizado
- Middleware reutilizable
- Separación de responsabilidades
```

---

## 💡 Cómo Funciona la IA

### 1. Búsqueda de Contexto

```javascript
// searchInKnowledge() en estatutoKnowledge.js

const lowerQuery = query.toLowerCase();
// Busca palabras clave en la pregunta
// Retorna información relevante del Estatuto
```

### 2. Generación de Respuesta

```javascript
// generateResponse() en openaiClient.js

const completion = await openai.chat.completions.create({
  model: 'gpt-4o-mini',           // Modelo rápido y eficiente
  messages: [
    { role: 'system', content: systemPrompt },  // Contexto del sistema
    { role: 'user', content: userMessage }      // Pregunta + contexto
  ],
  temperature: 0.7,        // Creatividad media
  max_tokens: 1000         // Respuestas concisas
});
```

### 3. System Prompt (Instrucciones del Chatbot)

```
"Eres un asistente experto en el Estatuto Orgánico de la UASD.
Tu tarea es responder preguntas de manera clara y precisa.

Reglas:
1. Responde basándote ÚNICAMENTE en el contexto
2. Si no sabes, indica claramente
3. Sé conciso y claro
4. Usa un tono formal pero amable
5. Cita artículos cuando sea relevante
6. Rechaza preguntas no relacionadas"
```

---

## 📡 Endpoints de la API

### 1. POST /api/chat/message

**Request:**
```json
{
  "question": "¿Cuál es la misión de la UASD?"
}
```

**Response:**
```json
{
  "success": true,
  "question": "¿Cuál es la misión de la UASD?",
  "response": "La misión de la UASD es formar profesionales...",
  "timestamp": "2026-05-27T10:30:00.000Z"
}
```

**Código:**
```javascript
// routes/chatRoutes.js
router.post('/message', async (req, res, next) => {
  const { question } = req.body;
  
  // Validación
  if (!question || question.trim() === '') {
    throw new AppError('Pregunta vacía', 400);
  }
  
  // Búsqueda de contexto
  const context = searchInKnowledge(question);
  
  // Generación de respuesta
  const response = await generateResponse(question, context);
  
  // Retorno
  res.json({ success: true, question, response, timestamp });
});
```

### 2. GET /api/chat/suggestions

**Response:**
```json
{
  "success": true,
  "suggestions": [
    {
      "id": 1,
      "category": "Información General",
      "text": "¿Qué es la Universidad Autónoma de Santo Domingo?"
    },
    // ... más preguntas
  ]
}
```

---

## 🎨 Componentes React

### ChatContainer.jsx (Componente Principal)

```javascript
// Responsabilidades:
- Gestiona el estado de mensajes
- Coordina la comunicación con el backend
- Auto-scroll al final de mensajes
- Manejo de loading y errores

// Hooks utilizados:
- useState: mensajes, sugerencias, loading, error
- useEffect: cargar sugerencias, auto-scroll
- useRef: referencia al final de mensajes
```

### Message.jsx (Componente de Mensaje)

```javascript
// Responsabilidades:
- Renderiza un mensaje individual
- Distingue usuario vs bot vs error
- Formatea timestamps
- Convierte URLs en enlaces

// Props:
- message: { id, type, text, timestamp }
```

### ChatInput.jsx (Campo de Entrada)

```javascript
// Responsabilidades:
- Captura entrada del usuario
- Valida que no esté vacío
- Permite envío con Enter
- Desactiva durante loading

// Callbacks:
- onSendMessage(question)
- loading prop
```

---

## 🚀 Optimizaciones

### Frontend
- **Lazy Loading**: Componentes cargados bajo demanda
- **Memoización**: Evita re-renders innecesarios
- **CSS Optimizado**: Clases reutilizables
- **Responsive Design**: Mobile-first approach

### Backend
- **Caché de Preguntas**: Evita búsquedas repetidas
- **Error Handling**: Manejo centralizado
- **CORS Configurado**: Seguridad y acceso
- **Rate Limiting**: Protección contra abuso

### API OpenAI
- **Modelo Eficiente**: gpt-4o-mini (más rápido)
- **Temperature Balanceado**: 0.7 (creativo pero consistente)
- **Max Tokens**: 1000 (respuestas concisas)

---

## 🔐 Seguridad

### 1. Variables de Entorno
```bash
# Nunca commits .env
# Siempre usa .env.example
OPENAI_API_KEY=secret_nunca_visible
```

### 2. CORS Configurado
```javascript
// Solo localhost durante desarrollo
const origins = [
  "http://localhost",
  "http://localhost:5173",
];
```

### 3. Input Validation
```javascript
// Valida que pregunta no esté vacía
if (!question || question.trim() === '') {
  throw new AppError('Pregunta vacía', 400);
}
```

### 4. Error Handling
```javascript
// Nunca expone detalles internos en producción
{
  error: true,
  status: 500,
  message: "Error seguro para usuario"
}
```

---

## 📈 Rendimiento

### Métricas Típicas
- **Tiempo de Respuesta**: 1-3 segundos
- **Tamaño Bundle**: ~150KB (React + dependencias)
- **Caché Browser**: 7 días
- **Database Queries**: 0 (en memoria)

### Optimizaciones Posibles
1. Implementar Redis para caché
2. Agregar compresión Gzip
3. Usar CDN para assets
4. Implementar paginación de mensajes

---

## 🧪 Testing (Recomendado)

```javascript
// Testing Framework: Jest + React Testing Library

// Ejemplo de test
describe('ChatContainer', () => {
  it('should send message on Enter key', () => {
    // Test de envío
  });
  
  it('should display suggestions on load', () => {
    // Test de sugerencias
  });
  
  it('should handle API errors gracefully', () => {
    // Test de errores
  });
});
```

---

## 📚 Bibliografía y Recursos

### Documentación Oficial
- [OpenAI API Reference](https://platform.openai.com/docs)
- [Express.js Guide](https://expressjs.com)
- [React Documentation](https://react.dev)
- [MDN Web Docs](https://developer.mozilla.org)

### Artículos Técnicos
- [REST API Best Practices](https://restfulapi.net)
- [React Hooks Deep Dive](https://react.dev/reference/react/hooks)
- [Node.js Best Practices](https://nodejs.org/en/docs/guides)

---

**Versión**: 1.0.0  
**Última Actualización**: Mayo 2026  
**Autor**: Kimberly Moquete Mercado
