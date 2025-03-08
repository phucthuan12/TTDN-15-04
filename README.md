Hệ thống quản lý dự án
1. Dự án
 ![image](https://github.com/user-attachments/assets/9513221a-b319-4618-8ecc-b4dc3e16cdc0)
2. Quản lý nhiệm vụ
   ![image](https://github.com/user-attachments/assets/9ac09873-c135-4185-8146-a0371bfa886f)
3. Thời gian làm việc
   ![image](https://github.com/user-attachments/assets/0360a9f8-254d-43a6-a6e4-d0274f638b37)
4. Tiến độ làm việc
   ![image](https://github.com/user-attachments/assets/34b01405-b429-4b57-bf81-e31870d2d53b)
5. Rủi do dự án
   ![image](https://github.com/user-attachments/assets/9c8be28d-3d02-41b6-ada8-44b3b4060ab2)
6. Dự án trễ hạn
   ![image](https://github.com/user-attachments/assets/6c64af82-ae83-4aa6-9508-51ae7b691b69)
7. Thống kê
   ![image](https://github.com/user-attachments/assets/a1f4e9b9-3dc5-4194-90b5-9241ab4b1412)




---
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)



# 1. Cài đặt công cụ, môi trường và các thư viện cần thiết

## 1.1. Clone project.
```
git clone https://gitlab.com/anhlta/odoo-fitdnu.git
```

```
git checkout cntt15_04
```


## 1.2. cài đặt các thư viện cần thiết

Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

```
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
```
## 1.3. khởi tạo môi trường ảo.

`python3.10 -m venv ./venv`
Thay đổi trình thông dịch sang môi trường ảo và chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu

```
source venv/bin/activate
pip3 install -r requirements.txt
```

# 2. Setup database

Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.

`docker-compose up -d`

# 3. Setup tham số chạy cho hệ thống

## 3.1. Khởi tạo odoo.conf

Tạo tệp **odoo.conf** có nội dung như sau:

```
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5434
xmlrpc_port = 8069
```

# 4. Chạy hệ thống và cài đặt các ứng dụng cần thiết

Lệnh chạy
```
python3 odoo-bin.py -c odoo.conf -u all
```


Người sử dụng truy cập theo đường dẫn _http://localhost:8069/_ để đăng nhập vào hệ thống.

Hoàn tất
    
