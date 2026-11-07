from __future__ import annotations
import ast
ALLOWED = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.Load)
def safe_eval(expr: str) -> float:
    tree = ast.parse(expr, mode="eval")
    for node in ast.walk(tree):
        if not isinstance(node, ALLOWED):
            raise ValueError("disallowed expression")
    return float(eval(compile(tree, "<sandbox>", "eval"), {"__builtins__": {}}, {}))
