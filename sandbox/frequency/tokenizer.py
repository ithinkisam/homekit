import re
from domain import transformation, units

class TransformationTokenizer:

  def tokenize(format_string):
    code = re.sub(r"[+-]\d*", "", format_string)
    unit = units.by_value(code)
    if not unit:
      raise Exception(f"No unit found for code {code}")
    amount = int(re.sub(r"[^\d]", "", format_string))
    return transformation.Transformation(amount, unit)
