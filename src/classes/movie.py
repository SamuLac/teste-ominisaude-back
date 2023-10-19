class Movie:
  def __init__(self, title, year, rating, plot, director):
    self.title = title
    self.year = year
    self.rating = rating
    self.plot = plot
    self.director = director

  def getTitle(self):
    return self.title
  
  def getYear(self):
    return self.year

  def getRating(self):
    return self.rating
  
  def getPlot(self):
    return self.plot
  
  def getDirector(self):
    return self.director