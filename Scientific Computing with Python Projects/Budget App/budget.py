class Category:

  def __init__(self, cat):
    self.ledger = []
    self.category = cat
    self.withdrawals = 0

  def __str__(self):
    title = ("{:*^30}".format(self.category)) + '\n'
    items = ""
    for x in self.ledger:
      items += ("{:23.23}{:>7.2f}".format(x["description"], x["amount"])) + '\n'
    total = ("Total: {:.2f}".format(self.get_balance()))
    return title + items + total
  
  def deposit(self, amount, description=""):    
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if (self.check_funds(amount)):

      # add all withdrawls
      self.withdrawals += amount
      
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  # used by check_funds() // hence used by withdraw() and transfer()
  def get_balance(self):
    balance = 0
    for x in self.ledger:
      balance += x["amount"]
    return balance

  def transfer(self, amount, destination_category):
    withdraw_desc = "Transfer to " + str(destination_category.category)
    deposit_desc = "Transfer from " + str(self.category)

    if (self.check_funds(amount)):
      # transfer takes place
      self.withdraw(amount, withdraw_desc)
      destination_category.deposit(amount, deposit_desc)
      return True
    else:
      return False

  # used by withdraw() and transfer()
  def check_funds(self, amount):
    if (self.get_balance() >= amount):
      return True
    else:
      return False

def create_spend_chart(categories):
  returing_string = ""
  cat_length = len(categories)
  total_spent = 0
  for x in categories:
    total_spent += x.withdrawals

  biggest_category_word = 0
  percentage_spent = {}
  for x in categories:
    if biggest_category_word < len(x.category):
      biggest_category_word = len(x.category)
    percentage_spent[x.category] = (x.withdrawals / total_spent) // (1/100)
  
  title = ("Percentage spent by category") + '\n'
  
  chart_line = ""
  for x in range(100, -1, -10):
    chart_line += ("{:3}| ".format(x))
    for key, value in percentage_spent.items():
      if value >= x:
        chart_line += ('o  ')
      else:
        chart_line += ('   ')
    chart_line += '\n'
    dashed_line = "    -"
  
  dashed_line = "    -"
  for y in range(cat_length):
    dashed_line += ('---')
  dashed_line += '\n'

  key_line = ""
  for i in range(biggest_category_word):
    key_line += "     "
    for key, value in percentage_spent.items():
      if i < len(key):
        key_line += key[i] + "  "
      else:
        key_line += "   "

    # skip '\n' at the last line
    if i < biggest_category_word - 1:
      key_line += '\n'

  returing_string = title + chart_line + dashed_line + key_line
  return returing_string