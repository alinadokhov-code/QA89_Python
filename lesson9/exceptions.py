#with open("user.json","r",encoding="utf-8") as file:
   # print(file.read())

#result = 10/0
#print(result)
#print("End program")

def is_number(text):
    try:
        float(text)
        return True
    except (ValueError, TypeError):
        return False
print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("Hello"))
print(is_number(None))