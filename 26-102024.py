#theory of packages 
"""
package:- it contains a group of functions and modules we can import the module to the another package and
use

ex:-
we have a add() and mul() functions in module1.py in the package of pkg.
then we can import

from pkg.module1 import add,mul  #importing add,mul from the module1 in the package alias pkg
"""

from package1.module1 import add,mul
x = 20
y = 30

print(add(x,y))
print(mul(x,y))

