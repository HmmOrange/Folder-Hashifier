# Task 3 - Phát hiện code (Bonus :>)
Script `Task 3.py` có thể tìm kiếm một đoạn code bất kỳ trong folder phách

## Cách sử dụng
### 1. Xác định directory của folder phách và thay thế vào biến `target_folder` trong code.
- Ví dụ directory đến folder code thí sinh là `C:\Users\Admin\Documents\Phách` thì điền trong code là
```py
target_folder = r"C:\Users\Admin\Documents\Phách"
```
### 2. Khởi tạo các đoạn code của các thí sinh (biến `target_code`) theo cấu trúc Directories của Python
- Cấu trúc: 
```py
target_code = {
    "Ten1": "Code1",
    "Ten2": "Code2",
    ...
    "TenN": "CodeN"
}
```

Kết quả sẽ được log ở trong file `log.txt`
