diems = []

for i in range(3):
  diem = float(input(f"Nhập điểm môn {i+1}:"))
  diems.append(diem)

average = sum(diems) / len(diems)

print("Điểm trung bình =",average)