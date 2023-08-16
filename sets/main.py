# Setw (as dictionaries but without keys) does not have duplicates items

set1 = {"Franco", "Axel", "Dante"}
set2 = {"Franco", "nacho"}

#return values that coincide
intersect = set1 & set2

#return not duplicates values
mod = set1 | set2