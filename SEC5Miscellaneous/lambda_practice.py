def celsius_to_fahrenheit_above_freezing(celsius_temperatures):
    F_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temperatures))
    return list(filter(lambda f: f >= 32, F_temps))

# Example usage
print(celsius_to_fahrenheit_above_freezing([0, 10, 20, -5, 30]))
# Expected output: temperatures in Fahrenheit that are above 32 degrees






result = lambda x, y, z: z % x == 0 and z % y == 0
print(result(5, 1, 5))