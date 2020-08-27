
def arithmetic_arranger(problems, display=False):
  no_of_probems = len(problems)
  
  
  line1 = []
  operator = []
  line2 = []

  str_len = 0
  new_line1 = []
  new_line2 = []
  new_line3 = [] # dashes
  new_line4 = [] # answers

  for i in problems:
    a, op, b = i.split()
    # error: test_too_many_problems(self)
    if no_of_probems > 5:
      return "Error: Too many problems."
    # error: test_incorrect_operator(self)
    elif op != '+' and op != '-':
      return "Error: Operator must be '+' or '-'."
    # error: test_too_many_digits(self)
    elif len(a) > 4 or len(b) > 4:
      return "Error: Numbers cannot be more than four digits."
    # error: test_only_digits(self)
    elif a.isdigit() == False or b.isdigit() == False:
      return "Error: Numbers must only contain digits."
    else:
      operator.append(op)
      line1.append(a)
      line2.append(b)

  for i in range(no_of_probems):
    if int(line1[i]) > int(line2[i]):
      str_len = len(line1[i])
      # print("{}: length: {}".format(line1[i], str_len))
    else:
      str_len = len(line2[i])
      # print("{}".format(line2[i]))
    
    new_line1.append("  {:>{}}".format(line1[i], str_len))
    new_line2.append(operator[i] + " {:>{}}".format(line2[i], str_len))
    new_line3.append("{:->{}}".format("", (str_len + 2)))
    
    if operator[i] == '+':
      total = int(line1[i]) + int(line2[i])
    elif operator[i] == '-':
      total = int(line1[i]) - int(line2[i])

    # error: test_solutions(self)
    if total >= 0:
      new_line4.append("  {:>{}}".format(total, str_len))
    else:
      new_line4.append(" {:>{}}".format(total, str_len))

  str1 = "    ".join(new_line1)
  str2 = "    ".join(new_line2)
  str3 = "    ".join(new_line3)
  str4 = "    ".join(new_line4)

  if display:
    print(str1)
    print(str2)
    print(str3)
    print(str4)
    arranged_problems = (str1 + "\n" + str2 + "\n" +  str3 + "\n" +  str4)
  else:
    print(str1)
    print(str2)
    print(str3)
    arranged_problems = (str1 + "\n" + str2 + "\n" +  str3)    
    
  return arranged_problems
