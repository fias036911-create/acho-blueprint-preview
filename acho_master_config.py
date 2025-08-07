class CulturalResonanceLibrary:
    def __init__(self, name):
        self.name = name
        self.ethics = []
        self.symbols = []
        self.metaphors = []
        self.tokens = []

    def load(self, ethics=[], symbols=[], metaphors=[], tokens=""):
        self.ethics += ethics
        self.symbols += symbols
        self.metaphors += metaphors
        self.tokens += tokens.split()

    def map(self):
        return {
            "Culture": self.name,
            "Ethics": self.ethics,
            "Symbols": self.symbols,
            "Metaphors": self.metaphors,
            "Tokens": self.tokens
        }
