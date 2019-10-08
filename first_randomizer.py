import random

color = ["fuchsia",
		 "hot pink",
		 "lavender",
		 "neon orange",
		 "gray"]

decorative_item = ["flowers",
				   "UFOs",
				   "lizards",
				   "cowboy boots",
				   "dragons"]

random_color = random.choice(color)
random_decorative_item = random.choice(decorative_item)


print(f"How about you knit a sweater with {random_color} {random_decorative_item}?") 