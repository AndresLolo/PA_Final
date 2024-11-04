class Maybe:
    def __init__(self, value):
        self.value = value
    
    def is_nothing(self):
        return self.value is None
    
    def bind(self, func):
        if self.is_nothing():
            return self
        return func(self.value)
    
    def __str__(self):
        return f"Maybe({self.value})" if not self.is_nothing() else "Maybe(None)"