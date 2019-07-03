
class Fractal:
    def __init__(self):
        raise NotImplementedError("Fractals cannot be instantiated.")
    def count(self, z, c, MAX_ITERATIONS, powerof):
            for i in range(MAX_ITERATIONS):
                z = z**powerof + c
                if abs(z) > 2:
                    return i
            return MAX_ITERATIONS - 1


