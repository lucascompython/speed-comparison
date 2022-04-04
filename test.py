from subprocess import check_call
from tempfile import NamedTemporaryFile


cmd = "g++ main.cpp -o main; ./main" 
with NamedTemporaryFile() as f:
    check_call(cmd, shell=True, stdout=f, stderr=f, cwd="./src")
    f.seek(0)
    output = f.read().decode("utf8")


print(output)