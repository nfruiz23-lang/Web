# 📘 Informe de Entregable y Documentación — Taller 3
## CI/CD, Automatización de Pruebas y Cierre de Pendientes (Render + ConfigCat)

**Proyecto:** Calculator API / Dashboard - Chanchito Feliz 🐷  
**Repositorio:** [github.com/nfruiz23-lang/Web](https://github.com/nfruiz23-lang/Web)  
**URL de Producción (Render):** [https://web-k1av.onrender.com](https://web-k1av.onrender.com)  
**Herramienta de Feature Flags:** ConfigCat (Proyecto: *Aresaens03's Product*)  

---

## 🎯 Objetivo Cumplido

Se han cerrado exitosamente los **3 pendientes de Fase 1**, logrando un flujo completo de **Trunk-Based Development (TBD)** y **Despliegue Continuo (CD)**:

1. ✅ **Auto-deploy automático a Render** desde la rama principal (`master`).
2. ✅ **Feature Toggles integrados con ConfigCat** para desacoplar el despliegue de la liberación de código.
3. ✅ **Definition of Done (DoD)** formalizado e integrado en el Playbook.
4. ✅ **Pipeline CI robusto** con linter (`ruff`), 26 pruebas automáticas y control de cobertura mínima del 80%.

---

## 📋 Checklist de Fase 1 — Estado Final

| Ítem | Estado | Descripción / Evidencia |
|---|---|---|
| Repositorio Git con Branch Protection | ✅ Completado | Regla activada en `master` con requerimiento de CI |
| Pipeline CI en GitHub Actions | ✅ Completado | [.github/workflows/ci.yaml](file:///c:/Users/Usuario/diplomado/Sabado/Web/.github/workflows/ci.yaml) con tests + ruff + cov |
| Imagen Docker en GHCR | ✅ Completado | Construcción y push automático a `ghcr.io` |
| Auto-deploy a Render | ✅ Completado | Despliegue automático vía Deploy Hook tras pasar CI |
| Feature Toggles (ConfigCat) | ✅ Completado | Flags `division_enabled` y `dark_mode_enabled` en producción |
| Definition of Done (DoD) | ✅ Documentado | Criterios técnicos, de negocio y despliegue formalizados |

---

## 🏗️ Arquitectura y Cambios Implementados

```
[ Push / PR a master ] 
         │
         ▼
 ┌────────────────────────┐
 │   GitHub Actions CI    │ ───► 1. Linting (ruff)
 └───────────┬────────────┘      2. 26 Pytest (84% Cobertura)
             │ (Si verde)
             ▼
 ┌────────────────────────┐
 │  Build Docker & Push   │ ───► Imagen publicada en GHCR
 └───────────┬────────────┘
             │
             ▼
 ┌────────────────────────┐
 │ Trigger Deploy Render  │ ───► Web Service desplegado automáticamente
 └───────────┬────────────┘
             │
             ▼
 ┌────────────────────────┐
 │   App en Producción    │ ◄─── ConfigCat SDK evalúa Feature Flags
 └────────────────────────┘      (/division, Dark Mode toggle)
```

### 📄 Archivos Clave del Proyecto

1. **`src/main.py`**:
   * API web en Flask.
   * Lógica de calculadora (`suma`, `resta`, `multiplicacion`, `division`).
   * Integración con el SDK de ConfigCat para consultar feature flags en tiempo real.
   * Endpoint de salud (`/health`) y endpoint de configuración (`/config`).

2. **`src/templates/dashboard.html`**:
   * Dashboard web responsivo y moderno.
   * Soporte de temas Claro / Oscuro vía CSS custom properties.
   * Interfaz interactiva para probar operaciones y visualizar el estado de los Feature Flags en vivo.

3. **`src/test.py`**:
   * Suite completa de **26 pruebas automáticas** (unitarias + integración de endpoints).
   * Verificación del comportamiento de endpoints cuando un flag está desactivado (retorno 404 seguro).

4. **`.github/workflows/ci.yaml`**:
   * Workflow automatizado de GitHub Actions.
   * Valida calidad del código y umbral de cobertura (mínimo 80%).
   * Dispara el Deploy Hook de Render únicamente si las pruebas y el build Docker son exitosos.

---

## 🎨 Demostración Práctica: Ejemplo 3 (Dark Mode & Feature Slicing)

Para demostrar cómo Trunk-Based Development permite integrar código incompleto de forma segura, se implementó el **Ejemplo 3 (Modo Oscuro)** siguiendo la técnica de slicing en 2 tickets:

* **Ticket 1 (Estructura detras del Flag):**
  * Se definieron las variables CSS de tema oscuro y la lógica de Javascript en `dashboard.html`.
  * Mientras `dark_mode_enabled` en ConfigCat estuvo en **OFF**, el botón de cambio de tema permaneció **completamente oculto** para los usuarios.

* **Ticket 2 (Liberación sin Re-deploy):**
  * Al cambiar `dark_mode_enabled` a **ON** en el panel de ConfigCat, el botón de cambio de tema (☀️ / 🌙) apareció inmediatamente en la aplicación desplegada sin necesidad de hacer un nuevo commit ni redeplegar en Render.

---

## 📜 Definition of Done (DoD) Formalizado

Una Historia de Usuario se considera **TERMINADA (Done)** cuando cumple con:

### 1. Calidad de Código y Pruebas
- [x] Código revisado vía Pull Request.
- [x] Análisis estático y linter (`ruff check .`) sin errores.
- [x] Cobertura de pruebas unitarias e integración mayor o igual al **80%**.

### 2. Integración y Despliegue (CI/CD)
- [x] Pipeline de CI en GitHub Actions ejecutado en verde.
- [x] Imagen Docker construida y publicada exitosamente.
- [x] Código desplegado automáticamente en Render desde `master`.
- [x] Endpoint `/health` respondiendo estado HTTP 200 OK.

### 3. Control de Funcionalidades (Feature Toggles)
- [x] Si la funcionalidad es parcial o está en desarrollo, está protegida por un Feature Toggle en **OFF** en ConfigCat.
- [x] Si está lista para producción, el Product Owner valida y activa el toggle en **ON**.

---

## 📊 Métricas del Pipeline

| Métrica | Valor |
|---|---|
| Tiempo de ejecución del CI | ~30 - 45 segundos |
| Cobertura de código alcanzada | **84%** (Total: 69 líneas, 26 tests) |
| Tiempo de despliegue en Render | ~30 segundos |
| Latencia de evaluación de Feature Toggle | < 5 ms (Caché local SDK) |
