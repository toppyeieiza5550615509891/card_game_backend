# card_game_backend
  เกม จับคู่ไพ่ โดยใช้ 
      stack 
          backend: fastapi (base on python)
          frontend: react

# Important
    - python >= 3.6
    - fastapi >= 0.61.0
  
# software require
   - docker
  
# API Docs
  รายละเอียดข้อมูลของแต่ละ api (ต้องเปิดเซิฟเวอร์ก่อน)
   - http://127.0.0.1:8000/docs

# Deploy
```
  $ docker build -t myimage .
  $ docker run -d --name mycontainer -p 8000:80 myimage
```
