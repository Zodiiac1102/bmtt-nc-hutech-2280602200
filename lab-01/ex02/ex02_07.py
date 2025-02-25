print("Nhập các dòng văn bản (Nhập 'done' khi kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    line.append(line)
print("\nCác dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())