# traceviz

this program accepts python3 files as input

it scans every file for the function declaration `signatures` and stores as a Node
then it scans every file and parses every function as a `function block`
within each function block, it scans for function calls and if the function call signature exists, it will create an edge between the current function node, and the function call node.

Edges:
(src, dest)
i.e. function `src` calls, function `dest`

example
-------
```
fun1():
  pass

fun2():
  fun1()

nodes:
[fun1, fun2]

edges:
[(fun2, fun1)]
```