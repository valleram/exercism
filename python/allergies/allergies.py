class Allergies:
    values = [1, 2, 4, 8, 16, 32, 64, 128]
    allergies = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128,
    }
    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        newl = []
        while self.score > 0:
            for i in range(len(Allergies.values)):
                if self.score in Allergies.values:
                    newl.append(self.score)
                    self.score = 0
                    break
                elif self.score > Allergies.values[i]:
                    self.score = self.score - Allergies.values[i]
                    newl.append(Allergies.values[i])
            print(newl)

    @property
    def lst(self):
        pass
