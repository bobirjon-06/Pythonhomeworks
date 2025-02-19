import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def _add_(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Error!")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Error.")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Error.")
            return sum(a * b for a, b in zip(self.components, other.components))
        raise TypeError("Error")

    def __rmul__(self, other):
        return self * other

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Error.")
        return Vector(*[round(a / mag, 3) for a in self.components])
