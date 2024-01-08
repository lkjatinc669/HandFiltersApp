class FingersDistance:
    def __init__(self) -> None:
        pass    

    def calDistance(self, p1, p2):
        x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
        lenght = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1.0 / 2)
        return lenght