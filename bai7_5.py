def file_append_and_read(fname):
    with open(fname, "a") as myfile:
        myfile.write("21 vothisau\n")
        myfile.write("15082005\n")
    with open(fname, "r") as txt:
        print(txt.read())
file_append_and_read('hieu.txt')
print("sinh vien: Le Van Binh")
print("Mssv: 235752020710002")