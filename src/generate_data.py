import numpy as np

def simulate_production(days, num_products, min_units=50, max_units=200) -> np.ndarray:
    return np.random.randint(min_units, max_units + 1, size=(days, num_products))
