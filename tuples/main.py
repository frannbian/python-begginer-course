# Tuples once be created cannot be modified

tuples = ("Tuple 1", "Tuple 2", "Tuple 3")

tuples[0] # return Tuple 1
tuples.index("Tuper 2") # return 1 (the index)
len(tuples) # count
"Tuple 1" in tuples # return true
tuples[0:2] # return the index 0 to 2

sorted(tuples) # sort

# for editing we need to create a new one
newTuple = tuples + ("Tuple 4")