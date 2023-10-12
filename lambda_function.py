"""
Lambda functions return anonymous functions.

Syntax: lambda variable, ...: expression
"""

# Example 1
# declare a lambda function
greet = lambda : print("Hello, world!")
# call the lambda function
greet()

# Example 2
# declare a lambda function wtih one parameter
greet_with_name = lambda name: print(f"Hello, {name}!")
# call the lambda function
greet_with_name("KL")

# Example 3
print(sorted(["A", "b", "C"], key=lambda x: x.lower()))
print("***")
print(sorted(["A", "b", "C"]))

# Example 4: Pandas related example
df["new_column"] = df["column"].apply(lambda x: x + 1)

# Example 5: Pandas related example
df_grouped_by = df.groupby("column")
df = df_grouped_by.apply(lambda x: x.sample(10))
