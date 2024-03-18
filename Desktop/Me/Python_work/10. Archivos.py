from pathlib import Path

path = Path('pi_digits.txt') 
contents = path.read_text().rstrip()
print(contents)

lines = contents.splitlines() 
for line in lines: 
    print(line)


pi_string = '' 
for line in lines: 
    pi_string += line.lstrip()
    print(pi_string)
print(len(pi_string))


#for line in lines: 
#    pi_string += line.strip() 
#    birthday = input("Enter your birthday, in the form mmddyy: ") 
#    if birthday in pi_string: 
#        print("Your birthday appears in the first million digits of pi!")
#    else: print("Your birthday does not appear in the first million digits of pi.")

path.write_text("I love programming.")

