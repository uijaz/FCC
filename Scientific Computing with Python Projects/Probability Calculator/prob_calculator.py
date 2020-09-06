import copy
import random
# Consider using the modules imported above.

class Hat:

	def __init__(self, **hat):
		self.contents = []
		if (len(hat) > 0):
			self.contents = dict_to_list(hat)
		else:
			print("Please add balls in the hat")

	def draw(self, number_of_balls_to_draw):
		draw_list = []
		if (number_of_balls_to_draw <= len(self.contents)):
			for i in range(number_of_balls_to_draw):
				random_item_from_list = random.choice(self.contents) # random pick
				draw_list.append(random_item_from_list) # add random pick to new list
				self.contents.remove(random_item_from_list) # removed random pick
		else:
			return self.contents
		return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	M = 0
	newlist = []

	# run experiments
	for N in range(num_experiments):
		new_hat = copy.deepcopy(hat)

		# draw balls
		draw = new_hat.draw(num_balls_drawn)
		newlist.append(draw)

		# # convert to dictionary
		d = list_to_dict(draw)

		answer = True
		# compare expected dict to drawn dict
		for i in expected_balls:
			if (i not in d or d[i]<expected_balls[i]):
				answer = False
				break
		if answer:
			M += 1
			
	probablity = (M / num_experiments)
	return probablity

# used by Hat.__init__()
def dict_to_list(hat):
	contents = []
	if (len(hat) > 0):
		for key, values in hat.items():
			for value in range(values):
				contents.append(key)
	return contents

# used by experiment()
def list_to_dict(list):
	dict = {}
	for i in list:
		dict[i] = list.count(i)
	return dict