#Write a python program that removes all punctuation from a given string.
punctuations='''{}[]-();:"\,./<>?#@%$*^&!~_'''
str="hello welcome to python"
nopunc=""
for i in str:
    if i not in punctuations:
        nopunc=nopunc+i
print(nopunc)        



