# Basic Data Processing and Computing Utilities

Dự án này bao gồm 3 file Python thực hiện các chức năng khác nhau, từ tính thuế, kiểm tra mật khẩu đến xử lý mảng dữ liệu.

# 1. Calculate tax payable.py
## Mô tả
- File này tính toán số thuế phải nộp dựa trên thu nhập được cung cấp.
- Quy tắc tính thuế:
  - Thu nhập ≤ 10,000: Thuế = 0.
  - Thu nhập từ 10,001 đến 20,000: Thuế = 10% của phần thu nhập vượt quá 10,000.
  - Thu nhập > 20,000: Thuế = 20% của phần thu nhập vượt quá 20,000.
- Sử dụng
  - Người dùng nhập thu nhập của mình.
  - Chương trình sẽ xuất ra số thuế phải nộp.
# 2. Check valid password.py
## Mô tả
- File này kiểm tra xem một mật khẩu có hợp lệ hay không.
- Điều kiện để mật khẩu hợp lệ:
  - Có ít nhất 1 chữ cái thường.
  - Có ít nhất 1 chữ cái viết hoa.
  - Có ít nhất 1 chữ số.
  - Có ít nhất 1 ký tự đặc biệt trong nhóm [$, @, #].
  - Độ dài mật khẩu nằm trong khoảng từ 6 đến 12 ký tự.
- Sử dụng
  - Người dùng cung cấp mật khẩu.
  - Chương trình trả về kết quả "Valid password" (hợp lệ) hoặc "Invalid password" (không hợp lệ).
# 3. Format & remove duplicates in an array.py
## Mô tả
- File này xử lý một mảng chuỗi, bao gồm:
  - Loại bỏ khoảng trắng thừa.
  - Viết hoa chữ cái đầu tiên của mỗi chuỗi.
  - Loại bỏ các giá trị trùng lặp.
  - Sắp xếp các giá trị đã chuẩn hóa theo thứ tự bảng chữ cái.
- Sử dụng
  - Người dùng cung cấp một mảng chuỗi.
  - Chương trình trả về mảng đã chuẩn hóa và sắp xếp.
