class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        year_second = 31557600
        total = round(self.seconds / year_second, 2)
        return total

    def on_mercury(self):
        equivalent = round(0.2408467 * 31557600, 2)
        year_second = round(self.seconds / equivalent, 2)
        return year_second

    def on_venus(self):
        equivalent = round(0.61519726 * 31557600, 2)
        year_second = round(self.seconds / equivalent, 2)
        return year_second

    def on_mars(self):
        equivalent = round(1.8808158 * 31557600, 2)
        year_second = round(self.seconds / equivalent, 2)
        return year_second

    def on_jupiter(self):
        equivalent = round(11.862615 * 31557600, 2)
        year_second = round(self.seconds / equivalent, 2)
        return year_second

    def on_saturn(self):
        equivalent = round(29.447498 * 31557600, 2)
        year_second = round(self.seconds / equivalent, 2)
        return year_second

    def on_uranus(self):
        equivalent = round(84.016846 * 31557600, 2)
        year_second = round(self.seconds / equivalent, 2)
        return year_second

    def on_neptune(self):
        equivalent = round(164.79132 * 31557600, 2)
        year_second = round(self.seconds / equivalent, 2)
        return year_second

