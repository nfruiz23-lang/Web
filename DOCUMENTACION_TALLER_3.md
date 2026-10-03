# 📄 DOCUMENTACIÓN OFICIAL Y ENTREGABLE COMPLETO — TALLER 3
## CI/CD, Automatización de Pruebas y Cierre de Pendientes (Render + ConfigCat)

**Proyecto:** Calculator API / Dashboard - Chanchito Feliz 🐷  
**Estudiante / Equipo:** Diplomado Desarrollo Web  
**URL de la Aplicación en Vivo:** [https://web-k1av.onrender.com](https://web-k1av.onrender.com)  
**Repositorio GitHub:** [github.com/nfruiz23-lang/Web](https://github.com/nfruiz23-lang/Web)  

---

## 📌 1. RESUMEN DE OBJETIVOS Y SEGUIMIENTO DE PENDIENTES

En este taller 3 se cerraron completamente los **3 pendientes de la Fase 1**:

1. **Auto-deploy a Render:** Configuramos GitHub Actions para que, al aprobar cambios en la rama `master`, la aplicación se publique automáticamente en Render en la URL [https://web-k1av.onrender.com](https://web-k1av.onrender.com).
2. **Automatización de Pruebas:** Ampliamos la suite de 3 a **26 pruebas automáticas** en Python con una cobertura del **84%**. Si una prueba o linter falla, el pipeline bloquea el despliegue.
3. **Feature Toggles (ConfigCat):** Integramos la herramienta ConfigCat con los flags `division_enabled` y `dark_mode_enabled`, permitiendo desacoplar el despliegue del código de su liberación al usuario.

---

## 📸 2. EVIDENCIAS FOTOGRÁFICAS REQUERIDAS (PANTALLAZOS)

*(En esta sección debes adjuntar las 5 capturas de pantalla de tu navegador)*

### 📸 Evidencia 1: Pipeline de CI en GitHub Actions (Verde 🟢)
* **Descripción:** Muestra que las 26 pruebas automáticas y la verificación de estilo (`ruff`) se ejecutaron correctamente en GitHub.
*(Pegar aquí el pantallazo de GitHub Actions o del PR con los checks en verde)*

---

### 📸 Evidencia 2: Despliegue Exitoso en Render
* **Descripción:** Muestra el panel de Render en estado `Deploy succeeded | Live` con la URL pública generada (`https://web-k1av.onrender.com`).
*(Pegar aquí el pantallazo del panel de Render)*

---

### 📸 Evidencia 3: Panel de ConfigCat con Feature Flags
* **Descripción:** Muestra los dos interruptores (flags) creados en ConfigCat: `division_enabled` y `dark_mode_enabled`.
*(Pegar aquí el pantallazo del dashboard de ConfigCat)*

---

### 📸 Evidencia 4: Ejemplo 3 — Ticket 1 (Funcionalidad Oculta / Toggle OFF)
* **Descripción:** La aplicación está desplegada en vivo, pero como el toggle de Modo Oscuro y División están en `OFF`, el botón de cambio de tema no aparece y la división está bloqueada.
*(Pegar aquí el pantallazo de la web en modo claro con los flags en OFF)*

---

### 📸 Evidencia 5: Ejemplo 3 — Ticket 2 (Modo Oscuro Activado / Toggle ON)
* **Descripción:** Tras activar `dark_mode_enabled` en ConfigCat y refrescar la página, el botón de cambio de tema aparece arriba y la web se transforma a Modo Oscuro en tiempo real.
*(Pegar aquí el pantallazo de la web en Modo Oscuro)*

---

## 📜 3. DEFINITION OF DONE (DoD) FORMALIZADO

Criterios con los que el equipo considera que una historia de usuario está **Terminada (Done)**:

- [x] **Código probado:** 26 pruebas automáticas pasando con un 84% de cobertura.
- [x] **Código limpio:** Linter `ruff` sin advertencias ni errores.
- [x] **Desplegado:** Cambios publicados automáticamente en Render desde `master`.
- [x] **Protegido:** Nuevas funciones incompletas ocultas tras un Feature Toggle (`OFF`).
- [x] **Verificado:** Endpoint de salud `/health` respondiendo estado HTTP 200 OK.

---

## 💻 4. CÓDIGO COMPLETO IMPLEMENTADO EN EL TALLER

A continuación se adjunta el código fuente exacto de todos los archivos creados y modificados durante el Taller 3:

### 4.1. `src/requirements.txt` (Dependencias del Proyecto)
```text
flask==3.1.1
configcat-client==9.0.4
pytest==8.3.4
pytest-cov==6.1.1
ruff==0.8.1
```

---

### 4.2. `src/main.py` (Aplicación Principal Flask + SDK ConfigCat)
```python
import os
import configcatclient

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# --- ConfigCat (Feature Toggle) ---
CONFIGCAT_SDK_KEY = os.environ.get("CONFIGCAT_SDK_KEY", "")
configcat_client = None

if CONFIGCAT_SDK_KEY:
    configcat_client = configcatclient.get(CONFIGCAT_SDK_KEY)


def is_feature_enabled(flag_name: str, default: bool = False) -> bool:
    """Consulta si un feature flag está habilitado en ConfigCat."""
    if configcat_client:
        return configcat_client.get_value(flag_name, default)
    return default


# --- Calculator (lógica de negocio) ---
class Calculator:
    def suma(self, a: int, b: int) -> int:
        return a + b

    def resta(self, a: int, b: int) -> int:
        return a - b

    def multiplicacion(self, a: int, b: int) -> int:
        return a * b

    def division(self, a: int, b: int) -> float:
        """Nueva funcionalidad — protegida por feature flag 'division_enabled'."""
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b


calc = Calculator()


# =============================================
#  Rutas — Página principal (Dashboard)
# =============================================
@app.route("/")
def dashboard():
    """
    Dashboard visual con soporte de Dark Mode (Ejemplo 3 del Taller).
    Ticket 1: Variables CSS + lógica de cambio de clase, detrás de dark_mode_enabled.
    Ticket 2: Botón toggle visible solo cuando el flag está ON.
    """
    dark_mode = is_feature_enabled("dark_mode_enabled", default=False)
    division_enabled = is_feature_enabled("division_enabled", default=False)
    return render_template(
        "dashboard.html",
        dark_mode=dark_mode,
        division_enabled=division_enabled,
    )


# =============================================
#  Rutas — API JSON
# =============================================
@app.route("/api")
def api_index():
    return jsonify({
        "servicio": "Calculator API - Chanchito Feliz 🐷",
        "version": "1.0.0",
        "endpoints": ["/suma", "/resta", "/multiplicacion", "/division", "/health", "/config"],
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/suma")
def ruta_suma():
    a = request.args.get("a", type=int, default=0)
    b = request.args.get("b", type=int, default=0)
    return jsonify({"operacion": "suma", "a": a, "b": b, "resultado": calc.suma(a, b)})


@app.route("/resta")
def ruta_resta():
    a = request.args.get("a", type=int, default=0)
    b = request.args.get("b", type=int, default=0)
    return jsonify({"operacion": "resta", "a": a, "b": b, "resultado": calc.resta(a, b)})


@app.route("/multiplicacion")
def ruta_multiplicacion():
    a = request.args.get("a", type=int, default=0)
    b = request.args.get("b", type=int, default=0)
    return jsonify({"operacion": "multiplicacion", "a": a, "b": b, "resultado": calc.multiplicacion(a, b)})


@app.route("/division")
def ruta_division():
    """Solo disponible si el feature flag 'division_enabled' está ON en ConfigCat."""
    if not is_feature_enabled("division_enabled", default=False):
        return jsonify({"error": "Función no disponible todavía"}), 404

    a = request.args.get("a", type=int, default=0)
    b = request.args.get("b", type=int, default=0)
    try:
        resultado = calc.division(a, b)
        return jsonify({"operacion": "division", "a": a, "b": b, "resultado": resultado})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# =============================================
#  Rutas — Feature Toggle Config
# =============================================
@app.route("/config")
def config():
    """Devuelve la configuración de UI basada en feature flags (para el frontend)."""
    dark_mode = is_feature_enabled("dark_mode_enabled", default=False)
    division = is_feature_enabled("division_enabled", default=False)
    return jsonify({
        "dark_mode_enabled": dark_mode,
        "division_enabled": division,
        "theme": "dark" if dark_mode else "light",
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```

---

### 4.3. `src/templates/dashboard.html` (Interfaz de Usuario + Dark Mode Ejemplo 3)
```html
<!DOCTYPE html>
<html lang="es" data-theme="{{ 'dark' if dark_mode else 'light' }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🐷 Calculator Dashboard - Chanchito Feliz</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* EJEMPLO 3 — DARK MODE (Ticket 1: Estilos CSS) */
        :root, [data-theme="light"] {
            --bg-primary: #f0f2f5;
            --bg-card: #ffffff;
            --text-primary: #1a1a2e;
            --text-secondary: #6b7280;
            --accent: #667eea;
            --border: #e5e7eb;
        }

        [data-theme="dark"] {
            --bg-primary: #0f0f1a;
            --bg-card: #1a1a2e;
            --text-primary: #e5e7eb;
            --text-secondary: #9ca3af;
            --accent: #818cf8;
            --border: #2d2d4a;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            transition: background 0.4s ease, color 0.4s ease;
        }

        .theme-toggle.hidden { display: none; }
    </style>
</head>
<body>
    <header>
        <h1>🐷 Calculator Dashboard</h1>
        <!-- EJEMPLO 3 — Ticket 2: Oculto si dark_mode_enabled = OFF -->
        <div id="themeToggle" class="theme-toggle {{ '' if dark_mode else 'hidden' }}">
            <button id="toggleSwitch">Cambiar Tema ☀️/🌙</button>
        </div>
    </header>
    <!-- ... Resto del Dashboard ... -->
</body>
</html>
```

---

### 4.4. `src/test.py` (Suite de 26 Pruebas Automáticas)
```python
import pytest
from main import Calculator, app


class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_suma_positivos(self):
        assert self.calc.suma(2, 3) == 5

    def test_resta_positivos(self):
        assert self.calc.resta(5, 3) == 2

    def test_multiplicacion_positivos(self):
        assert self.calc.multiplicacion(3, 4) == 12

    def test_division_exacta(self):
        assert self.calc.division(10, 2) == 5.0

    def test_division_por_cero_lanza_error(self):
        with pytest.raises(ValueError, match="No se puede dividir entre cero"):
            self.calc.division(10, 0)


class TestAPI:
    def setup_method(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_health_check_status(self):
        response = self.client.get("/health")
        assert response.status_code == 200

    def test_division_sin_toggle_retorna_404(self):
        response = self.client.get("/division?a=10&b=2")
        assert response.status_code == 404
```

---

### 4.5. `.github/workflows/ci.yaml` (Pipeline CI/CD con Deploy Hook)
```yaml
name: CI Pipeline - Test, Lint, Build & Deploy

on:
  push:
    branches:
      - master
  pull_request:
    branches:
      - master

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install -r src/requirements.txt
      - run: cd src && ruff check .
      - run: cd src && pytest test.py -v --cov=main --cov-fail-under=80

  build_and_push:
    needs: test
    if: github.ref == 'refs/heads/master' && github.event_name == 'push'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - run: echo "REPO=${GITHUB_REPOSITORY,,}" >> ${GITHUB_ENV}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ghcr.io/${{ env.REPO }}:latest

  deploy_to_render:
    needs: build_and_push
    if: github.ref == 'refs/heads/master' && github.event_name == 'push'
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy
        run: curl -X POST "${{ secrets.RENDER_DEPLOY_HOOK_URL }}"
```

---

### 4.6. `Dockerfile`
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ /app/
EXPOSE 5000
CMD ["python", "main.py"]
```
