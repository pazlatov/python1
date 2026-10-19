class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_growth(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def show(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self._height = 0
        self._age_days = 0
        self._stats = Plant.Stats()
        self.set_height(height)
        self.set_age(age_days)

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = height

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age_days = age_days

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def grow(self) -> None:
        self.set_height(self._height + 1)
        self._stats.record_growth()

    def age(self) -> None:
        self.set_age(self._age_days + 1)
        self._stats.record_age()

    def show(self) -> None:
        self._stats.record_show()
        print(
            f"{self.name}: {self._height}cm, "
            f"{self._age_days} days old"
        )

    def show_stats(self) -> None:
        self._stats.show()


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
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def show(self) -> None:
            super().show()
            print(f"{self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: int,
        age_days: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree.TreeStats()

    def produce_shade(self) -> None:
        self._stats.record_shade()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

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


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: int,
        age_days: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age_days, color)
        self._seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed_count}")


def display_statistics(plant: Plant) -> None:
    print(f"Statistics for {plant.name}:")
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden Statistics ===")

    print("=== Check Year-Old ===")
    print(f"30 days older than a year? {Plant.is_older_than_year(30)}")
    print(f"400 days older than a year? {Plant.is_older_than_year(400)}")

    print("=== Flower ===")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    display_statistics(rose)

    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("=== Tree ===")
    oak = Tree("Oak", 200, 365, 5.0)
    oak.show()
    display_statistics(oak)

    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed ===")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    display_statistics(sunflower)

    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("=== Vegetable ===")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    tomato.grow()
    tomato.age()
    tomato.show()
    display_statistics(tomato)

    print("=== Anonymous ===")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_statistics(unknown)