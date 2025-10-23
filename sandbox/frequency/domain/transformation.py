from domain.units import Units

class Transformation:
  
  def __init__(self, amount = 0, unit = Units.none):
    self._amount = amount
    self._unit = unit

  @property
  def amount(self):
    return self._amount
  
  @property
  def unit(self):
    return self._unit
