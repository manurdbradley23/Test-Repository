#Takes the user input's selected month number and gives the total days.
dictionary ={'1': 31,'2': 28,'3': 31,'4': 30,'5': 31,'6': 30,'7': 31,'8': 31,'9': 30, '10': 31, '11': 30, '12': 31}
key = input('Enter A Month Number:')
print(dictionary.get(key))