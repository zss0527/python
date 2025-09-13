import pizza # import the entire module
from mutiple_functions import function2, function3 # import specific functions from a module
from pizza import make_pizza as mp # aliasing a functin name
import pizza as p # aliasing a module name
from pizza import * # import all functions from a module

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

function2()
function3()

mp(20, 'extra cheese', 'bacon', 'pineapple')

p.make_pizza(18, 'sausage', 'jalapenos', 'onions')

make_pizza(14, 'pepperoni')