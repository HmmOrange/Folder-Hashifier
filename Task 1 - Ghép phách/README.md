# Task 1 - Ghép phách (log file xlsx)

## I. Điều kiện
- `xlsxwriter` - `pip install xlsxwriter` (ghi file xlsx)

## II. Cách sử dụng
### 1. Xác định directory của folder code của thí sinh và thay thế vào biến `source_folder` ở trong code.
- Folder thí sinh nên có dạng:
```
📂 Folder gốc
╰ 📂 Thí sinh 1
  ╰ 📄(Tên bài 1).cpp
  ╰ 📄(Tên bài 2).cpp
  ...

╰ 📂Thí sinh 2
  ╰ 📄(Tên bài 1).cpp
  ╰ 📄(Tên bài 2).cpp
  ...
```

- Ví dụ directory đến folder code thí sinh là `C:\Users\Admin\Documents\Thí sinh` thì điền trong code là
```py
source_folder = r"C:\Users\Admin\Documents\Participants Code"
```

### 2. Xác định directory của folder phách và thay thế vào biến `destination_folder`. 
- Ví dụ directory đến folder phách là `C:\Users\Admin\Documents\Phách` thì điền trong code là
```py
destination_folder = r"C:\Users\Admin\Documents\Phách"
```

### 3. Chạy code Python bằng cách sử dụng IDE yêu thích của bạn hoặc dùng cmd/terminal - `python "Task 1.py"`

Khi script chạy xong, các dữ liệu của phách được lưu trong file `HashLog.xlsx`