# 📘 Scrum + Trunk-Based Development (TBD) Playbook
**Versión:** 2.0 (Actualizado tras Taller 4: Backlog & Flow Sprint Planning)  
**Repositorio:** [https://github.com/nfruiz23-lang/Web](https://github.com/nfruiz23-lang/Web)  
**Estado:** Activo / Normativo  

Este playbook establece los acuerdos operativos, roles, reglas de integración, Definition of Ready (DoR) y Definition of Done (DoD) para trabajar con **Trunk-Based Development (TBD)** y **Continuous Deployment (CD)** en nuestro equipo.

---

## 1. Diagnóstico del Flujo Actual (Resumen)
* **Flujo Operativo:** `Commit Local` ➔ `PR Corto` ➔ `CI (Ruff + Pytest)` ➔ `Review Rápida` ➔ `Merge a main` ➔ `Docker Build & Push (GHCR)` ➔ `Deploy Continuo`.
* **Fricciones Superadas:**
  1. Eliminación de ramas de larga duración mediante re-sliceado vertical ($\le 24$h).
  2. Reducción de cuellos de botella en Code Reviews fijando acuerdos de SLA $< 2$ horas para lotes pequeños.
  3. Eliminación del temor a romper producción desacoplando el **Despliegue Técnico** de la **Liberación Comercial (*Release*)** mediante **Feature Toggles** (ConfigCat).

---

## 2. Roles Adaptados a TBD + Continuous Deployment

| Rol | Responsabilidad Tradicional | Nueva Responsabilidad en TBD + CD |
| :--- | :--- | :--- |
| **Product Owner (PO)** | Define qué construir en sprints de 2-3 semanas; espera a la Review para validar. | • Participa activamente en el **Story Slicing** vertical ($\le 24$h).<br>• Gestiona el ciclo de vida de los **Feature Toggles** (decide cuándo activar una función a los usuarios desde el panel de ConfigCat).<br>• Redacta Acceptance Criteria verificables directamente en producción. |
| **Developers** | Desarrollan en ramas aisladas durante días; integran al final del sprint. | • **Ownership colectivo del pipeline:** Si `main` se rompe (rojo), detener todo hasta arreglarlo.<br>• Integrar código a `main` al menos **una vez al día** en lotes muy pequeños (< 150 líneas).<br>• Escribir pruebas unitarias automatizadas antes o junto con el código (CI siempre en verde). |
| **Scrum Master** | Facilita ceremonias clásicas y monitorea velocidad del sprint. | • Elimina el miedo a integrar directamente a `main`.<br>• Facilita la disciplina diaria de ramas cortas y remueve bloqueos inmediatos de CI/CD.<br>• Vela por el cumplimiento del Definition of Ready (DoR) antes de la Planning. |

---

## 3. Definition of Ready (DoR) para Trunk-Based Development

Ninguna historia ingresa al **Sprint Backlog** si no satisface el 100% de estos 5 criterios:

1. **[x] Sliceado Diario ($\le$ 24 Horas):** La funcionalidad está rebanada de modo que un desarrollador pueda codificarla, probarla y fusionarla a `main` en menos de un día hábil (lotes menores a 150-200 líneas).
2. **[x] Acceptance Criteria Observables en Producción:** Condiciones de satisfacción redactadas para ser verificadas una vez desplegado el artefacto (en vivo o mediante flags), no en local.
3. **[x] Estrategia de Feature Toggle Definida:** Se explicita si requiere toggle, su identificador técnico en ConfigCat (ej. `ENABLE_DIVISION`) y su estado inicial apagado (`Rollout 0%`).
4. **[x] Cero Dependencias Bloqueantes Externas:** No existen bloqueos técnicos, contratos de datos inconclusos ni dependencias de terceros sin mockear.
5. **[x] Criterio de Validación Comprendido por el Equipo:** Claridad absoluta en cómo la suite de `pytest` y la verificación manual o de logs confirmarán el éxito.

---

## 4. Acuerdos de Planificación de Sprint Orientada a Flujo (Flow Planning)

### Reglas de Ordenación del Sprint Backlog:
1. **Regla del Día 1:** El primer ítem del Sprint Backlog debe tener commit y merge a `main` el **Día 1 del sprint**.
2. **Orden por Integración y Riesgo:**
   * **Día 1-2 (Habilitación & Dark Launch):** Lógica del Core, APIs internas y tests unitarios. Flags en `OFF` (0%). Cero impacto al usuario.
   * **Día 3-4 (UI & Canary Rollout):** Conexión visual en frontend y habilitación al 10% para validación de PO y usuarios piloto.
   * **Día 5+ (Feature Completion & Flag Sunset):** Rollout progresivo al 100% y PR de limpieza de condicionales de flag.

### Plantilla de Sprint Goal Orientado a TBD:
> *"Al final del sprint, los usuarios podrán **[Capacidad de Valor Principal]**, aunque **[Funcionalidad Secundaria/Avanzada]** permanezca inicialmente protegida detrás de un Feature Toggle para validación interna."*

---

## 5. Caso de Estudio Práctico de Re-sliceado (Taller 4)

### Des-construcción de Antipatrón Monolítico:
* **Historia Original Problemática (Issue #4):** *"feat: multiplicación, división e historial + encender toggle al 100%"* (Estimación > 4 días, batch masivo, alto riesgo de regresión).

### Re-sliceado Vertical Aplicado en el Repositorio Real:
* **Issue #11 (Día 1 - Dark Launch):** Implementación de `division()` en `Calculator` con captura de `ZeroDivisionError`. Flag `ENABLE_DIVISION` al 0%. Merge a `main` verde.
* **Issue #12 (Día 2 - Canario):** Botones en interfaz web condicionados por ConfigCat. Rollout interno al 10%.
* **Issue #13 (Día 3 - Camino Feliz):** Estructura de historial en memoria y renderizado condicionado por `ENABLE_CALC_HISTORY`.
* **Issue #14 (Día 4-5 - Sunsetting):** Rollout al 100% en ConfigCat y PR de remoción de deuda técnica de flags temporales.

---

## 6. Reglas de Oro de Integración a Main (TBD Golden Rules)
1. **Vida de rama máxima de 24 horas:** Ningún branch sobrevive más de un día sin merge a `main`.
2. **Main siempre verde y desplegable:** Si el pipeline de GitHub Actions falla, se activa la regla *Stop the Line*; nadie introduce cambios hasta reparar `main` o revertir en $< 10$ minutos.
3. **Tests locales obligatorios:** Ejecución local de `ruff check .` y `pytest` previa a todo push.
4. **Desacoplar Deploy de Release:** Desplegar a producción es continuo; habilitar al cliente es una decisión comercial controlada por flags.
5. **Cambios en lotes pequeños (Small Batches):** Commits atómicos de 50 a 150 líneas para revisiones inmediatas y sin conflictos.

---

## 7. Definition of Done (DoD) Consolidado
Un incremento se considera **DONE** cuando:
* [x] Pruebas unitarias automatizadas cubren los caminos felices y de excepción.
* [x] Linter `ruff` ejecutado sin errores.
* [x] Pipeline de CI en GitHub Actions en verde (Jobs `test` y `build_and_push` exitosos).
* [x] Imagen Docker construida y publicada en GitHub Container Registry (`ghcr.io`).
* [x] Feature Flag configurado y verificado en ConfigCat si la función no es pública aún.
* [x] Criterios de Aceptación verificados por el PO en ambiente desplegado.
* [x] En caso de lanzamiento al 100%, se planificó la tarea de remoción del flag (Sunsetting).

---

## 8. Acuerdos y Compromisos para los Próximos Sprints
1. **Filtro DoR Estricto:** Toda historia nueva debe ser evaluada frente a los 4 criterios de TBD antes de la Planning.
2. **Code Reviews en < 2 Horas:** Prioridad de revisión para destrabar el pipeline y no acumular PRs abiertos.
3. **Ronda de Daily Orientada a Integración:** Cada mañana responder: *¿Qué voy a integrar hoy a main y qué flag protege el cambio?*
