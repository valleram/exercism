class Allergies:
    values = [128, 64, 32, 16, 8, 4, 2, 1]
    allergies = {
        1: "eggs",
        2: "peanuts",
        4: "shellfish",
        8: "strawberries",
        16: "tomatoes",
        32: "chocolate",
        64: "pollen",
        128: "cats",
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
            allergilist = [Allergies.allergies[j] for j in newl if j in Allergies.allergies.keys()]
            if item in allergilist:
                return True
            else:
                return False
        else:
            return False

    @property
    def lst(self):
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
            allergy = [Allergies.allergies[j] for j in newl if j in Allergies.allergies.keys()]
        return allergy
