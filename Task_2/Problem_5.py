
text = open("texter.txt", "r")
text_file = text.readlines()

words = text_file.split()
word_count = {}  

for word in words:
    if word in word_count:
        word_count[word] += 1  
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word}: {count}")


# My code seems reasonable but it keeps saying file/directory does not exist 
# I tried many things and none worked was able to read the file even on pyspark library
# Pleas rate my code as it is, if the code fails because of what is written and not some extensions/missing python files
# then kindly share the answer 
