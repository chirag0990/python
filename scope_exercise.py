# write a program that demonstrates the concept of scope in Python

# we have variables and function names

# address 
# cabinet_items
# basement_items 
# print()

# From the prescriptive of the mouse in the cabinet, order them into four scope.

# 1. local scope
def address():
    """This function returns the address of the user"""
    address = "3/3, Krushna Nagar, Ahmedabad, Gujarat, India"
    print(f" Adress: {address}")
    return address
address ()

def cabinet_items():
    """This function returns the items in the cabinet"""
    cab_items = ["mouse", "keyboard", "monitor"]
    print(f"items int the cabinet: {cab_items}")
    return cab_items
cabinet_items()

def basement_items():
    """This function returns the basement items"""
    bas_items = ["boxs", "furnitures", "tools"]
    print(f"the items in the basement: {bas_items}")
    return bas_items
basement_items()

def print_items():
    """ This function returns the cabinet items and basement items from the address"""
    items = cabinet_items() + basement_items()
    print(f"Items in the address: {items}")
    return items
print_items()


# program that demonstrates the concept of scope in Python
def exploring_basement():
    """This function explores the basement items and prints them"""
    def exploring_cabinet():
        """This function explores the cabinet items and prints them"""
        cabinet_items = ["mouse", "keyboard", "monitor"]# local scope
        print(f"Items in the cabinet: {cabinet_items}") 
    
    basement_items =  ["boxs", "furnitures", "tools"] # exclosing scope
    print(f"Items in the basement: {basement_items}")
    exploring_cabinet() 

address = "3/3, Krushna Nagar, Ahmedabad, Gujarat, India" # global scope
exploring_basement()
print(f"Address: {address}") # buil-in scope

# exersie

def exporing_basement():
    """This function explores the basement items and prints them"""
    def exploring_cabinet():
      """This function explores the cabinents the  items and prints them"""
      address = "Cookie cabinet" # local scope
      cabinet_items = ["biscuits", "chocolate", "chips"] # local scope
      print(f"Items in the cabinet: {cabinet_items} in {address}")

    adress = "Mouse House" # enclosing scope
    basement_items = ["boxs", "furnitures", "tools"] # enclosing scope
    print(f"Items in the basement: {basement_items} in {adress}")
    exploring_cabinet()

address = "Python palace" # global scope
exporing_basement()
print(f"Address: {address}")  # built-in scope

# global scope
def exporing_basement():
    """This function explores the basement items and prints them"""
    def exploring_cabinet():
      
      """This function explores the cabinents the  items and prints them"""
      global address
      address = "Cookie cabinet" # local scope
      print(f"Items in the cabinet: {address}")

    address = "Mouse House" # enclosing scope
    print(f"Items in the basement: {address}")
    exploring_cabinet()

address = "Python palace" # global scope
exporing_basement()
print(f"Address: {address}")  # built-in scope

""" You also want to invite a bear to the party. 
To make sure the bear receives the invitation, you decide to hand it over personally. 
That’s pretty nice."""

def visit_woods(my_invitation):
    "this function visits the woods and provide invitation to the bear"
    if "my_invitation" in locals():
        print(f"Bear, you are invited: {my_invitation}")

invitation = "let's have a party!"  # global scope
visit_woods(invitation)

# coockie task 

def on_the_self():
    """this function used for collected the cookies from the list"""
    coockies = ["Penaut", "Chocolate"]
    print(f"Coockies on the self: {coockies}")
    return coockies

def under_the_sofa():
    """this function used for collected the cookies from the list"""
    coockies = ["Oat", "Salted Caramel"]
    print(f"Coockies under the sofa: {coockies}")
    return coockies

#coockies = []
#coockies += on_the_self()  # collect cookies from the self
#coockies += under_the_sofa()  # collect cookies from under the sofa

coockies = on_the_self() + under_the_sofa()  # collect cookies from both places
print(f"Coockies collected: {coockies}")

# Exercise : last line printing the address of the mouse in the cabinet
def explore_cabinets():
    """This function explores the cabinets and prints the items"""
    def explore_drawers():
        """This function explores the drawers and prints the items"""
        address = "Cookie cabinet"
        print(f"Items in the drawers: {address}")
    explore_drawers()
    address = "Mouse House"  # enclosing scope
    print(f"Items in the cabinets: {address}")
    return address
address = "Python palace"  # global scope
address = explore_cabinets()
print(f"Address: {address}")  # built-in scope

# above code write a much cleaner way 

def expore_cabinets():
    """This function explores the cabinets and prints the items"""
    def explore_drwers():
        """This function explores the drawers and prints the items"""
        address = "Cookie cabinet"
        print(f"Items in the drawers: {address}")
    
    address = "Mouse House"  # enclosing scope
    explore_drwers()
    print(f"Items in the cabinets: {address}")
    return address
address = "Python palace"  # global scope
print(f"Address: {address}")  # built-in scope


def explore_cabinets(address):
    """This function explores the cabinets and prints the items"""
    def explore_drawers(address):
        """This function explores the drawers and prints the items"""
        address = "Cookie cabinet"
        print(f"Items in the drawers: {address}")
        return address
    explore_drawers(address)
    address = "Mouse House"  # enclosing scope
    print(f"Items in the cabinets: {address}")
    return address
address = "Python palace"  # global scope
explore_cabinets(address)
print(f"Address: {address}")  # built-in scope
