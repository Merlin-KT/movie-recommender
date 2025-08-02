
from recommender.movies import MovieRecommender

def main():
      recommender = MovieRecommender("data/movies.csv")
      print("Recommendations for  genre='Adventure',rating=5:")
      print(recommender.recommend(genre='Adventure'))

if __name__ == "__main__":
      main()
