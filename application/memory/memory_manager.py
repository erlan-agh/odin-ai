class MemoryManager:
    def __init__(self):
        self.history = []

    def remember(self, item):
        self.history.append(item)

    def recall(self):
        return self.history
