#initialize my_set
my_set={1,3}
print(my_set)

#my_set[0]
#if you uncomment the above line you will get an error
#TypeError: 'set' object is not subscriptable

#add an element
my_set.add(2)
print(my_set)

#add multiple elements #
my_set.update([2,3,4])
print(my_set)

#add list and set #
my_set.update([4,5],{1,6,8})
print(my_set)

#discard an element #
my_set.discard(4)
print(my_set)

#remove an element #
my_set.remove(6)
print(my_set)

#discard an element not present in my_set
my_set.discard(2)
print(my_set)
#remove an element not present in my set you will get an error

my_set=set("HelloWorld")
print(my_set)

#pop an element #
print(my_set.pop())

#pop another element
my_set.pop()
print(my_set)

#clear
my_set.clear()
print(my_set)