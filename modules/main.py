# Modules

# import thw whole module
import dog;
dog.bark()

#Import only one funtion or part
from dog import bark
bark()

from cat import cat

cat.bark()

from cat.cat import bark
bark()