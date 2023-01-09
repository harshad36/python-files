'''
When there is need to preserve old data or new data must be
added at the end of the old data use append mode.

'''
fp=open("data.txt","a")
#d="This is  first line in the file"
#fp.write(d)
mn=input("enter mobile number:")
data=mn+"\n"   #\n stands for new line character
fp.write(data)
fp.close()
