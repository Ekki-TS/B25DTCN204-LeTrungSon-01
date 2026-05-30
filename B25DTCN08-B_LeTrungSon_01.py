students = [
    {
        "id": "SV001",
        "ten": "Nguyen Van A",
        "diem_toan": 8.5,
        "diem_ly": 7.0,
        "diem_hoa": 9.0,
        "diem_tb": 8.17,
        "xep_loai": "Giỏi"
    }
]

while True:
    print("\n================= MENU =================")
    print("1. Hiển thị danh sách sinh viên")
    print("2. Thêm mới sinh viên")
    print("3. Cập nhật thông tin sinh viên")
    print("4. Xóa sinh viên")
    print("5. Tìm kiếm sinh viên")
    print("6. Sắp xếp danh sách sinh viên")
    print("7. Thống kê học lực")
    print("8. Liệt kê sinh viên có điểm TB cao nhất / thấp nhất")
    print("9. Phân loại học lực sinh viên")
    print("10. Thoát")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    if choice == "1":
        if not students:
            print("Danh sách sinh viên trống.")
        else:
            print(f"\n{'Mã SV':<10}{'Tên':<25}{'Điểm TB':<10}{'Xếp loại':<10}")

            for student in students:
                print(f"{student['id']:<10}{student['ten']:<25}{student['diem_tb']:<10}{student['xep_loai']:<10}")

    elif choice == "2":
        student_id = input("Nhập mã sinh viên: ").strip()

        is_duplicate = False
        for s in students:
            if s["id"] == student_id:
                is_duplicate = True
                break

        if is_duplicate:
            print("Mã sinh viên đã tồn tại!")
            continue

        name = input("Nhập tên sinh viên: ").strip()

        while True:
            diem_toan = input("Nhập điểm Toán: ").strip()
            if diem_toan.replace(".", "", 1).isdigit():
                diem_toan = float(diem_toan)
                if 0 <= diem_toan <= 10:
                    break
            print("Điểm phải từ 0 đến 10!")

        while True:
            diem_ly = input("Nhập điểm Lý: ").strip()
            if diem_ly.replace(".", "", 1).isdigit():
                diem_ly = float(diem_ly)
                if 0 <= diem_ly <= 10:
                    break
            print("Điểm phải từ 0 đến 10!")

        while True:
            diem_hoa = input("Nhập điểm Hóa: ").strip()
            if diem_hoa.replace(".", "", 1).isdigit():
                diem_hoa = float(diem_hoa)
                if 0 <= diem_hoa <= 10:
                    break
            print("Điểm phải từ 0 đến 10!")

        diem_tb = round((diem_toan + diem_ly + diem_hoa) / 3, 2)

        if diem_tb >= 8:
            xep_loai = "Giỏi"
        elif diem_tb >= 7:
            xep_loai = "Khá"
        elif diem_tb >= 5:
            xep_loai = "TB"
        else:
            xep_loai = "Yếu"

        students.append({
            "id": student_id,
            "ten": name,
            "diem_toan": diem_toan,
            "diem_ly": diem_ly,
            "diem_hoa": diem_hoa,
            "diem_tb": diem_tb,
            "xep_loai": xep_loai
        })

        print("Thêm sinh viên thành công!")

    elif choice == "3":
        student_id = input("Nhập mã sinh viên cần cập nhật: ").strip()

        student = None
        for s in students:
            if s["id"] == student_id:
                student = s
                break

        if student is None:
            print("Không tìm thấy sinh viên.")
            continue

        new_name = input("Nhập tên mới: ").strip()
        if new_name:
            student["ten"] = new_name

        while True:
            diem_toan = input("Nhập điểm Toán mới: ").strip()
            if diem_toan.replace(".", "", 1).isdigit():
                diem_toan = float(diem_toan)
                if 0 <= diem_toan <= 10:
                    break
            print("Điểm phải từ 0 đến 10!")

        while True:
            diem_ly = input("Nhập điểm Lý mới: ").strip()
            if diem_ly.replace(".", "", 1).isdigit():
                diem_ly = float(diem_ly)
                if 0 <= diem_ly <= 10:
                    break
            print("Điểm phải từ 0 đến 10!")

        while True:
            diem_hoa = input("Nhập điểm Hóa mới: ").strip()
            if diem_hoa.replace(".", "", 1).isdigit():
                diem_hoa = float(diem_hoa)
                if 0 <= diem_hoa <= 10:
                    break
            print("Điểm phải từ 0 đến 10!")

        student["diem_toan"] = diem_toan
        student["diem_ly"] = diem_ly
        student["diem_hoa"] = diem_hoa

        diem_tb = round((diem_toan + diem_ly + diem_hoa) / 3, 2)
        student["diem_tb"] = diem_tb

        if diem_tb >= 8:
            student["xep_loai"] = "Giỏi"
        elif diem_tb >= 7:
            student["xep_loai"] = "Khá"
        elif diem_tb >= 5:
            student["xep_loai"] = "TB"
        else:
            student["xep_loai"] = "Yếu"

        print("Cập nhật thành công!")

    elif choice == "4":
        student_id = input("Nhập mã sinh viên cần xóa: ").strip()

        student = None
        for s in students:
            if s["id"] == student_id:
                student = s
                break

        if student is None:
            print("Không tìm thấy sinh viên.")
            continue

        confirm = input("Bạn có chắc muốn xóa? (Y/N): ").upper()

        if confirm == "Y":
            students.remove(student)
            print("Đã xóa sinh viên.")
        else:
            print("Đã hủy xóa.")

    elif choice == "5":
        keyword = input("Nhập tên hoặc mã sinh viên cần tìm: ").lower().strip()

        found = False

        for s in students:
            if keyword in s["id"].lower() or keyword in s["ten"].lower():
                found = True
                print("----------------------------")
                print("Mã SV:", s["id"])
                print("Tên:", s["ten"])
                print("Điểm TB:", s["diem_tb"])
                print("Xếp loại:", s["xep_loai"])

        if not found:
            print("Không tìm thấy sinh viên.")

    elif choice == "6":
        print("\n1. Sắp xếp theo điểm TB giảm dần")
        print("2. Sắp xếp theo tên A-Z")

        sort_choice = input("Chọn kiểu sắp xếp: ").strip()

        if sort_choice == "1":
            students.sort(
                key=lambda student: student["diem_tb"],
                reverse=True
            )
            print("Đã sắp xếp theo điểm TB giảm dần.")

        elif sort_choice == "2":
            students.sort(
                key=lambda student: student["ten"]
            )
            print("Đã sắp xếp theo tên A-Z.")

        else:
            print("Lựa chọn không hợp lệ.")

    elif choice == "7":
        gioi = 0
        kha = 0
        tb = 0
        yeu = 0

        for student in students:
            if student["xep_loai"] == "Giỏi":
                gioi += 1
            elif student["xep_loai"] == "Khá":
                kha += 1
            elif student["xep_loai"] == "TB":
                tb += 1
            else:
                yeu += 1

        print("\nTHỐNG KÊ HỌC LỰC")
        print("Giỏi:", gioi)
        print("Khá:", kha)
        print("TB:", tb)
        print("Yếu:", yeu)

    elif choice == "8":
        if not students:
            print("Danh sách sinh viên trống.")
            continue

        max_tb = max(students, key=lambda student: student["diem_tb"])["diem_tb"]
        min_tb = min(students, key=lambda student: student["diem_tb"])["diem_tb"]

        print("\nSinh viên có điểm TB cao nhất:")
        for student in students:
            if student["diem_tb"] == max_tb:
                print(
                    f"{student['id']} | "
                    f"{student['ten']} | "
                    f"{student['diem_tb']}"
                )

        print("\nSinh viên có điểm TB thấp nhất:")
        for student in students:
            if student["diem_tb"] == min_tb:
                print(
                    f"{student['id']} | "
                    f"{student['ten']} | "
                    f"{student['diem_tb']}"
                )

    elif choice == "9":
        print("\nPHÂN LOẠI HỌC LỰC")

        for student in students:
            print(
                f"{student['id']} | "
                f"{student['ten']} | "
                f"{student['diem_tb']} | "
                f"{student['xep_loai']}"
            )

    elif choice == "10":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ.")