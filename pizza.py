#introduction to python modules

"""def make_pizza(*toppings):
    print the lits of toppings that have been requested
    print(toppings)


make_pizza('pepperoni')
make_pizza('corn','extracheese','olives')"""

#obj --> size, toppings...print out requested toppings in seperatley

def make_pizza(size,*toppings):
    """summarize the pizzas we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")


make_pizza(12,'corn','tomatoes','olives')
make_pizza(16,'extracheese','chicken')


