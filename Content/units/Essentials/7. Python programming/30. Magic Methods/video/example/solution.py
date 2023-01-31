class FantasticBook:
    def __init__(self):
        self.title = 'The Fantastic Adventure'
        self.pages = [
            "It was the crack of dawn...",
            "...disaster strikes...",
            "...and they lived happily ever after"
        ]
        self.blurb = "A high octane thriller"

    def __len__(self):
        return len(self.pages)

    def __getitem__(self, idx):
        return self.pages[idx]

    def __str__(self):
        return f"{self.title}\n{' '.join(self.pages)}"
