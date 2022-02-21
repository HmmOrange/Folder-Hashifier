# Task 2 - Kiểm tra files
Script `Task 2.py` có thể kiểm tra:
- Tên file hợp lệ với yêu cầu
- Đọc/ghi file trong code
- Compile Error

Việc đầu tiên cần làm là xác định directory của folder **phách** và thay thế vào biến `target_folder` ở dòng 5 trong code.
- Ví dụ directory đến folder code thí sinh là `C:\Users\Admin\Documents\Phách` thì điền trong code là
```py
5 | target_folder = r"C:\Users\Admin\Documents\Phách"
```

## * Điều kiện:
- Có g++ compiler install trong path

## I. Kiểm tra tên file
- Cần khởi tạo các tên files hợp lệ ở dòng 6 trong code theo dạng list của Python.
- Khi script chạy xong, các tên bài không hợp lệ sẽ được show ở trong cmd/terminal:<br>
![Ví dụ]("VD1.png")

## II. Kiểm tra đọc/ghi files
- Script sẽ kiểm tra xem có tồn tại file input ở trong code hay không (ví dụ tên bài là `A.cpp` thì sẽ check có `A.inp` ở trong bài hay không)
- Khi script chạy xong, các file chưa có input file sẽ được show ở trong cmd/terminal:<br>
![Ví dụ]("VD2.png")

## III. Kiểm tra Compile Error
- Script sẽ kiểm tra xem có compile được các file hay không. Khi code chạy sẽ có có file `tmp.txt` và các file `.exe` được tạo ra trong quá trinh compile, bạn có thể bỏ qua :)
- Khi script chạy xong, các file chưa có input file sẽ được show ở trong cmd/terminal:<br>
![Ví dụ]("VD3.png")

