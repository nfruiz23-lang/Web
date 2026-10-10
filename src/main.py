import os
import random
import logging
import configcatclient

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# --- Configuración de Métricas (Taller 6) ---
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

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
        "endpoints": ["/suma", "/resta", "/multiplicacion", "/division", "/pagos_express", "/health", "/config"],
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
#  Rutas — Ejemplo Taller 6 (Pagos Express)
# =============================================
@app.route("/pagos_express", methods=["GET", "POST"])
def ruta_pagos_express():
    """Ejemplo Práctico Taller 6: Pagos Express (protegido por toggle)."""
    # 1. Validar el toggle
    if not is_feature_enabled("pagos-express-v1", default=False):
        return jsonify({"error": "Pagos Express no está activo todavía"}), 404

    # 2. Simulación de la operación y TELEMETRÍA (Métricas requeridas)
    if random.random() < 0.3:  # 30% de probabilidad de fallo simulado
        logging.error("MÉTRICA TALLER 6: [FALLO] Error procesando Pago Express.")
        return jsonify({"error": "Transacción rechazada"}), 500
    
    logging.info("MÉTRICA TALLER 6: [ÉXITO] Pago Express procesado correctamente.")
    return jsonify({"status": "ok", "mensaje": "Pago exitoso con un solo clic"})


# =============================================
#  Rutas — Feature Toggle Config
# =============================================
@app.route("/config")
def config():
    """Devuelve la configuración de UI basada en feature flags (para el frontend)."""
    dark_mode = is_feature_enabled("dark_mode_enabled", default=False)
    division = is_feature_enabled("division_enabled", default=False)
    pagos_express = is_feature_enabled("pagos-express-v1", default=False)
    return jsonify({
        "dark_mode_enabled": dark_mode,
        "division_enabled": division,
        "pagos_express_v1": pagos_express,
        "theme": "dark" if dark_mode else "light",
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)