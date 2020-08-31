class Category:

  def __init__(self, cat):
    # instance variable
    self.ledger = []
    self.category = cat
    # self.initial_deposit = 0
    self.withdrawals = 0

  def __str__(self):
    title = ("{:*^30}".format(self.category)) + '\n'

    # * A list of the items in the ledger. Each line should show the description and amount.
    # The first 23 characters of the description should be displayed, then the amount.
    # The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    items = ""
    for x in self.ledger:
      items += ("{:23.23}{:>7.2f}".format(x["description"], x["amount"])) + '\n'

    # * A line displaying the category total.
    total = ("Total: {:.2f}".format(self.get_balance()))

    return title + items + total
    

  def deposit(self, amount, description=""):
    
    # set initial deposit
    # if (len(self.ledger) == 0):
    #   self.initial_deposit = amount
    
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
    # * The method should add a withdrawal with the amount and the description
    withdraw_desc = "Transfer to " + str(destination_category.category)

    # * The method should then add a deposit to the other budget category with the amount and the description
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
  # return a string that is a bar chart.
  returing_string = ""

  # add all withdrawls
  # total = sum(x.withdrawals for x in categories)
  total_spent = 0
  for x in categories:
    total_spent += x.withdrawals

  # percentage of spent per category from the total spent
  # percentages = [(x.withdrawals/total)//(1/100) for x in categories]
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
  for y in percentage_spent:
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