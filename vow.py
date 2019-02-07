b=input('')
a=b.isalpha()
if(len(b)==1):
	if a==True:
		if b in('a','e','i','o','u','A','E','I','O','U'):
			print("Vowel")
		else:
			print("Consonant")
	else:
		print("invalid")
else:
	print("invalid")
