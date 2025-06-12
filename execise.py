str = "mississippi"

list_str  = [*str]
print(list_str)

word_dic = {}
word_set = set()


for strs in list_str:
    if strs in word_dic:
        word_dic[strs] = word_dic[strs] + 1
    else:
        word_dic[strs] = 1

lst2 =sorted(word_dic.items(),key = lambda item:item[1])
x , *y = lst2[len(lst2) -1]
print( x )



#for letter in list_str:
    #if letter not in word_set:
## word_set.add(letter)
####   word_dic[letter] =1
##else:
      ##current_value = word_dic[letter]
      ##word_dic[letter] = current_value + 1

##higest_occurance = max(word_dic,key=word_dic.get)
##print(higest_occurance)


sentence = "apple banana apple orange banana apple"
new_sentence = sentence.split(" ")
new_dic = {}
for fruit in new_sentence:
    if fruit in new_dic:
        new_dic[fruit] +=1
    else:
        new_dic[fruit] = 1


print(new_dic)


numbers = [5, 3, 1, 5, 2, 3, 1]
real_num = set()

for num in numbers:
    real_num.add(num)
result = list(real_num)
print(result)



points = [(3, 2), (7, 4), (1, 9)]
# Output: [(2, 3), (4, 7), (9, 1)]
new_point = []

for i,p in points:
    new_point.append((p,i))

print(new_point)

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

seta = set(a)
setb = set(b)

print(seta & setb)

sentences = ("hello world", "world of python", "hello python")

new_list = []
new_sentence = [*sentences]
print(new_sentence)
strs = ""
new_set = set ()
len_of_setence = len(new_sentence) - 1
for i,y in enumerate(new_sentence):
    if len_of_setence > i:
         strs += y + " "
    else:
        strs +=y

for wrd in [strs.split()]:
    new_set.add(wrd)


print(new_set)
