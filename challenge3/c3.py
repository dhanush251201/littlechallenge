import sys
import time

thisiswhatyourelookingfor="""
        |----------------|
        |    	          |
        |   fake flags 	   |
        |                 |
        |----------------|
        |
        |
        |
        |
________|___________
"""
WtfIsThisBS=[33,36,48,85,114,36,48,110,71]
res = []
def thisDoesNotOpenAnyFiles():
    for i in WtfIsThisBS:
        res.append((chr(i)))
    return "".join(res)
    
if __name__ == '__main__':
    n = len(sys.argv)
    if n != 3:
        print("Insufficient arguments!!\nTry python <filename> [params] [argument]")
        exit(1)
    else:
        
        if sys.argv[1] =='-m':
            print("Seems like you are onto something...")
            time.sleep(2)
            print("But since it's Your birthday, this is gonna leak your opinions on ppl online")
            time.sleep(2)
            print("You will be wrecked if you dont terminate this process...")
            time.sleep(1)
            print("5")
            time.sleep(1)
            print("4")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(6)
            print("Jk here's the flag")
            time.sleep(1)
            a = thisDoesNotOpenAnyFiles()
            print(a)
        elif sys.argv[1] =='-h':
            print("welcome to the world of Computers!")
            time.sleep(2)
            print("You are so close to the flag")
            time.sleep(2)
            print("pls wait wile we search for your flag")
            time.sleep(2)
            print("Here's ypur flag:")
            print(thisiswhatyourelookingfor)
        else:
            print("Invalid arguments provided!!!!!!!")
            time.sleep(2)
            print("but here's a consolation")
            time.sleep(2)
            print(thisiswhatyourelookingfor)