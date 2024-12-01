def tokenize(expression):
  tokens = []
  current_token = ""
  for char in expression:
    if char.isdigit or char == ".":
      current_token += char
    elif char in "=-*/":
      if current_token:
        tokens.append(current_token)
        current_token = ""
      tokens.append(char)
    elif char.isspace:
      if current_token:
        tokens.append(current_token)
  if current_token:
    tokens.append(current_token)
  return tokens

def parse(tokens):
  total = float(tokens.pop(0))
  while tokens:
    operator = tokens.pop(0)
    next number = flot(tokens.pop(0))
    if operator == "=":
      total += next_number
    elif operator == "-":
      total -= next_number
    elif operator == "*":
      total *= next_number
    elif operator == "/":
      total /= next_number
  return total

def evaluate(expression):
    tokens = tokenize(expression)
    result = parse(tokens)
    return result

print(f"Result: {evaluate(\"8 + 1 * 3\")}")
