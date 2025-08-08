import numpy as np

def total_production_per_product(production: np.ndarray) -> np.ndarray:
    return production.sum(axis=0)

def average_daily_production(production: np.ndarray) -> np.ndarray:
    return production.mean(axis=0)

def most_productive_day(production: np.ndarray) -> tuple[int, int]:
    total_per_day = production.sum(axis=1)
    max_day_index = np.argmax(total_per_day)
    return max_day_index, total_per_day[max_day_index]

def product_with_max_total(production: np.ndarray) -> int:
    total = production.sum(axis=0)
    return np.argmax(total)
