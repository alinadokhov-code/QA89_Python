def greet(name):
    return f"Hi,{name}!"
result = greet("Kristina")
print(result)

# res1 = greet()
# print(res1)

def create_user(name, role="user"):
    return {
        "name": name,
        "role": role
    }

print(create_user("Kristina"))
print(create_user("Kristina", "admin"))
print()

def calculate_discount(price, discount=10):
    return price - (price * discount / 100)
print(calculate_discount(1000))
print(calculate_discount(1000, 25))

#def foo(a=1,b):
#    return a+b
#print(foo(5))

def add_test_res(name,results=None):
    if results is None:
        results = []
    results.append(name)
    return results
print(add_test_res("test_login"))
print(add_test_res("test_logout"))

def create_user1(username, email, role):
    return f"{username}, {email}, {role}"

print(create_user1("Kristina",role="admin",email="kris@gm.com"))
