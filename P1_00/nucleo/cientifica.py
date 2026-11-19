from .z_aleatorios    import Aleatorios
from .z_algebra       import Algebra
from .z_aritmetica    import Aritmetica
from .z_combinatoria  import Combinatoria
from .z_constantes    import Constantes
from .z_conversiones  import Conversiones
from .z_estadistica   import Estadistica
from .z_logaritmos    import Logaritmos
from .z_trigonometria import Trigonometria

class CalculadoraCientifica(
    Aleatorios,
    Algebra,
    Aritmetica,
    Combinatoria,
    Constantes,
    Conversiones,
    Estadistica,
    Logaritmos,
    Trigonometria
):


    def __init__(self, configuracion=None):
        Trigonometria.__init__(self, configuracion)

