from collections import OrderedDict 



x = 1
ing_dict = dict()
ing_list = []
j = 0
with open("set-a.txt", 'r') as file:   
	data = file.readlines()
	for line in data:
		if x == 1:
			data1 = list(map(int, line.split()))
			number_of_pizza = data1[0]
			number_of_2_member_teams = data1[1]
			number_of_3_member_teams = data1[2]
			number_of_4_member_teams = data1[3]
			x = 2
		else:
			data1 = line.strip().split()
			ing_count = int(data1[0])
			ings = data1[1:]
			ing_dict[j] = ing_count
			j+=1
			ing_list.append(sorted(ings))

	dict1 = OrderedDict(sorted(ing_dict.items())) 
	teams_delivered = 0
	n = 0
	available_pizzas = number_of_pizza
	i = 1
	while i <= number_of_pizza:
		if ((available_pizzas - 4) > 1 or available_pizzas % 4 == 0) and number_of_4_member_teams > 0 :
			number_of_4_member_teams -=1					
			available_pizzas -= 4
			i +=4
			teams_delivered += 1
			print(4, n, end = " ")
			n+=1
			print(4, n, end = " ")
			n+=1
			print(4, n, end = " ")
			n+=1
			print(4, n)
			n+=1
		elif ((available_pizzas - 3) > 1 or available_pizzas % 3 == 0) and number_of_3_member_teams > 0:
			number_of_3_member_teams -= 1
			available_pizzas -= 3
			i += 3
			teams_delivered += 1
			print(3, n, end = " ")
			n+=1
			print(3, n, end = " ")
			n+=1
			print(3, n)
			n+=1
		elif ((available_pizzas - 2) > 1 or available_pizzas % 2 == 0) and number_of_2_member_teams > 0:
			number_of_2_member_teams -= 1
			available_pizzas -= 2
			i += 2
			teams_delivered += 1
			print(2, n, end = " ")
			n+=1
			print(2, n)
			n+=1

	#print(number_of_pizza, number_of_2_member_teams, number_of_3_member_teams, number_of_4_member_teams)
	#print(ing_count, ings)
	#print(ing_dict)
	#print(ing_list)
	#print(dict1)
	#print(teams_delivered)




	#Only one issue left if all ingredients match then!! ----- join -> not in -> separate list to hold undelivered
	# finalyy check and deliver
	# 1-hkdsghkdgsfkkgshfghk in 2-dshakjfkdhakfhakkahsfkjhakj