import turtle, random
path='/Users/techwizard/Desktop/wordlist.txt'
stage=[0]

def wordlist():
        #Opens the wordlist file, reads them, and
        #selects one word from random
	file= open(path, 'r')
	lst=file.readlines()
	file.close()
	rNum = random.randint(0,len(lst));
	return lst[rNum]
	
def go_to(x, y, p):
        #Setup Turtle Drawing Coordinates
	turtle.hideturtle()
	turtle.penup()
	turtle.goto(x,y)
	turtle.setheading(p)
	turtle.pendown()
	
def hang():
        #Draws each piece of the hangman based on
        #number of guesses entered
	turtle.speed(0)
	if stage[0]==0:
		go_to(-300,0,0)
		turtle.forward(600)
		go_to(-100,0, 90)
		turtle.forward(200)
		turtle.right(90)
		turtle.forward(100)
		turtle.right(90)
		turtle.forward(25)
	elif stage[0]==1:
		go_to(0, 150, 0)
		turtle.circle(12.5)
	elif stage[0]==2:
		go_to(0,150, -90)
		turtle.forward(50)
	elif stage[0]==3:
		go_to(0,140, -45)
		turtle.forward(25)
		go_to(0,140, -135)
		turtle.forward(25)
	elif stage[0]==4:
		go_to(0,100, -45)
		turtle.forward(25)
		go_to(0,100, -135)
		turtle.forward(25)
	stage[0]+=1
	return 0

def spaces(word):
        #Draws the number of spaces based upon random
        #selected word
	l=len(word)
	if l %2 !=0:
		go_to(-5-(l//2*20) - (l//2*10), -150, 0)
		for i in range(l):
			turtle.forward(20)
			turtle.penup()
			turtle.forward(10)
			turtle.pendown()
	else:
		go_to(-(l//2*20) - (l//2*10), -150, 0)
		for i in range(l):
			turtle.forward(20)
			turtle.penup()
			turtle.forward(10)
			turtle.pendown()

def error(word, char):
        #When player guesses incorrectly, call hang
        #to draw a piece of hangman
	go_to(-5-(len(word)//2*20) - (len(word)//2*10), -200, 0)
	turtle.penup()
	for j in range(stage[0]):
		turtle.forward(20)
	turtle.pendown()
	turtle.write(char, align='center', font=("Arial", 8, "normal"))
	hang()
	
	
	
def point(word, char, i):
        #When player guessses correctly, write the character
        #on the line
	go_to(-5-(len(word)//2*20) - (len(word)//2*10), -150, 0)
	turtle.penup()
	for j in range(i):
		turtle.forward(20)
		turtle.forward(10)
	turtle.forward(10)
	turtle.pendown()
	turtle.write(char, align='center', font=("Arial", 24, "normal"))

def play(word, out):
        #Text UI on screen for player to enter characters
	ch=input('Guess a letter: ')
	key=''
	if ch in word:
		for i in range(len(word)):
			if ch==word[i]:
				key+=ch
				point(word, ch, i)
			else:
				key+=out[i]
		return key
	else:
		error(word, ch)
		return out

def main():
        word=wordlist().strip('\n').lower()
        #print(word) #Remove the comment to display answer prior
        spaces(word)
        out=''
        for i in range(len(word)):
                out+='_'
        while out != word and stage[0]<=4:
                print(out)
                out=play(word, out)
        if stage[0] > 4:
                print("YOU'RE DEAD, KID!")
                print((word) + " was the word.")
                turtle.bgcolor('red')
                turtle.up()
                turtle.goto(100,-50)
                turtle.down()
                turtle.write("YOU'RE DEAD KID", font= ("Arial", 16))
                turtle.exitonclick()
        else:
                print('CONGRATS!!!! The word was ' + word + '!')
                turtle.up()
                turtle.goto(-50, -50)
                turtle.down()
                turtle.write("CONGRATULATIONS, YOU'VE WON!", font=("Arial", 16, "bold"))
                turtle.bgcolor('green')
                turtle.exitonclick()

if __name__ == '__main__':
	main()
