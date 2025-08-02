
import pandas as pd

class MovieRecommender:
  def __init__(self, csv_path):
    self.data = pd.read_csv(csv_path)

  def recommend(self, title=None, genre=None, rating=None):
    result = self.data
    if title:
      result = result[result['title'].str.lower() == title.lower()]
    if genre:
      result = result[result['genre'].str.lower() == genre.lower()]
    if rating:
      result = result[result['rating'].str.lower() == rating.lower()]
    return result['title'].tolist()

