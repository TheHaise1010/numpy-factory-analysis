import numpy as np
from src.generate_data import simulate_production
from src.analyze_production import (
    total_production_per_product,
    average_daily_production,
    most_productive_day,
    product_with_max_total
)
from src.helpers import print_total_per_product, print_average_per_product

if __name__ == "__main__":
    days = 30
    products = ['A', 'B', 'C', 'D', 'E']

    production = simulate_production(days=days, num_products=len(products))

    print("Production matrix:\n")
    print(production)

    totals = total_production_per_product(production)
    print_total_per_product(totals, products)

    averages = average_daily_production(production)
    print_average_per_product(averages, products)

    best_day_index, best_day_total = most_productive_day(production)
    print(f"\nMost productive day: Day {best_day_index + 1} with {best_day_total} units")

    best_product_index = product_with_max_total(production)
    print(f"Most produced product overall: Product {products[best_product_index]}")
