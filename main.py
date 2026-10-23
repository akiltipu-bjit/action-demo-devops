"""A tiny greeting app for a GitHub Actions lesson."""


def greet(name: str = "World") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
