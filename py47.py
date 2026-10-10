#Program to count vowels in the inputted string and store their count in dictionary

def count_vowels(input_string):
    vowels='aeiouAEIOU'
    vowel_count={vowels:0 for vowels in vowels}

    for char in input_string:
        if char in vowel_count:
            vowel_count[char]=+1
    return vowel_count

user_input=input("Enter a string: ")
vowel_count=count_vowels(user_input)
print("Vowel counts:")
for vowel, count in vowel_count.items():
    print(f"{vowel}:{count}")
    
'''s=input("enter string).lower()
vow={'a:0, 'e':0, 'i':0, 'o':0, 'u':0}
for i in s:
if i in 'aeiou':
vow[i]+=1
print{vow}'''