# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.__brand = brand         # Private attribute (encapsulation)
        self.model = model
        self.storage = storage

    def make_call(self, number):
        print(f"{self.model} is calling {number}...")

    def get_brand(self):
        return self.__brand

# Child Class inheriting from Smartphone
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_type):
        super().__init__(brand, model, storage)
        self.strap_type = strap_type

    def track_steps(self, steps):
        print(f"{self.model} tracked {steps} steps.")

# Create objects
phone = Smartphone("Apple", "iPhone 14", "128GB")
watch = Smartwatch("Apple", "Apple Watch", "32GB", "Silicone")

# Demonstrate functionality
phone.make_call("0712345678")
print(f"Phone Brand: {phone.get_brand()}")

watch.make_call("0711122233")  # Inherited method
watch.track_steps(5000)
print(f"Smartwatch Brand: {watch.get_brand()}")
