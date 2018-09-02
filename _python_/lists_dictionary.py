from datetime import datetime
print("today is %02d-%02d-%04d" % (datetime.now().day, datetime.now().month, datetime.now().year))

# Lists are a datatype you can use to store
# a collection of different pieces of information
# as a sequence under a single variable name.
# list.index("element of the list")
# list.insert("index", "element to insert")
# list.sort()
# EXAMPLE OF DICTIONARY :
d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
# del dict_name[key_name]
beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")

# PRINT EVERY ELEMENT OF A DICTIONARY
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Dab": "A small amount."
}
for w in webster:
  print webster[w]


prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for food in prices:
  print food
  print "price: %s" % prices[food]
  print "stock: %s" % stock[food]


print('___________________________________________________')
n = [3, 5, 7]
def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

print double_list(n)
