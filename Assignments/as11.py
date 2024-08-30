

def vowels_ct(str):
    count = 0
    vowel = set(
        "aeiouAEIOU"
    )
    for x in str:
        if x in vowel:
            count = count + 1

    print("Number of vowels: ",count)

str = "Soham"
vowels_ct(str)
