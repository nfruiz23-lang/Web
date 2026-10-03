# 📄 DOCUMENTACIÓN Y EVIDENCIAS — TALLER 3
## CI/CD, Automatización de Pruebas y Cierre de Pendientes (Render + ConfigCat)

**Estudiante / Equipo:** Diplomado Desarrollo Web  
**URL de la Aplicación en Vivo:** [https://web-k1av.onrender.com](https://web-k1av.onrender.com)  
**Repositorio GitHub:** [github.com/nfruiz23-lang/Web](https://github.com/nfruiz23-lang/Web)  

---

## 1. RESUMEN SENCILLO DE LO REALIZADO

En este taller se completaron los **3 pendientes de la Fase 1**:

1. **Auto-deploy a Render:** Configuramos GitHub Actions para que, al aprobar cambios en la rama `master`, la aplicación se publique automáticamente en Render en la URL [https://web-k1av.onrender.com](https://web-k1av.onrender.com).
2. **Automatización de Pruebas:** Ampliamos la suite de 3 a **26 pruebas automáticas** en Python (cobertura del 84%). Si alguna prueba falla, el despliegue se cancela automáticamente.
3. **Feature Toggles (ConfigCat):** Integramos la herramienta ConfigCat para controlar qué funcionalidades ven los usuarios sin necesidad de redesplegar el código.

---

## 2. EVIDENCIAS FOTOGRÁFICAS (PANTALLAZOS)

### 📸 Evidencia 1: Pipeline de CI en GitHub Actions (Verde 🟢)
* **Descripción:** Muestra que las 26 pruebas automáticas y la verificación de estilo (`ruff`) se ejecutaron correctamente en GitHub.
*(Pegar aquí el pantallazo de GitHub Actions o del PR con los checks en verde)*

---

### 📸 Evidencia 2: Despliegue Exitoso en Render
* **Descripción:** Muestra el panel de Render en estado `Deploy succeeded | Live` con la URL pública generada.
*(Pegar aquí el pantallazo del panel de Render donde muestra `Deploy succeeded`)*

---

### 📸 Evidencia 3: Panel de ConfigCat con Feature Flags
* **Descripción:** Muestra los dos interruptores (flags) creados en ConfigCat: `division_enabled` y `dark_mode_enabled`.
*(Pegar aquí el pantallazo de ConfigCat donde se ven los 2 flags)*

---

### 📸 Evidencia 4: Ejemplo 3 — Ticket 1 (Funcionalidad Oculta / Toggle OFF)
* **Descripción:** La aplicación está desplegada en vivo, pero como el toggle de Modo Oscuro y División están en `OFF`, el botón de cambio de tema no aparece y la división está bloqueada.
*(Pegar aquí el pantallazo de la web en modo claro con la división desactivada)*

---

### 📸 Evidencia 5: Ejemplo 3 — Ticket 2 (Modo Oscuro Activado / Toggle ON)
* **Descripción:** Tras activar `dark_mode_enabled` en ConfigCat y refrescar la página, el botón de cambio de tema aparece arriba y la web se transforma a Modo Oscuro en tiempo real.
*(Pegar aquí el pantallazo de la web en Modo Oscuro)*

---

## 3. DEFINITION OF DONE (DoD) ACORDADO

Criterios con los que el equipo considera que una tarea está **Terminada (Done)**:

- [x] **Código probado:** 26 pruebas automáticas pasando con un 84% de cobertura.
- [x] **Código limpio:** Linter `ruff` sin advertencias ni errores.
- [x] **Desplegado:** Cambios publicados automáticamente en Render desde `master`.
- [x] **Protegido:** Nuevas funciones incompletas ocultas tras un Feature Toggle (`OFF`).
- [x] **Verificado:** Endpoint de salud `/health` respondiendo estado OK.
