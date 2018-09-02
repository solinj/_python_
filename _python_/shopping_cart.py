class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""

  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_cart = {}
  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."






class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

  def display_customer_id(self):
    print "Customer id is %s." % (str(self.customer_id))

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
