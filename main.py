#inputs:
#how many different types of weights and how many of each
#store info in a hashmap

def weight_combination(weights, lift_target):
  weights.sort()
  possible_combos = list()
  def backtrack(curr, index, lift_target):
    if lift_target == 0:
      possible_combos.append(curr.copy())
    if lift_target <= 0:
      return

    prev = -1
    for x in range(index,len(weights)):
      if weights[x] == prev:
        continue
      curr.append(weights[x])
      backtrack(curr, x+1, lift_target - weights[x])
      curr.pop()
      prev = weights[x]
  backtrack([],0,lift_target)
  return possible_combos


asking = True
weights_info = dict()
while asking:
  try:
    barbell_weight= int(input("barbell weight: ")) 
    asking = False
  except ValueError:
    print("invalid input")

asking = True
while asking:
  user_input = input("input plate weight (type 'f' and enter if you have entered all your weight): ")
  if user_input == "f":
    asking = False
    break
  else:
    try:
      user_input = int(user_input)
      try:
        user_input_2 = int(input("input how many plates you have (of that weight): "))
        weights_info[user_input] = user_input_2
      except ValueError:
        print("invalid input")
    except ValueError:
      print("invalid input")

weights_info = {45: 2, 35: 2, 25: 2, 5: 2, 2.5: 2}
barbell_weight = 45
print("enter lift amount (we will calculate how many plates you have to put on each side of the bar)")
lift_amount = int(input("input: "))
lift_amount -= barbell_weight
lift_amount /= 2

# print(lift_amount)
# print(list(weights_info))

# plates = (list(weights_info))

weights_list_for_one_side = list()
for weight, amount in weights_info.items():
  print(amount,weight)
  for x in range(amount//2):
    weights_list_for_one_side.append(weight)

print(weights_list_for_one_side)
print(weight_combination([45,45],lift_amount))
