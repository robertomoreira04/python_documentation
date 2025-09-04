class Dev:
    def __init__(self, name, stack):
        self.name = name
        self.stack = stack

    def __str__(self):
        return f"{self.name} -> {', '.join(self.stack)}"

    # não precisa de self nem cls
    @staticmethod
    def is_modern_language(language):
        modern = {"Python", "JavaScript", "Go", "Rust"}
        return language in modern


roberto = Dev("Roberto", ["Python", "Django", "FastAPI"])
print(roberto)

print(Dev.is_modern_language("Python"))   # Saída: True
print(Dev.is_modern_language("Cobol"))    # Saída: False


