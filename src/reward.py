#calculates rewards based on prediction accuracy
#severity levels are represended by integers 1-5

def calculate_reward(predicted, actual):
  difference=abs(predicted-actual)
  reward=max(0.0, 1.0 -(0.25*difference))
  return reward 

#temporarliy test 
print(calculate_reward(5,5))
print(calculate_reward(4,5))
print(calculate_reward(3,5))
print(calculate_reward(2,5))
print(calculate_reward(1,5))

