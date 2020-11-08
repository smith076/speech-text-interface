import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
val=input("Enter a name")
speak.Speak("Hello "+val+ ". I am David. I am your humble assistant.")
speak.Speak("Enter 2 numbers")
a=input(". . .")
b=input(". . .")
sum=a+b
speak.Speak("The Sum is "+sum+"")