def surface_area_of_cube(edge_length: float) -> str:
	return f"The surface area of the cube is {6 * edge_length ** 2}."
# Nothing is being called above because we are defining, not calling.

# Call the function and print the result
print(surface_area_of_cube(3))
# The surface area of the cube is 54.

########################
########################
########################

# Type Aliases
type Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
	return [scalar * num for num in vector]
# passes type checking; a list of floats qualifies as a Vector
new_vector = scale(2.0, [1.0, -4.2, 5.4])

print(new_vector)
# [2.0, -8.4, 10.8]