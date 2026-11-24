import os

LINES = [
    "Don't lend your charger to the man in seat 14B on the flight to Jakarta.",
    "He walked off the plane with it, and that's why you now carry two chargers and never trust a stranger at 30,000 feet.",
]

TEXT = "\n".join(LINES)


def main():
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
