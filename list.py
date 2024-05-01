# numbers=[1,2,3,4,5]
# squares=[]

# for number in numbers:
#     squares.append(number ** 2)
# print(squares)

# square = [number ** 2 for number in numbers]
# print(square)

# even=[]
# for i in range(1,51):
#     if i%2==0:
#         even.append(i)
# print(even)

# evens=[i for i in range(1,51) if i%2==0]
# print(evens)

# numbers=[1,2,3,4,5]

# [-1.-2-3,-4,-5]

# negative_num=[]

# for number in numbers:
#     negative_num.append(number * -1)
# print(negative_num)

# nega_num=[number * -1 for number in numbers]
# print(nega_num)

# names=['laura','steve','bill','james','bob','greig','scott','alex','ive']
# vowels=[]
# for name in names:
#     if name[0] in 'aeiou':
#         vowels.append(name)
# print(vowels)

# vowel=[name for name in names if name[0] in 'aeiou']
# print(vowel)/

# langs=['python','php','perl','js','c++','ruby','html','css','html']
# p_langs=[]
# for lang in langs:
#     if lang[0]=='p':
#         p_langs.append(lang)

# print(p_langs)

# p_lang=[lang for lang in langs if lang[0]=='p']
# print(p_lang)

# p_language= [lang for lang in langs if lang.startswith('p')]
# print(p_language)

# names=['apple','google','yahoo','gmail','flipkart','microsoft']
# s_names=[]
# for name in names:
#     if len(name)<6:
#         s_names.append(name)
# print(s_names)

# sh_name=[name for name in names if len(name)<6]
# print(sh_name)

names=['laura','steve','bill','james','bob','greig','scott','alex','ive']
vowels=[]
for name in names:
    if name[0] not in 'aeiou':
        vowels.append(name)
print(vowels)

vowel=[name for name in names if name[0] not in 'aeiou']
print(vowel)

full_name=