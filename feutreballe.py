#!/usr/bin/env python3
"""
Arbitrage du Feutre-Balle
"""

class Record():
    """
    A numeric record, which can be beaten
    """

    best = None

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "best {}: {}".format(self.name, self.best)

    def update(self, value):
        """
        If value is better than best,
        update best and print info
        """
        if value is not None:
            if self.best is None or value > self.best:
                self.best = value
                print("new {}".format(self.__str__()))

    def display(self):
        """
        Display current value
        """
        if self.best is not None:
            print(self.__str__())

def avg(values):
    """
    @param  values  Iterable of numeric values
    @return  Arithmetic average
    """
    return sum(values) / len(values)

def avgof(values, nb_considered):
    """
    @param  values         Iterable of numeric values
    @param  nb_considered  Number of values at the end of values to consider
    @return  Arithmetic average of last n values
    """
    if nb_considered > len(values):
        return None
    return avg(values[-nb_considered:])

def bestof(values, nb_considered, nb_best):
    """
    @param  values         Iterable of numeric values
    @param  nb_considered  Number of values at the end of values to consider
    @param  nb_best        Number of best values among nb_considered to keep
    @return  Average of best nb_best values in last nb_considered of values
    """
    if nb_considered > len(values):
        return None
    return avg(sorted(values[-nb_considered:])[-nb_best:])

def __main__():

    best = Record("")
    bestavg5 = Record("average of 5")
    bestavg10 = Record("average of 10")
    best3of5 = Record("3 of 5")
    best10of12 = Record("10 of 12")

    historique = list()

    print("Entrer chaque score consécutif réalisé au Feutre Ball :")
    while True:
        try:
            nb_rebonds = int(input("> "))
        except KeyboardInterrupt:
            best.display()
            bestavg5.display()
            bestavg10.display()
            best3of5.display()
            best10of12.display()
            break

        historique.append(nb_rebonds)

        best.update(nb_rebonds)
        bestavg5.update(avgof(historique, 5))
        bestavg10.update(avgof(historique, 10))
        best3of5.update(bestof(historique, 5, 3))
        best10of12.update(bestof(historique, 12, 10))

if __name__ == "__main__":
    __main__()
