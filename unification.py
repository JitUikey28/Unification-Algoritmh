# Function to check if a term is a variable
def is_variable(term):
    return isinstance(term, str) and term.islower()

# Unification function
def unify(x, y, theta={}):
    # Base cases
    if theta is None:
        return None
    elif x == y:
        return theta
    elif is_variable(x):
        return unify_var(x, y, theta)
    elif is_variable(y):
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

# Function to unify a variable with a term
def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    elif occurs_check(var, x, theta):
        return None
    else:
        theta[var] = x
        return theta

# Occurs check to prevent infinite loops (var occurring in term)
def occurs_check(var, x, theta):
    if var == x:
        return True
    elif is_variable(x) and x in theta:
        return occurs_check(var, theta[x], theta)
    elif isinstance(x, list):
        return any(occurs_check(var, xi, theta) for xi in x)
    return False

# Example usage
x = ['f', 'x', 'y']
y = ['f', 'a', 'b']

result = unify(x, y)
if result:
    print("Unification successful with substitutions:", result)
else:
    print("Unification failed.")
