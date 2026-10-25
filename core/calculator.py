print("ZED Calculator v1.5");
try:
    expr=input("Calc (e.g 1+1): ")
    print(f"Result: {eval(expr)}")
except Exception as e:
    print(f"Error: {e}")