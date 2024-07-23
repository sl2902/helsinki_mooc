# Write your solution here:
class Series:
    def __init__(self, title: str, n_seasons: int, genre: list):
        self.title = title
        self.n_seasons = n_seasons
        self.genre = genre
        self.ratings = []
    
    def rate(self, rating: int):
        self.ratings.append(rating)
    
    def get_rating_size(self):
        return len(self.ratings)
    
    def get_ratings(self):
        return self.ratings
    
    def get_genres(self):
        return self.genre
    
    def __str__(self):
        if self.get_rating_size() > 0:
            return f'{self.title} ({self.n_seasons} seasons)\ngenres: {", ".join(self.genre)}\n{self.get_rating_size()} ratings, average {sum(self.ratings)/self.get_rating_size():.1f} points'
        return f'{self.title} ({self.n_seasons} seasons)\ngenres: {", ".join(self.genre)}\nno ratings'

def minimum_grade(rating: float, series_list: list) -> Series:
    return [series for series in series_list if max(series.get_ratings()) >= rating]

def includes_genre(genre: str, series_list: list) -> Series:
    return [series for series in series_list if genre in series.get_genres()]

if __name__ == "__main__":
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

