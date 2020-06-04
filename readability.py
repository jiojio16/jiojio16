import cs50
from cs50 import get_string
#input from user for text.
text = get_string("Enter Text:");
#declare words, letters,sentences
words = 1
letters = 0
sentences = 0
#formula set to count characters in letters,words and sentences.
for i in text:
    if (i.isalpha()):
        letters += 1
    if (i == '.' or i == '!' or i == '?'):
        sentences += 1
    if ( i == ' '):
        words += 1
# formula average for letters and sentences
letters = 100 * float (letters) / float (words)
sentences = 100 * float (sentences) / float (words)
#"Coleman-Liau index"-formual
index = (0.0588 * letters) - (0.296 * sentences) -15.8
#declare grade to equal and round index.
grade = round (index)
#seperating index results for grade 1 and grade 16+
if (index < 1):
    print ("Before Grade 1")
elif(index >= 16):
        print ("Grade 16+")
else:
#output of final results.
            print ("Grade " + str(grade))