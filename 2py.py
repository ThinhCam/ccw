# Khởi tạo số tiền ban đầu của người dùng
tien = 50000

# Khởi tạo danh sách sản phẩm (tên, giá, số lượng)
san_pham = {
    1: {"ten": "Nước suối", "gia": 10000, "ton": 5},
    2: {"ten": "Bánh snack", "gia": 15000, "ton": 3},
    3: {"ten": "Trà sữa", "gia": 25000, "ton": 2},
    4: {"ten": "Coca cola", "gia": 10000, "ton": 3}
} # Có thể tạo thêm sản phảm 

# Tạo vòng lập
while True:
    
# Hiển thị menu sản phẩm

    print("\n--- MENU SẢN PHẨM ---") # Tiêu đề
    for i in san_pham: # Duyệt từng sản phẩm
        sp = san_pham[i] # Lấy thông tin sản phẩm
        print(f"{i}. {sp['ten']} - {sp['gia']}đ (Còn: {sp['ton']})")  # In chi tiết sản phẩm

    print("0. Thoát") # Thoát giao diện
    print("/. Nạp tiền") # Nạp tiền ban đầu
    print(f"Số tiền của bạn: {tien}đ") # Hiển thị tiền đang có
    
     # Người dùng chọn sản phẩm
    chon = input("Chọn sản phẩm: ")

    # THOÁT
    if chon == "0":
        print("______________________________")
        print("Cảm ơn bạn đã sử dụng máy bán hàng!")
        break

    # NẠP TIỀN
    elif chon == "/":
        nap = int(input("Nhập số tiền muốn nạp: "))
        if nap > 0:
            tien += nap # nap cộng vào tien
            print("______________________________")
            print(f"Nạp thành công! Số dư: {tien}đ")
        else:
            print("______________________________")
            print("Số tiền không hợp lệ!")

    # MUA HÀNG
    elif chon.isdigit(): # Kiểm tra xem nhập có phải là số
        chon = int(chon)
        if chon in san_pham:
            sp = san_pham[chon]
            if sp["ton"] <= 0: # Ton ít hơn 0
                print("______________________________")
                print("Sản phẩm đã hết hàng!")
            elif tien < sp["gia"]: # Tiền đang có ít hơn giá
                print("______________________________")
                print("Bạn không đủ tiền!")
            else:
                tien -= sp["gia"] # Tiền đang có trừ giá
                sp["ton"] -= 1 # Tồn của sp giảm
                print("______________________________")
                print(f"Mua thành công {sp['ten']}!")
        else:
            print("______________________________")
            print("Sản phẩm không tồn tại!")
    else: # Nếu nhập không phải số
        print("______________________________")
        print("Lựa chọn không hợp lệ!")
