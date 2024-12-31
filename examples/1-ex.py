#!/usr/bin/env python3
'using type aliases'

type Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [ scalar * num for num in vector ]

new_vector = scale(2.0, [1.0, -4.2, 5.4 ])
