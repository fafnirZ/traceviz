import re
from store import allNodeMaps, allNodeSignatures, allDirectedEdges
from model import FunctionNode

def scanFile(file_path: str):
  with open(file_path, "r") as f:
    """
    first pass for function signatures
    TODO first pass second pass should be for entire glob files
    """
    for function_block in getFunctionBlock(f):
      function_signature = getFunctionNameOnly(function_block[0])
      if function_signature == None:
        continue
      if function_signature not in allNodeSignatures:
        # add to cache
        allNodeSignatures.add(function_signature)


    """
    second pass for function calls
    """
    for function_block in getFunctionBlock(f):
      for function_call in getFunctionCalls(function_block):
        function_call_name_only = getFunctionNameOnly(function_call)
        if function_signature not in allNodeSignatures:
          continue
        if function_call_name_only not in allNodeSignatures:
          continue

        # edges
        edge = (function_signature, function_call_name_only)
        if edge not in allDirectedEdges:
          # ignore duplicates
          allDirectedEdges.add(edge)


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
