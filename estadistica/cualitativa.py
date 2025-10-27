from collections import Counter
from .base import EstadisticaBase

class EstadisticaCualitativa(EstadisticaBase):
    """
    Clase para análisis de variables cualitativas (categóricas).
    Hereda de EstadisticaBase.
    """

    def resumen(self):
        """
        Retorna un diccionario con:
         - moda: lista de valores que más se repiten (puede ser multi-moda)
         - frecuencias: Counter con conteos
         - porcentajes: dict con porcentaje por categoría (float con 2 decimales)
        """
        # Normalizar None/NaN si se reciben como strings o valores especiales
        datos_limpios = [d for d in self.datos if d is not None]

        conteos = Counter(datos_limpios)
        total = sum(conteos.values()) if conteos else 0

        if total == 0:
            return {
                "moda": [],
                "frecuencias": conteos,
                "porcentajes": {}
            }

        max_count = max(conteos.values())
        moda = [k for k, v in conteos.items() if v == max_count]

        porcentajes = {k: round((v / total) * 100, 2) for k, v in conteos.items()}

        return {
            "moda": moda,
            "frecuencias": dict(conteos),
            "porcentajes": porcentajes
        }
