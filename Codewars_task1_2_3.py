#Convert a Number to a String!

def number_to_string(num):
    return str (num)
    # Return a string of the number here!

#Reversing Words in a String

def reverse(st):
    a = st.split()
    b = a[::-1]
    c = ' '.join(str(x) for x in b)
    return c
#Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

