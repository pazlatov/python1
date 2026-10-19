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

if __name__ == "__main__":
	print("=== Garden Security System ===")

	rose = Plant("Rose", 15, 10)
	rose.show()

	rose.set_height(25)
	rose.set_age(30)
	rose.show()

	rose.set_height(-5)
	rose.set_age(-10)

	print(f"Current height: {rose.get_height()}cm")
	print(f"Current age: {rose.get_age()} days")

	print("=== Invalid Starting Values ===")
	cactus = Plant("Cactus", -5, -10)
	cactus.show()