n = input("Enter a num: ")
d1 = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
d2 = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'ninteen',20:'twenty'}
d3= {2:'twenty', 30:'thirty', 3:'thirty', 40:'forty', 4:'fourty', 50:'fifty', 5:'fifty', 60:'sixty', 6:'sixty', 70:'seventy', 7:'seventy', 80:'eighty', 8:'eighty', 90:'ninty', 9:'ninty'}
l = []
if int(n)>=0 and int(n)<10:
    x = int(n)
    print("Enter num in words :",d1[x])

elif int(n)>=10 and int(n)<=20:
    x = int(n)
    print("Enter num in words :",d2[x])

elif int(n)>=20 and int(n)<100:
    for i in n:
        x = int(i)
        l.append(x)
    if l[1]!=0:
        print("Enter num in words :", d3[l[0]],d1[l[1]])
    
    else:
        x = int(n)
        print("Enter num in words :", d3[x])
           