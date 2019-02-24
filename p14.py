l=int(input())
string = input()
if string == 'x':
    exit();
else:
    d = string;
    vowels = ('a', 'e', 'i', 'o', 'u');
    for x in string.lower():
        if x in vowels:
            d = d.replace(x,"");
    print(d[::-1]);
