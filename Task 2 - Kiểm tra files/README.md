# Task 2 - Kiểm tra files
Script `Task 2.py` có thể kiểm tra:
- Tên file hợp lệ với yêu cầu
- Đọc/ghi file trong code
- Compile Error

Việc đầu tiên cần làm là xác định directory của folder **phách** và thay thế vào biến `target_folder` ở dòng 5 trong code.
- Ví dụ directory đến folder code thí sinh là `C:\Users\Admin\Documents\Phách` thì điền trong code là
```py
target_folder = r"C:\Users\Admin\Documents\Phách"
```

## * Điều kiện:
- Có g++ compiler install trong path

## I. Kiểm tra tên file
- Cần khởi tạo các tên files hợp lệ trong code theo dạng list của Python (biến `file_name_list`). Ví dụ:
```py
file_name_list = ['bai1.cpp', 'bai2.cpp', 'bai3.cpp', '309A.cpp']
```

## II. Kiểm tra đọc/ghi files
- Script sẽ kiểm tra xem có tồn tại file input ở trong code hay không (ví dụ tên bài là `A.cpp` thì sẽ check có `A.inp` ở trong bài hay không).

## III. Kiểm tra Compile Error
- Script sẽ kiểm tra xem có compile được các file hay không. Khi code chạy sẽ có có file `tmp.txt` và các file `.exe` được tạo ra trong quá trinh compile, bạn có thể bỏ qua :)

Kết quả sẽ được log ở trong file `log.txt`
