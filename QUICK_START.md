# 🚀 Guía Rápida de Inicio

## ⚡ 5 Pasos para Ejecutar el Proyecto

### 1️⃣ Clonar y Navegar
```bash
git clone https://github.com/kmoquetemercado-collab/proyecto-estatuto-organico-uasd-ai-web.git
cd proyecto-estatuto-organico-uasd-ai-web
```

### 2️⃣ Crear Variables de Entorno
Crea un archivo `.env` en la raíz:
```env
OPENAI_API_KEY=tu_clave_openai_aqui
NODE_ENV=development
PORT=5000
FRONTEND_URL=http://localhost:5173
```

### 3️⃣ Instalar Dependencias
```bash
# Backend
npm install

# Frontend
cd frontend && npm install && cd ..
```

### 4️⃣ Ejecutar Servidores (2 terminales)

**Terminal 1 - Backend:**
```bash
npm start
# Escucha en http://localhost:5000
```

**Terminal 2 - Frontend:**
```bash
cd frontend && npm run dev
# Escucha en http://localhost:5173
```

### 5️⃣ Abrir en Navegador
```
http://localhost:5173
```

---

## ✅ Verificación

El proyecto está listo cuando ves:
- ✅ Backend: "🚀 Servidor iniciado en puerto 5000"
- ✅ Frontend: "VITE v5.x.x ready in XXX ms"
- ✅ Navegador: Chatbot abierto sin errores

---

## 📋 Checklist Antes de Entregar

- [ ] Cree archivo `.env` con su OPENAI_API_KEY
- [ ] Ejecutó `npm install` en raíz y en frontend/
- [ ] Backend corre sin errores
- [ ] Frontend carga correctamente
- [ ] Chat responde preguntas
- [ ] Preguntas sugeridas aparecen
- [ ] Interfaz es responsiva en móvil

---

## 🐛 Errores Comunes

| Error | Solución |
|-------|----------|
| "OPENAI_API_KEY no existe" | Crea `.env` con tu clave |
| "Puerto 5000 en uso" | Cambia PORT en `.env` |
| "Cannot find module" | Ejecuta `npm install` |
| "API no responde" | Verifica que backend corre |
| "Frontend no conecta" | Revisa proxy en vite.config.js |

---

## 📚 Documentación Completa

Para información técnica detallada, ver: [TECHNICAL_DOCUMENTATION.md](./TECHNICAL_DOCUMENTATION.md)

---

**¡A empezar!** 🎉
