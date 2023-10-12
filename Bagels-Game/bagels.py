from random import choice

secret_num = ""
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
i = 0
random_digit_arr = []
max_trial = 10
initial_trial = 1
number_digit = 3

print('''Bagels, a deductive logic game.
I am thinking of a {}-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the clue would be fermi pico '''.format(number_digit))

while i < number_digit : 
    random_digit = choice(number_list)
    if random_digit not in secret_num:
        secret_num = ''.join((secret_num,random_digit))
    else:
        continue
    i += 1
for new_gen_num in secret_num:
        random_digit_arr.append(new_gen_num)
arr1 = random_digit_arr


while initial_trial < max_trial:

    #Player enters a three digit number
    input_num = input("Please enter a three digit number")
    if len(input_num) < 3:
        print("The number entered is less than three !!!")
    else:
        input_arr = []
        for input_iterator in input_num:
            input_arr.append(input_iterator)
        arr2 = input_arr
        clues = []
        for j in range(len(arr2)):
            if (arr1.index(str(arr1[j])) == arr2.index(str(arr2[j])) and arr1[j] == arr2[j]):
                clues.append('fermi')
            elif arr2[j] in arr1:
                clues.append('pico')
        if len(clues) == 0:
            print("Bagels")
        else:
            clues.sort()
        sorted_clue = ' '.join(clues)
        print(sorted_clue)
    initial_trial += 1
    if arr1 == arr2:
        print ('You have guessed right')
        break


