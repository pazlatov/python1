class Plant:
	name: str
	height: int
	age_days: int

	def show(self) -> None:
		print(f"{self.name}: {self.height}cm, {self.age_days} days old")

	def grow(self) -> None:
		self.height += 1

	def age(self) -> None:
		self.age_days += 1

	
if __name__ == "__main__":
	rose = Plant()
	rose.name = "Rose"
	rose.height = 25
	rose.age_days = 30

	starting_height = rose.height

	print("=== Garden Plant Growth ===")
	rose.show()

	for day in range(1, 8):
		print(f"=== Day {day} ===")
		rose.grow()
		rose.age()
		rose.show()


	growth = rose.height - starting_height
	print(f"Growth this week: {growth}cm")
