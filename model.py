import re
"""
important 
right now ignores whether
function()
function(1)
function(1,2,3)

we treat it all as the same signature "function"
"""

class FunctionNode:
  """
  Properties
    calls -> list[*FunctionNodes]
    signature -> def ...()->:
  """
  def __init__(self, signature: str):
    self.signature = signature
    self.calls = []

