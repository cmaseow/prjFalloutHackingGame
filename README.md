# prjFalloutHackingGame
Written in Python 3.7.0; "Fallout Hacking Game" challenge by reddit.com/r/dailyprogrammer. https://www.reddit.com/r/dailyprogrammer/comments/3qjnil/20151028_challenge_238_intermediate_fallout/

Description: 

The popular video games Fallout 3 and Fallout: New Vegas have a 
computer "hacking" minigame where the player must correctly guess the correct 
#password from a list of same-length words. Your challenge is to implement this 
game yourself.

The game operates similarly to the classic board game Mastermind. The player 
has only 4 guesses and on each incorrect guess the computer will indicate how 
many letter positions are correct.

For example, if the password is MIND and the player guesses MEND, the game will 
indicate that 3 out of 4 positions are correct (M_ND). If the password is COMPUTE 
and the player guesses PLAYFUL, the game will report 0/7. While some of the letters 
match, they're in the wrong position.

Ask the player for a difficulty (very easy, easy, average, hard, very hard), then present 
the player with 5 to 15 words of the same length. The length can be 4 to 15 letters. 
More words and letters make for a harder puzzle. The player then has 4 guesses, and on each 
incorrect guess indicate the number of correct positions.
