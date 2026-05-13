import random
import re

README = "README.md"

random_id = random.randint(100000, 999999)

with open(README, "r") as f:
    content = f.read()

updated = re.sub(
    r'cachebuster=\d+',
    f'cachebuster={random_id}',
    content
)

with open(README, "w") as f:
    f.write(updated)

print("Updated cachebuster:", random_id)
