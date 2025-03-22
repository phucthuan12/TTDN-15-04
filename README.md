Hệ thống quản lý dự án


![image](https://github.com/user-attachments/assets/6a147d32-42c7-4954-a616-28a16fafcff6)
1. Dự án
![image](https://github.com/user-attachments/assets/aea65e86-259f-45f2-82aa-0de339856700)
2. Quản lý nhiệm vụ
![image](https://github.com/user-attachments/assets/fc01d55f-4484-4fc7-b4f7-b20be50bc4cb)
3. Thời gian làm việc
![image](https://github.com/user-attachments/assets/8520454e-b269-4e8a-8a5e-f05b5ffe163b)
4. Tiến độ công việc
 ![image](https://github.com/user-attachments/assets/fd9e307b-f3b3-4e86-b269-0ebea3cb8e4a)
5. Rủi do dự án
![image](https://github.com/user-attachments/assets/48ff191e-e43a-431e-8e1a-6b43e14e7772)
6. Dự án trễ hạn
![image](https://github.com/user-attachments/assets/da1ea825-7a2a-4f1e-acf6-5f27e2c44c98)
7. Dashboard
![image](https://github.com/user-attachments/assets/4f2866c2-115e-4305-8033-6a5ef32b3f74)
![image](https://github.com/user-attachments/assets/656cc7e9-1bf3-4ce0-86aa-fc5f7d72f26f)


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
    
