# 🎨 PLANTILLAS DE MIRO RELLENADAS — TALLER 3
> **Instrucciones:** Copia y pega estos textos directamente en las notas adhesivas (sticky notes) y tarjetas de tu tablero de Miro.

---

## 🖼️ Frame 1: Frame Principal del Taller

* **Título del Frame Grande:** `Taller 3 – CI/CD + Render + ConfigCat + DoD Final`
* **Subtítulo:** Cierre de Fase 1 — Repositorio Web (Calculator API)

---

## 🖼️ Frame 2: Diagnóstico del Pipeline Actual (Bloque 1)

### 📌 Zona A — Flujo Actual (Sticky Notes horizontales)
1. 🟨 `Push / PR a master`
2. 🟦 `CI (ruff lint + 26 pytest + 80% coverage)`
3. 🟪 `Code Review (Pull Request)`
4. 🟩 `Merge a master`
5. 🟦 `Imagen Docker -> GHCR`
6. 🟩 `Auto-deploy a Render (Deploy Hook)`
7. 🟪 `Feature Toggle (ConfigCat)`

---

### 🚦 Zona B — Semáforo del Pipeline

#### 🟢 Ya Funciona Bien (Sticky Notes Verdes)
* CI automatizado en GitHub Actions con ruff y pytest.
* Cobertura de código del 84% (supera el mínimo del 80%).
* Generación de imagen Docker y publicación en GHCR.
* Auto-deploy a Render en vivo (`https://web-k1av.onrender.com`).
* Feature Toggles configurados con ConfigCat.

#### 🟡 Parcial / Manual (Sticky Notes Amarillas)
* Aprobación manual de bypass en Pull Requests por permisos de equipo.
* Monitoreo inicial de notificaciones de despliegue.

#### 🔴 Falta Completamente (Sticky Notes Rojas)
* *(¡Ninguno! Todos los 3 pendientes de Fase 1 fueron cerrados hoy).*

---

### ❓ Zona C — Preguntas Clave

* **Sticky Note 1:** ¿Cuánto tarda el CI actualmente?  
  👉 *Respuesta: ~40 segundos.*
* **Sticky Note 2:** ¿Qué tan confiable es?  
  👉 *Respuesta: 100% confiable, 26 tests en verde sin flakiness.*
* **Sticky Note 3:** ¿Quién tiene que hacer algo manual después del merge a master?  
  👉 *Respuesta: Nadie, el deploy a Render es 100% automático vía Deploy Hook.*
* **Sticky Note 4:** ¿Cuál es el mayor miedo al desplegar?  
  👉 *Respuesta: Romper producción. Mitigado por los 26 tests y Feature Flags en OFF por defecto.*

---

## 🖼️ Frame 3: Automatización de Pruebas (Bloque 2)

### 📝 Sección A – Mínimo Viable de Calidad
* **Tests que deben pasar sí o sí:**
  - Pruebas unitarias de operaciones básicas (suma, resta, multiplicación, división).
  - Pruebas de integración de endpoints Flask (`/health`, `/suma`, `/resta`, `/multiplicacion`, `/division`, `/config`).
  - Linter `ruff` sin ninguna advertencia.
  - Cobertura de código mínima: **80%**.
* **Tiempo máximo aceptable del CI:** `3 minutos`

---

### 🚀 Sección B – Mejoras Realizadas Hoy
1. Creación de servidor web Flask con 12 pruebas de endpoints HTTP.
2. Ampliación de la suite a 26 pruebas automáticas con reporte de cobertura (`pytest-cov` al 84%).
3. Pruebas de seguridad para endpoints bloqueados por Feature Flags (retorno HTTP 404).

---

### 🤝 Sección C – Acuerdo del Equipo
> *"Si el CI está rojo -> se prioriza ponerlo verde antes de seguir con features."*  
> **¿Acordado?** `SÍ ✅ (Unánime)`

---

## 🖼️ Frame 4: Auto-deploy a Render (Bloque 3)

### ✅ Checklist de Configuración
* [x] Repositorio conectado a Render (`github.com/nfruiz23-lang/Web`)
* [x] Branch: `master`
* [x] Auto-Deploy / Deploy Hook activado
* [x] Build Command: Dockerfile
* [x] Start Command: `python main.py` (CMD Dockerfile)
* [x] Variables de entorno cargadas (`PORT=5000`, `CONFIGCAT_SDK_KEY`)
* [x] Health Check Path definido (`/health`)
* [x] Primer deploy automático verificado (`https://web-k1av.onrender.com`)

---

### 👥 Decisiones del Equipo
* **¿Desplegamos directo a Producción o primero a Staging?**  
  👉 *Directo a Producción, protegidos por Feature Flags en OFF.*
* **¿Quién recibe la notificación si falla el deploy?**  
  👉 *El equipo de desarrollo vía correos de Render y logs de GitHub Actions.*

---

### 🛠️ Problemas Encontrados y Soluciones
* **Problema:** Conflicto de ramas entre `main` y `master`.
* **Solución:** Se actualizó el workflow `ci.yaml` para apuntar a `master` y se realizó la resolución de conflictos localmente.

---

## 🖼️ Frame 5: Feature Toggle con ConfigCat (Bloque 4)

### ⚙️ Configuración
* **Proyecto ConfigCat:** `Aresaens03's Product`
* **SDK integrado:** `Sí (configcat-client 9.0.4)`
* **API Key en variable de entorno:** `Sí (CONFIGCAT_SDK_KEY)`

---

### 🚩 Toggles Creados
1. **`division_enabled`**: Controla el endpoint `/division`. (Estado inicial: OFF).
2. **`dark_mode_enabled` (Ejemplo 3)**: Controla el botón de tema oscuro en el Dashboard. (Estado inicial: OFF).

---

### 🎬 Demostración en Vivo (Ejemplo 3 - Dark Mode)
* **Toggle OFF:**  
  - Endpoint `/division` retorna error 404.
  - El botón de cambio de tema (☀️/🌙) permanece **completamente oculto**.
* **Toggle ON:**  
  - Endpoint `/division` realiza el cálculo normalmente.
  - El botón de cambio de tema **aparece arriba** y permite alternar a **Modo Oscuro** en vivo sin redeploy.

---

### 🔐 Acuerdos de Gobernanza
* **¿Quién puede activar/desactivar toggles en producción?**  
  👉 *El Product Owner con la validación del Tech Lead.*
* **¿Todo toggle debe tener fecha de limpieza?**  
  👉 *Sí, se elimina el código del toggle después de 2 semanas de estabilidad.*

---

## 🖼️ Frame 6: Definition of Done Final (Bloque 5)

| 🛠️ DoD Técnico | 💼 DoD de Negocio | 🚀 DoD de Despliegue |
| :--- | :--- | :--- |
| • Código revisado en Pull Request | • Criterios de Aceptación cumplidos | • Desplegado automáticamente en Render |
| • CI verde (26 tests + ruff + 80% cov) | • Validado en la URL de producción | • Health check `/health` respondiendo 200 OK |
| • Imagen Docker publicada en GHCR | • PO informado del estado del Toggle | • Monitoreo de logs en Render verificado |
| • Feature Toggle configurado (`OFF`) | | • Toggle en estado inicial acordado (`OFF`) |
| • Sin regresiones en código existente | | |

* **¿Este DoD queda oficial a partir de hoy?** `SÍ ✅`  
* **Checklist de Fase 1 ->** `✅ CERRADA COMPLETAMENTE`

---

## 🖼️ Frame 7: Frame de Cierre del Taller

### 💬 Ronda Final (Frase del Equipo)
> *"A partir de mañana, desplegaremos a producción varias veces por semana con total confianza respaldados por tests automáticos y Feature Flags."*

---

### 📌 Acciones de Seguimiento
* [x] Monitorear los próximos 5 deploys automáticos en Render.
* [x] Crear Feature Toggles para las próximas 2 historias de usuario del backlog.
* [x] Revisar la efectividad del DoD en la próxima Retrospective del Sprint.
