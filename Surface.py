from Rectangle import Rectangle 

class Surface:
  def __init__(self, image, x, y, height, width):
    self.image = image
    self.rect = Rectangle(x, y, height, width)

  def getRect(self):
    return self.rect