name = "ada lovelace"
print(name.upper())
print(name.title())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")
message = f"Hello, {full_name.title()}"
print(message)

# \n & \t
print("\nLenguages:\n\t\tPython\n\t\tC++\n\t\tJava")

message = " python "
print(message.lstrip().rstrip())
print(message.strip())
print(message)

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

message = "\nOne of Python's strenghts is its dicerse community.\n"
print(message)