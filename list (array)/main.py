list = ['Franco', 'Dante', "Axel", 2, True]

# Check if exist one value
"Franco" in list

# show value of Index
list[0]

#updating a value
list[2] = "Zarasa"

#last element
list[-1]

#part of a list
list[2:4]

#first to n
list[:3]

#count 
len(list)

#adding new
list.append('guau')

#merge another list
list.extend([12, 34, "Franco"])
list += ['zarazasa']

#removing
list.remove("zarazasa")

# remove last  item
list.pop()

# insert a value in a specific index
list.insert(3, "testing")
list[1:1] = ['Zarasa', 2]

#sorting a list (always has to be same type of value)
list.sort()

#sorting a list ignoring uppercase letters
list.sort(key = str.lower)

#sorting a list ignoring uppercase letters
list.sort(key = str.lower)

