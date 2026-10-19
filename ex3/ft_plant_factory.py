class Plant:
	def __init__(self, name: str, height: int, age_days: int) -> None:
		self.name = name
		self.height = height
		self.age_days = age_days

	def show(self) -> None:
		print(f"{self.name}: {self.height}cm, {self.age_days} days old")

	def grow(self) -> None:
		self.height += 1

	def age(self) -> None:
		self.age_days += 1

	
if __name__ == "__main__":
	print("=== Plant Factory Output ===")

	rose = Plant("Rose", 25, 30)
	rose.show()

	oak = Plant("Oak", 200, 365)
	oak.show()

	cactus = Plant("Cactus", 5, 90)
	cactus.show()

	sunflower = Plant("Sunflower", 80, 45)
	sunflower.show()

	fern = Plant("Fern", 15, 120)
	fern.show()