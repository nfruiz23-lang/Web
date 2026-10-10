import pytest
from main import Calculator, app


# =============================================
#  Tests unitarios de Calculator
# =============================================
class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    # --- Suma ---
    def test_suma_positivos(self):
        assert self.calc.suma(2, 3) == 5

    def test_suma_negativos(self):
        assert self.calc.suma(-1, -1) == -2

    def test_suma_con_cero(self):
        assert self.calc.suma(0, 5) == 5

    def test_suma_numeros_grandes(self):
        assert self.calc.suma(1000000, 2000000) == 3000000

    # --- Resta ---
    def test_resta_positivos(self):
        assert self.calc.resta(5, 3) == 2

    def test_resta_resultado_negativo(self):
        assert self.calc.resta(3, 5) == -2

    def test_resta_iguales(self):
        assert self.calc.resta(7, 7) == 0

    # --- Multiplicación ---
    def test_multiplicacion_positivos(self):
        assert self.calc.multiplicacion(3, 4) == 12

    def test_multiplicacion_por_cero(self):
        assert self.calc.multiplicacion(5, 0) == 0

    def test_multiplicacion_negativos(self):
        assert self.calc.multiplicacion(-3, -4) == 12

    def test_multiplicacion_mixto(self):
        assert self.calc.multiplicacion(-2, 5) == -10

    # --- División (nueva funcionalidad detrás del toggle) ---
    def test_division_exacta(self):
        assert self.calc.division(10, 2) == 5.0

    def test_division_decimal(self):
        assert self.calc.division(7, 2) == 3.5

    def test_division_por_cero_lanza_error(self):
        with pytest.raises(ValueError, match="No se puede dividir entre cero"):
            self.calc.division(10, 0)

    def test_division_negativa(self):
        assert self.calc.division(-10, 2) == -5.0


# =============================================
#  Tests de integración de la API (Flask)
# =============================================
class TestAPI:
    def setup_method(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    # --- Health Check ---
    def test_health_check_status(self):
        response = self.client.get("/health")
        assert response.status_code == 200

    def test_health_check_body(self):
        response = self.client.get("/health")
        assert response.get_json()["status"] == "ok"

    # --- Dashboard ---
    def test_dashboard_carga(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert b"Calculator Dashboard" in response.data

    # --- API Index ---
    def test_api_index(self):
        response = self.client.get("/api")
        assert response.status_code == 200
        data = response.get_json()
        assert "Calculator API" in data["servicio"]

    # --- Suma Endpoint ---
    def test_suma_endpoint(self):
        response = self.client.get("/suma?a=3&b=4")
        assert response.status_code == 200
        assert response.get_json()["resultado"] == 7

    def test_suma_sin_parametros(self):
        response = self.client.get("/suma")
        assert response.status_code == 200
        assert response.get_json()["resultado"] == 0

    # --- Resta Endpoint ---
    def test_resta_endpoint(self):
        response = self.client.get("/resta?a=10&b=3")
        assert response.status_code == 200
        assert response.get_json()["resultado"] == 7

    # --- Multiplicación Endpoint ---
    def test_multiplicacion_endpoint(self):
        response = self.client.get("/multiplicacion?a=5&b=6")
        assert response.status_code == 200
        assert response.get_json()["resultado"] == 30

    # --- División Endpoint (toggle OFF por defecto) ---
    def test_division_sin_toggle_retorna_404(self):
        """Sin el flag activado, /division no está disponible."""
        response = self.client.get("/division?a=10&b=2")
        assert response.status_code == 404
        assert "no disponible" in response.get_json()["error"].lower()

    # --- Config Endpoint ---
    def test_config_endpoint(self):
        response = self.client.get("/config")
        assert response.status_code == 200
        data = response.get_json()
        assert "dark_mode_enabled" in data
        assert "division_enabled" in data
        assert "theme" in data

    def test_config_tema_por_defecto_es_light(self):
        """Sin ConfigCat, el tema por defecto debe ser light."""
        response = self.client.get("/config")
        data = response.get_json()
        assert data["theme"] == "light"
        assert data["dark_mode_enabled"] is False

    # --- Pagos Express Endpoint (toggle OFF por defecto) ---
    def test_pagos_express_sin_toggle_retorna_404(self):
        """Sin el flag activado, /pagos_express no está disponible."""
        response = self.client.get("/pagos_express")
        assert response.status_code == 404
        assert "no está activo" in response.get_json()["error"].lower()