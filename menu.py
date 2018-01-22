with open('menu.txt', 'a') as menu_file:
	print('Pozdravljeni. Prosim vnesite današnji datum in jedi na meniju.')
	date = input('Današnji datum: ')
	menu_file.write('Meni za dan: ' + date + '\n' + '\n')


	def add_dish():

		dish_name = input('Vnesite jed na današnjem meniju: ')
		dish_price = input('Vnesi ceno za jed: {} '.format(dish_name))
		dish = dish_name + ' ' + '$' + dish_price
		menu_file.write(dish + '\n')


	add_dish()

	new = input('Želite vnesti še kakšno jed? y/n')

	while new == 'y':
		add_dish()
		new = input('Želite vnesti še kakšno jed? y/n')

	menu_file.write('\n')
	print('Hvala. Lep dan.')
