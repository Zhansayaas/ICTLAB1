import random
#1
# thisdict = {
#     "A1":1,
#     "A2":2,
#     "A3":3,
#     "A4":4
# }
# a={"A1":5}
# thisdict.update(a)
# def reverse_Lookup(thisdict,x):
#     arr={}
#     for i,j in thisdict.items():
#         if j==x:
#             arr[i]=j
#     for i,j in arr.items():
#         print(j,i)
# reverse_Lookup(thisdict,4)
# reverse_Lookup(thisdict,5)
#2

# def two_dice_roll():
#     dice1 = random.randrange(6) + 1
#     dice2 = random.randrange(6) + 1
#     return dice1 + dice2
# result_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
# for turn in range(1000):
#     result = two_dice_roll()
#     result_dict[result] += 1
# print("Total".rjust(16), "|", "Simulated".rjust(16), "|", "Expected".rjust(16))
# for n in range(2, 13):
#     sim_result = str("%.2f" % (result_dict[n] / 1000 * 100))
#     if n <= 7:
#         exp_result = str("%.2f" % ((n - 1) / 36 * 100))
#     else:
#         exp_result = str("%.2f" % ((12 - n + 1) / 36 * 100))
#     print(str(n).rjust(16), "|", sim_result.rjust(16), "|", exp_result.rjust(16))

#3
# dictLetters={
#     1:{1:'.',2:',',3:'?',4:'!',5:':'},
#     2:{1:'a',2:'b',3:'c'},
#     3:{1:'d',2:'e',3:'f'},
#     4:{1:'g',2:'h',3:'i'},
#     5:{1:'j',2:'k',3:'l'},
#     6:{1:'m',2:'n',3:'o'},
#     7:{1:'q',2:'r',3:'s'},
#     8:{1:'t',2:'u',3:'v'},
#     9:{1:'w',2:'x',3:'y',4:'z'},
#     0:{1:" "}
# }
# n=input()
# n=n.lower()
# d=0
# num=0
# for t in n:
#     for i,j in dictLetters.items():
#         d+=1
#         for l in range(1,len(dictLetters[d%10])+1):
#             if(j[l]==t):
#                 num=l
#                 break
#         while num>0:
#             print(i,end="")
#             num=num-1

#4
# n = input() 
# MorseCodeDict = {
#     'a': '.-', 'j' : '.---', 's': '...',  '1' : '.---',
#     'b': '-...' ,'k': '-.-', 't' : '-', '2': '..--', 'c': '-.-.',
#     'l': '.-..', 'u': '..-', '3': '...-', 'd': '-..', 'm' :'--',
#     'v': '...-' ,'4': '....', 'e': '.', 'n': '-.', 'w': '.--',
#     '5': '.....', 'f': '..-.', 'o':'---', 'x': '-..-', '6' : '-....',
#     'g': '--.', 'p': '.--.', 'y': '-.--', '7': '--...', 'h': '....', 'q': '--.-',
#     'z': '--..', '8': '---..', 'i': '..', 'r':'.-.', '0': '-----', '9': '----.'
# }
# for t in n:
#     t=t.lower()
#     if(t in MorseCodeDict):
#         print(MorseCodeDict[t.lower()],end=' ') 

#5
# n=input()
# postalCodeDict = {
#     'A':'Newfoundland',
#     'B':'Nova Scotia',
#     'C':'Prince Edward Island',
#     'E':'New Brunswick',
#     'G':'Quebec',
#     'H':'Quebec',
#     'J':'Quebec',
#     'K':'Ontario',
#     'L':'Ontario',
#     'M':'Ontario',
#     'N':'Ontario',
#     'P':'Ontario',
#     'R':'Manitoba',
#     'S':'Saskatchwan',
#     'T':'Albertia',
#     'V':'British Columbia',
#     'X':'Nunavut'or'Northwest Territories',
#     'Y':'Yukon'
# }
# if(n[1] == '0'): print("Rural",end=' ')
# else: print("Urban",end=' ')
# print("address in ",end='')
# print(postalCodeDict[n[0]])   

#6
# n=input()
# num1={'0':'zero','1':'one', '2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
# num2={'10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen',
# '17':'seventeen','18':'eighteen','19':'nineteen','0':'','2':'twenty','3':'thirty','4':'forty','5':'fivety','6':'sixty','7':'seventy','8':'eighty',
# '9':'ninety'}
# if(len(n)==1):
#     print(num1[n])

# elif(len(n)==2):
#     if(n[0]=="1"):
#         print(num2[n])
#     else:
#         print(num2[n[0]],num1[n[0]])

# else:
#     print(num1[n[0]],"hundred",end=" ")
#     if(n[1]=="1"):
#         print(num2[n[1]+n[2]])
#     else:
#         print(num2[n[1]],num1[n[2]]) 

#7
# n=input()
# dict={}
# for i in n:
#     dict[i]=0
# for i in n:
#     dict[i]=dict+1
# print(len(dict)) 

#8
# dict={}
# dict1={}
# n=input()
# n1=input()
# cnt=0
# for i in n:
#     dict[i]=0
# for i in n1:
#     dict1[i]=0
# dict.update(dict1)
# for i,j in dict.items():
#         for l,r in dict1.items():
#             if i==l and j==r:
#                 cnt+=1
# if(cnt==len(n)):print("YES")
# else:print("NO")

#9
# n=input()
# n1=input()
# dict={}
# dict1={}

# for i in n:
#     i=i.lower()
#     if i>="a" and i<="z":
#         dict[i]=0
# for i in n1:
#     i=i.lower()
#     if i>="a" and i<="z":
#         dict1[i]=0
# cnt=0
# for i in n:
#     i=i.lower()
#     if i>="a" and i<="z":
#         dict[i]+=1
# for i in n1:
#     i=i.lower()
#     if i>="a" and i<="z":
#         dict1[i]+=1
# if(len(dict)!=len(dict1)):
#     print("NO")
# else:
#     for i,j in dict.items():
#         for l,r in dict1.items():
#             if i==l and j==r:
#                 cnt+=1
# if(cnt==len(dict)):
#     print("YES")
# else:
#     print("NO")

#10
n = input() 
cnt = 0
sc = {1:['A','E','I','L','N','O','R','S','T','U'],
       2:['D','G'],
       3:['B','C','M','P'],
       4:['F','H','V','W','Y'],
       5:['K'],
       8:['J','X'],
       10:['Q','Z']}
for i in n:
    for j,k in sc.items():
        for l in k:
            if l == i:
                cnt += j
print(cnt)