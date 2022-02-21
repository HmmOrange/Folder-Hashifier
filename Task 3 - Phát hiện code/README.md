# Task 3 - Phát hiện code (Bonus :>)
Script `Task 3.py` có thể tìm kiếm một đoạn code bất kỳ trong folder phách

## Cách sử dụng
### 1. Xác định directory của folder phách và thay thế vào biến `target_folder` ở dòng 5 trong code.
- Ví dụ directory đến folder code thí sinh là `C:\Users\Admin\Documents\Phách` thì điền trong code là
```py
5 | target_folder = r"C:\Users\Admin\Documents\Phách"
```
### 2. Khởi tạo các đoạn code của các thí sinh ở dòng 6 theo cấu trúc Directories của Python
- Cấu trúc: 
```py
target_code = {
    "Ten1": "Code1",
    "Ten2": "Code2",
    ...
    "TenN": "CodeN"
}
```
### 3. Khi script chạy xong, các file có thể chứa code như đã cho sẽ được show ở trong cmd/terminal:<br>
![Ví dụ]("VD.png")

