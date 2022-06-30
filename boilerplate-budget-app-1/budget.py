class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def __repr__(self):
    title = self.name.center(30, "*")
    body =str()
    for dict in self.ledger:
      amount = dict.get("amount")
      description = dict.get("description")
      amount = "{:.2f}".format(amount)
      description = description[0:23]
      aligned_description = f"{description :<23}"
      aligned_amount = f"{amount:>7}"
      if dict!= self.ledger[-1]: 
        body += aligned_description + aligned_amount + "\n"
      else:
        body += aligned_description + aligned_amount
    total = self.get_balance()
    output = f"{title}\n{body}\nTotal: {total}"
    return output

  def get_balance(self):
    balance = sum(item['amount'] for item in self.ledger)
    return balance

  def check_funds(self, amount):
    if self.get_balance() < amount:
      return False
    else:
      return True
      
  def deposit(self, amount, description = ""):
    deposit = {"amount":amount, "description": description}
    self.ledger.append(deposit)
    return "deposit successful"

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      withdraw_amount = 0 - amount
      withdrawal = {"amount":withdraw_amount, "description": description}
      self.ledger.append(withdrawal)
      return True
    else:
      return False

  def transfer(self, amount, category):
    if self.check_funds(amount):
      destination_name  = category.name
      source_name = self.name
      source_description = f"Transfer to {destination_name}"
      target_description = f"Transfer from {source_name}"

      self.withdraw(amount, source_description)
      category.deposit(amount,target_description)
      return True
    else:
      return False




def create_spend_chart(categories):
    spent_amounts = []
    # Get total spent in each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded down to the nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))
  # Create the bar chart substrings
    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    names = list(map(lambda category: category.name, categories))
    max_length = max(map(lambda name: len(name), names))
    names = list(map(lambda name: name.ljust(max_length), names))
    for x in zip(*names):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")  
   

    