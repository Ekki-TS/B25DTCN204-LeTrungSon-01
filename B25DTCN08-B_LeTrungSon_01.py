import json
import os

DATA_FILE = "data.json"

def tinh_diem_tb(toan: float, ly: float, hoa: float) -> float:
    return round((toan + ly + hoa) / 3, 2)


def xep_loai_hoc_luc(diem_tb: float) -> str:
    if diem_tb >= 8.0:
        return "Giỏi"
    elif diem_tb >= 7.0:
        return "Khá"
    elif diem_tb >= 5.0:
        return "Trung Bình"
    else:
        return "Yếu"


def doc_du_lieu() -> list:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def luu_du_lieu(ds: list) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=4)


def in_bang(ds: list) -> None:
    if not ds:
        print("  [Danh sách trống]")
        return
    header = (f"{'Mã SV':<8} {'Tên':<22} {'Toán':>6} {'Lý':>6} "
              f"{'Hóa':>6} {'Điểm TB':>8} {'Xếp loại':<12}")
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for sv in ds:
        print(
            f"{sv['ma_sv']:<8} {sv['ten']:<22} {sv['diem_toan']:>6.1f} "
            f"{sv['diem_ly']:>6.1f} {sv['diem_hoa']:>6.1f} "
            f"{sv['diem_tb']:>8.2f} {sv['xep_loai']:<12}"
        )
    print("-" * len(header))


def nhap_diem(nhan: str) -> float:
    while True:
        try:
            val = float(input(nhan))
            if 0 <= val <= 10:
                return round(val, 1)
            print("  Điểm phải trong khoảng 0 – 10. Vui lòng nhập lại.")
        except ValueError:
            print("  Vui lòng nhập số hợp lệ.")

def hien_thi_danh_sach(ds: list) -> None:
    print("\n===== DANH SÁCH SINH VIÊN =====")
    in_bang(ds)

def them_sinh_vien(ds: list) -> None:
    print("\n===== THÊM MỚI SINH VIÊN =====")
    ma_sv = input("Nhập mã sinh viên: ").strip().upper()
    if not ma_sv:
        print("  Mã sinh viên không được để trống.")
        return
    if any(sv["ma_sv"] == ma_sv for sv in ds):
        print(f"  Mã '{ma_sv}' đã tồn tại. Vui lòng nhập mã khác.")
        return

    ten = input("Nhập tên sinh viên: ").strip()
    if not ten:
        print("  Tên sinh viên không được để trống.")
        return

    diem_toan = nhap_diem("Điểm Toán (0-10): ")
    diem_ly   = nhap_diem("Điểm Lý   (0-10): ")
    diem_hoa  = nhap_diem("Điểm Hóa  (0-10): ")

    diem_tb  = tinh_diem_tb(diem_toan, diem_ly, diem_hoa)
    xep_loai = xep_loai_hoc_luc(diem_tb)

    sv = {
        "ma_sv": ma_sv,
        "ten": ten,
        "diem_toan": diem_toan,
        "diem_ly": diem_ly,
        "diem_hoa": diem_hoa,
        "diem_tb": diem_tb,
        "xep_loai": xep_loai,
    }
    ds.append(sv)
    luu_du_lieu(ds)
    print(f"\n  Đã thêm sinh viên '{ten}' | ĐTB: {diem_tb} | Xếp loại: {xep_loai}")

def cap_nhat_sinh_vien(ds: list) -> None:
    print("\n===== CẬP NHẬT SINH VIÊN =====")
    ma_sv = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    for sv in ds:
        if sv["ma_sv"] == ma_sv:
            print(f"  Tìm thấy: {sv['ten']} | Toán: {sv['diem_toan']} | Lý: {sv['diem_ly']} | Hóa: {sv['diem_hoa']}")
            diem_toan = nhap_diem("Điểm Toán mới (0-10): ")
            diem_ly   = nhap_diem("Điểm Lý   mới (0-10): ")
            diem_hoa  = nhap_diem("Điểm Hóa  mới (0-10): ")
            sv["diem_toan"] = diem_toan
            sv["diem_ly"]   = diem_ly
            sv["diem_hoa"]  = diem_hoa
            sv["diem_tb"]   = tinh_diem_tb(diem_toan, diem_ly, diem_hoa)
            sv["xep_loai"]  = xep_loai_hoc_luc(sv["diem_tb"])
            luu_du_lieu(ds)
            print(f"  Cập nhật thành công! ĐTB mới: {sv['diem_tb']} | Xếp loại: {sv['xep_loai']}")
            return
    print(f"  Không tìm thấy sinh viên với mã '{ma_sv}'.")

def xoa_sinh_vien(ds: list) -> None:
    print("\n===== XÓA SINH VIÊN =====")
    ma_sv = input("Nhập mã sinh viên cần xóa: ").strip().upper()
    for i, sv in enumerate(ds):
        if sv["ma_sv"] == ma_sv:
            xac_nhan = input(f"  Bạn có chắc muốn xóa '{sv['ten']}' (y/n)? ").strip().lower()
            if xac_nhan == "y":
                ds.pop(i)
                luu_du_lieu(ds)
                print("  Đã xóa thành công.")
            else:
                print("  Hủy thao tác xóa.")
            return
    print(f"  Không tìm thấy sinh viên với mã '{ma_sv}'.")

def tim_kiem_sinh_vien(ds: list) -> None:
    print("\n===== TÌM KIẾM SINH VIÊN =====")
    print("1. Tìm theo tên (gần đúng)")
    print("2. Tìm theo mã sinh viên")
    lua_chon = input("Chọn (1/2): ").strip()

    if lua_chon == "1":
        tu_khoa = input("Nhập tên cần tìm: ").strip().lower()
        ket_qua = [sv for sv in ds if tu_khoa in sv["ten"].lower()]
    elif lua_chon == "2":
        ma_sv = input("Nhập mã sinh viên: ").strip().upper()
        ket_qua = [sv for sv in ds if sv["ma_sv"] == ma_sv]
    else:
        print("  Lựa chọn không hợp lệ.")
        return

    if ket_qua:
        print(f"\n  Tìm thấy {len(ket_qua)} kết quả:")
        in_bang(ket_qua)
    else:
        print("  Không tìm thấy kết quả phù hợp.")

def sap_xep_sinh_vien(ds: list) -> None:
    print("\n===== SẮP XẾP DANH SÁCH =====")
    print("1. Sắp xếp theo Điểm TB (giảm dần)")
    print("2. Sắp xếp theo Tên (A-Z tăng dần)")
    lua_chon = input("Chọn (1/2): ").strip()

    if lua_chon == "1":
        ds_sx = sorted(ds, key=lambda sv: sv["diem_tb"], reverse=True)
        print("\n  Danh sách sau khi sắp xếp theo Điểm TB (giảm dần):")
    elif lua_chon == "2":
        ds_sx = sorted(ds, key=lambda sv: sv["ten"].lower())
        print("\n  Danh sách sau khi sắp xếp theo Tên (A-Z):")
    else:
        print("  Lựa chọn không hợp lệ.")
        return

    in_bang(ds_sx)

def thong_ke_diem_tb(ds: list) -> None:
    print("\n===== THỐNG KÊ ĐIỂM TRUNG BÌNH =====")
    if not ds:
        print("  [Danh sách trống]")
        return

    cac_loai = ["Giỏi", "Khá", "Trung Bình", "Yếu"]
    tong = len(ds)
    for loai in cac_loai:
        so_luong = sum(1 for sv in ds if sv["xep_loai"] == loai)
        phan_tram = (so_luong / tong * 100) if tong > 0 else 0
        print(f"  {loai:<12}: {so_luong:>3} sinh viên ({phan_tram:.1f}%)")
    print(f"  {'Tổng':<12}: {tong:>3} sinh viên")

def cao_nhat_thap_nhat(ds: list) -> None:
    print("\n===== SINH VIÊN CÓ ĐIỂM TB CAO NHẤT / THẤP NHẤT =====")
    if not ds:
        print("  [Danh sách trống]")
        return

    diem_cao = max(sv["diem_tb"] for sv in ds)
    diem_thap = min(sv["diem_tb"] for sv in ds)

    ds_cao  = [sv for sv in ds if sv["diem_tb"] == diem_cao]
    ds_thap = [sv for sv in ds if sv["diem_tb"] == diem_thap]

    print(f"\n  Điểm TB cao nhất ({diem_cao}):")
    in_bang(ds_cao)

    print(f"\n  Điểm TB thấp nhất ({diem_thap}):")
    in_bang(ds_thap)

def phan_loai_hoc_luc(ds: list) -> None:
    print("\n===== PHÂN LOẠI HỌC LỰC SINH VIÊN =====")
    if not ds:
        print("  [Danh sách trống]")
        return

    cac_loai = [
        ("Giỏi",       "ĐTB >= 8.0"),
        ("Khá",        "7.0 <= ĐTB < 8.0"),
        ("Trung Bình", "5.0 <= ĐTB < 7.0"),
        ("Yếu",        "ĐTB < 5.0"),
    ]

    for ten_loai, mo_ta in cac_loai:
        nhom = [sv for sv in ds if sv["xep_loai"] == ten_loai]
        print(f"\n  {ten_loai} ({mo_ta}) – {len(nhom)} sinh viên:")
        if nhom:
            in_bang(nhom)
        else:
            print("    [Không có sinh viên]")

def hien_thi_menu() -> None:
    print("\n" + "=" * 48)
    print("      QUẢN LÝ SINH VIÊN – HACKATHON 01")
    print("=" * 48)
    print("  1. Hiển thị danh sách sinh viên")
    print("  2. Thêm mới sinh viên")
    print("  3. Cập nhật thông tin sinh viên")
    print("  4. Xóa sinh viên")
    print("  5. Tìm kiếm sinh viên")
    print("  6. Sắp xếp danh sách sinh viên")
    print("  7. Thống kê điểm trung bình")
    print("  8. Sinh viên điểm TB cao nhất / thấp nhất")
    print("  9. Phân loại học lực sinh viên")
    print("  0. Thoát")
    print("=" * 48)


def main() -> None:
    ds = doc_du_lieu()
    print("Đã nạp dữ liệu từ", DATA_FILE if os.path.exists(DATA_FILE) else "(mới tạo)")

    while True:
        hien_thi_menu()
        lua_chon = input("  Chọn chức năng: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach(ds)
        elif lua_chon == "2":
            them_sinh_vien(ds)
        elif lua_chon == "3":
            cap_nhat_sinh_vien(ds)
        elif lua_chon == "4":
            xoa_sinh_vien(ds)
        elif lua_chon == "5":
            tim_kiem_sinh_vien(ds)
        elif lua_chon == "6":
            sap_xep_sinh_vien(ds)
        elif lua_chon == "7":
            thong_ke_diem_tb(ds)
        elif lua_chon == "8":
            cao_nhat_thap_nhat(ds)
        elif lua_chon == "9":
            phan_loai_hoc_luc(ds)
        elif lua_chon == "0":
            print("\n  Cảm ơn! Hẹn gặp lại. \n")
            break
        else:
            print("  Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
