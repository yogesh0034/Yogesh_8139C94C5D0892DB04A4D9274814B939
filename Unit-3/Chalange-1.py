def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Test the function
if __name__ == "__main__":
    products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
    target_product = "Apple"

    result = linear_search_product(products, target_product)

    if result:
        print(f"The target product '{target_product}' is found at indices: {result}")
    else:
        print(f"The target product '{target_product}' is not found in the list.")
