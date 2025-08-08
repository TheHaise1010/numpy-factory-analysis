def print_total_per_product(total_array: list, product_names: list[str]):
    print("\nTotal production per product:")
    for i, total in enumerate(total_array):
        print(f"Product {product_names[i]}: {total} units")

def print_average_per_product(avg_array: list, product_names: list[str]):
    print("\nAverage daily production per product:")
    for i, avg in enumerate(avg_array):
        print(f"Product {product_names[i]}: {avg:.2f} units")
