#Chritopher Seow
#9/12/2018
#"Fallout Hacking Game" challange by reddit.com/r/dailyprogrammer

#Description: The popular video games Fallout 3 and Fallout: New Vegas have a 
#computer "hacking" minigame where the player must correctly guess the correct 
#password from a list of same-length words. Your challenge is to implement this 
#game yourself.

#The game operates similarly to the classic board game Mastermind. The player 
#has only 4 guesses and on each incorrect guess the computer will indicate how 
#many letter positions are correct.

#For example, if the password is MIND and the player guesses MEND, the game will 
#indicate that 3 out of 4 positions are correct (M_ND). If the password is COMPUTE 
#and the player guesses PLAYFUL, the game will report 0/7. While some of the letters 
#match, they're in the wrong position.

#Ask the player for a difficulty (very easy, easy, average, hard, very hard), then present 
#the player with 5 to 15 words of the same length. The length can be 4 to 15 letters. 
#More words and letters make for a harder puzzle. The player then has 4 guesses, and on each 
#incorrect guess indicate the number of correct positions.

#imports
import random
import sys

#custom function to compare strings characters by character
def comapre_char(str1, str2):
	num = 0
	for x in range(0,len(str1)):
		if str1[x] == str2[x]:
			num += 1
		else:
			pass
	return num
	
#variables
word_count = 0
ans_list = []
guess_count = 4
end = 0	
	
#read file and get the entire list of words
with open('enable1.txt','r') as f:
	word_list = f.read()
f.close()
#split the words into a list
words = word_list.split()
words_len = len(words)

#get user input for difficulty
#1 = 3 length and number of words, 2 = 6, 3 = 9, 4 = 12, 5 = 15 
diff = input('Select difficulty: 1-5 ')
#check for valid user input
if diff != "1" and diff != "2" and diff != "3" and diff != "4" and diff != "5":
	print('Invalid difficulty')
	sys.exit()
diff_i = int(diff)
x = diff_i * 3

#from user input, get the potential answers
#find list of words; number of and length based on difficulty (x)
while word_count != x:
	word_chck = random.randint(0,words_len)
	if len(words[word_chck]) == x:
		ans_list.append(words[word_chck])
		word_count += 1
#randomly pick one to be the correct answer
ans = ans_list[random.randint(0,x)]

#display the list of potential answers
for y in range(0,x):
	print(ans_list[y])

#Continue checking guesses until either answer is found or guesses are used up	
while end == 0:
	guess = input('Guess (' + str(guess_count) + '/4 left)?: ')
	#from user input, determine if user picked correct 
	#if correct, end game as user won
	if guess == ans:
		end = 1
		print(x,"/",x,"Correct! You Win!")
	#if incorrect, calculate how many correct letters
	else:
		#if more than 1 guess left, use up a guess, display correct letters and continue
		if guess_count > 1:
			guess_count -= 1
			num = comapre_char(guess, ans)
			print(num, '/', x, ' correct')
		#if that was last guess, display correct letters, end game
		else:
			num = comapre_char(guess, ans)
			print(num, '/', x, ' correct')
			print('You lose!')
			end = 1