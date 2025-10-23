class Unit:
  
  def __init__(self, name, value):
    self._name = name
    self._value = value

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    self._name = name

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    self._value = value