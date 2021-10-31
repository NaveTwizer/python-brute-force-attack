import hashlib
from types import TracebackType

def convert_text_to_md5(text:str):
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()

inp = input("Enter the text: ")
import time as t
found = False
start_time = t.time()
hash_passowrd = convert_text_to_md5(inp)
with open("passwords.txt", "r") as passwords_file:
    all_lines = passwords_file.read().splitlines()
    for line in all_lines:
        if (convert_text_to_md5(str(line)) == hash_passowrd):
            print("PASSWORD FOUND")
            print(line)
            found = True
            break

print("PASSWORD MD5: ", hash_passowrd)
if not found:
    print("The password does not appear in the txt file.")
    with open("passwords.txt", "a") as f: #Append text and NOT REWRITE. w REWRITES.
        f.write(f"\n{inp}")
print("--- %s seconds ---" % (t.time() - start_time))  
