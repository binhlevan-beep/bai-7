def count_lines_in_file(fname):
    with open(fname, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        return num_lines
file_name = 'hieu.txt' 
line_count = count_lines_in_file(file_name)
print(f"Số dòng trong tệp '{file_name}' là: {line_count}")
print("sinh vien: Le Van Binh")
print("Mssv: 235752020710002")