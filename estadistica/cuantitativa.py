import numpy as np
from .base import EstadisticaBase

class EstadisticaCuantitativa(EstadisticaBase):
    """
    Clase para cálculos estadísticos cuantitativos.
    Hereda de EstadisticaBase.
    """

    def media(self):
        return sum(self.datos) / len(self.datos)

    def mediana(self):
        n = len(self.datos)
        mitad = n // 2
        if n % 2 == 0:
            return (self.datos[mitad - 1] + self.datos[mitad]) / 2
        else:
            return self.datos[mitad]

    def varianza(self):
        n = len(self.datos)
        media = self.media()
        suma_cuadrados = sum((x - media) ** 2 for x in self.datos)
        return suma_cuadrados / (n - 1)

    def desviacion_estandar(self):
        return self.varianza() ** 0.5

    def percentil(self, p):
        if not 0 <= p <= 100:
            raise ValueError("El percentil debe estar entre 0 y 100")
        n = len(self.datos)
        k = (n - 1) * (p / 100)
        f = int(k)
        c = k - f
        if f + 1 < n:
            return self.datos[f] + c * (self.datos[f + 1] - self.datos[f])
        else:
            return self.datos[f]

    def resumen_estadistico(self):
        """Devuelve un diccionario con todas las medidas."""
        return {
            "media": self.media(),
            "mediana": self.mediana(),
            "varianza": self.varianza(),
            "desviacion_estandar": self.desviacion_estandar(),
            "percentil_25": self.percentil(25),
            "percentil_50": self.percentil(50),
            "percentil_75": self.percentil(75),
        }
