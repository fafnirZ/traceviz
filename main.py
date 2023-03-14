import re

def scanFile(file_path: str):
  with open(file_path, "r") as f:
    getFunctionSignatures(f)


def getFunctionSignatures(file):
  """
  get all function signatures

  regex rules:
  must start with def
  first letter cannot be numeric: 
    [a-zA-Z_]
  next letter can be alphanumeric,_ or null: 
    [a-zA-Z0-9_]*
  optional space: 
    \s*
  inside parenthesis: 
    \(.*\)
  optional space: 
    \s*
  optional return type declaration: 
    (\s*\->.+\s*)*
  required colon: 
    :
  """
  signatures = []

  for line in file:
    match = re.match("def [a-zA-Z_][a-zA-Z0-9_]*\s*\(.*\)\s*(\s*\->.+\s*)*:", line)
    print(match)


scanFile("inputs/samefile.py")