class Plant:
	def __init__(self, name: str, height: int, age_days: int) -> None:
		self.name = name
		self._height = 0
		self._age_days = 0
		self.set_height(height)
		self.set_age(age_days)

	def set_height(self, height: int) -> None:
		if height < 0:
			print(f"{self.name}: Error, height cant be negative")
		else:
			self._height = height
	
	def set_age(self, age_days: int) -> None:
		if age_days < 0:
			print(f"{self.name}: Error, age cant be negative")
		else:
			self._age_days = age_days

	def get_height(self) -> int:
		return self._height
	
	def get_age(self) -> int:
		return self._age_days
	
	def grow(self) -> None:
		self.set_height(self._height + 1)

	def age(self) -> None:
		self.set_age(self._age_days + 1)

	def show(self) -> None:
		print(f"{self.name}: {self._height}cm, {self._age_days} days old")

class Flower(Plant):
	def __init__(
			self,
			name: str,
			height: int,
			age_days: int,
			color: str,
	) -> None:
		super().__init__(name, height, age_days)
		self.color = color
		self.has_bloomed = False

	def bloom(self) -> None:
		self.has_bloomed = True

	def show(self) -> None:
		super().show()
		print(f"Color: {self.color}")
		if self.has_bloomed:
			print(f"{self.name} is blooming beautifully!")
		else:
			print(f"{self.name} has not bloomed yet")
class Tree(Plant):
	def __init__(
			self,
			name: str,
			height: int,
			age_days: int,
			trunk_diameter: float,
	) -> None:
		super().__init__(name, height, age_days)
		self.trunk_diameter = trunk_diameter

	def produce_shade(self) -> None:
		print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide")

	def show(self) -> None:
		super().show()
		print(f"Trunk diameter: {self.trunk_diameter}cm")

class Vegetable(Plant):
	def __init__(
			self,
			name: str,
			height: int,
			age_days: int,
			harvest_season: str,
	) -> None:
		super().__init__(name, height, age_days)
		self.harvest_season = harvest_season
		self.nutritional_value = 0
	
	def grow(self) -> None:
		super().grow()
		self.nutritional_value += 1

	def age(self) -> None:
		super().age()
		self.nutritional_value += 1
	
	def show(self) -> None:
		super().show()
		print(f"Harvest season: {self.harvest_season}")
		print(f"Nutritional value: {self.nutritional_value}")

if __name__ == "__main__":
	print("=== Garden Plant Types ===")

	print("=== Flower ===")
	rose = Flower("Rose", 15, 10, "red")
	rose.show()
	rose.bloom()
	rose.show()

	print("=== Tree ===")
	oak = Tree("Oak", 200, 365, 5.0)
	oak.show()
	oak.produce_shade()

	print("=== Vegetable ===")
	tomato = Vegetable("Tomato", 5, 10, "April")
	tomato.show()

	for day in range(20):
		tomato.grow()
		tomato.age()

	tomato.show()