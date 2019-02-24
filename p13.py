def sq(num):
    m = list(str(num)) 
    for word in m:  
        print(int(word)**2, end="")

num =int(input())
sq(num)
