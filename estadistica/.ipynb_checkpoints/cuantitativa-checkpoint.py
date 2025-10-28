import numpy as np
from estadistica.base import EstadisticaBase

class EstadisticaCuantitativa(EstadisticaBase):
    """
    Clase para cálculos estadísticos cuantitativos.
    Hereda de EstadisticaBase.
    """

    def resumen(self):
        """
        Retorna un diccionario con estadísticas básicas:
        media, mediana, varianza, desviación estándar y percentiles 25,50,75
        """
        return {
            "media": np.mean(self.datos),
            "mediana": np.median(self.datos),
            "varianza": np.var(self.datos, ddof=1),
            "desviacion_estandar": np.std(self.datos, ddof=1),
            "percentil_25": np.percentile(self.datos, 25),
            "percentil_50": np.percentile(self.datos, 50),
            "percentil_75": np.percentile(self.datos, 75)
        }
