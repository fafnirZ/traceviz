import re
from store import allNodeMaps, allNodeSignatures, allDirectedEdges
from model import FunctionNode

def scanFile(file_path: str):
  with open(file_path, "r") as f:
    for function_block in getFunctionBlock(f):
      function_signature = getFunctionNameOnly(function_block[0])
      if function_signature not in allNodeSignatures:
        # add to cache
        allNodeSignatures.add(function_signature)
        # add to hashmap for fast retrieval
        allNodeMaps[function_signature] = FunctionNode(function_signature)
      # print(function_signature, end="")
      for function_call in getFunctionCalls(function_block):
        # edges
        edge = (function_signature, getFunctionNameOnly(function_call))
        if edge not in allDirectedEdges:
          allDirectedEdges.add(edge)
          # print()


def getFunctionBlock(file):
  """
  uses a generator
  get all function blocks

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
  block = []
  for line in file:
    match = re.match("def [a-zA-Z_][a-zA-Z0-9_]*\s*\(.*\)\s*(\s*\->.+\s*)*:", line)
    if match:
      start = True
      block.append(line)
    elif re.match("\s+.+", line):
      # anything indented
      block.append(line)
    else:
      yield block
      # reset block
      block = []

  # at the end yield block
  yield block


def getFunctionCalls(block):
  for line in block:
    match = re.match("\s*([a-zA-Z_][a-zA-Z0-9_]*\(.*\))", line)
    if match:
      yield match.group(1)


def getFunctionNameOnly(function_call_or_signature: str):
  match = re.match("(def\s)*([a-zA-Z_][a-zA-Z0-9_]+)", function_call_or_signature)
  if match:
    return match.group(2)



# scanFile("inputs/samefile.py")
# print(allNodeMaps["function1"].calls)
# print(allNodeMaps["function2"].calls)

