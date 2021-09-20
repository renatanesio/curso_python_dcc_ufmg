class Ponto2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Retangulo:
    def __init__(self, esq_sup, dir_inf):
        self.__esq_sup = esq_sup
        self.__dir_inf = dir_inf
        self.width = self.dir_inf.x - self.esq_sup.x
        self.height = self.esq_sup.y - self.dir_inf.y

    @property
    def esq_sup(self):
        return self.__esq_sup

    @property
    def dir_inf(self):
        return self.__dir_inf

    def calcularArea(self):
        return self.width * self.height

    def calcularIntersecao(self, ret):
        if (ret.dir_inf.x < self.esq_sup.x) or (ret.esq_sup.x > self.dir_inf.x) or (ret.dir_inf.y > self.esq_sup.y) or \
                (ret.esq_sup.y < self.dir_inf.y):
            return None

        else:
            esq_sup = Ponto2D(max(ret.esq_sup.x, self.esq_sup.x), min(ret.esq_sup.y, self.esq_sup.y))
            dir_inf = Ponto2D(min(ret.dir_inf.x, self.dir_inf.x), max(ret.dir_inf.y, self.dir_inf.y))

            inter = Retangulo(esq_sup, dir_inf)

            return inter.calcularArea()
