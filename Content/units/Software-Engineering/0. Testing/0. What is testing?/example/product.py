from unittest.main import main


class Product:
    def __init__(self, name, size, color):  # <1>
        self.name = name
        self.size = size
        self.color = color

    def transform_name_for_sku(self):
        return self.name.upper()

    def transform_color_for_sku(self):
        return self.color.upper()

    def generate_sku(self):
        """
        Generates a Stock Keeping Unit (SKU) for this product.
        Example:
            >>> small_black_shoes = Product('shoes', 'S', 'black')
            >>> small_black_shoes.generate_sku()
            'SHOES-S-BLACK'
        """
        name = self.transform_name_for_sku()
        color = self.transform_color_for_sku()
        return f'{name}-{self.size}-{color}'

if __name__ == "__main__":
    shoes = Product('Hugo Boss', 11, 'Black')
    print(shoes.generate_sku())

