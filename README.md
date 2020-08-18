# Flimbun : A Chat App

![Screenshot from 2020-07-03 12-05-27](https://user-images.githubusercontent.com/55910733/86439411-2b3c4b00-bd26-11ea-8e76-8ce0662fc33a.png)

![Screenshot from 2020-07-03 12-06-19](https://user-images.githubusercontent.com/55910733/86439506-5030be00-bd26-11ea-8235-4da880f56933.png)

# Setup

1) Installing Required Files

#### `For Windows:`

```javascript
pip install -r requirements.txt
```
#### `For Linux/Mac:`

```lang-python
pip3 install -r requirements.txt
```

2) Run your redis on port: 6379 (you may use docker as below)

```javascript
sudo apt install docker.io
sudo docker run -p 6379:6379 -d redis:5
```
3) Run the devlopment server:

#### `For Windows:`

```lang-python
python manage.py runserver
```

#### `For Linux/Mac:

```lang-python
python3 manage.py runserver
```

4) Go to the url shown in terminal say, 127.0.0.1:8000/admin and use following username and password:

```javascript
username: gitest
password: gitest
```

hey you got it! HAPPY SURFING :)

## Maintainers

- [itechindrustries](https://github.com/ItechIndrustries)
- [a.techguy.r](https://github.com/atechguyr)

## License
MIT - [See LICENSE](./LICENSE)

## Change Log
* Version 0.1 - Initial commit

## Contribution

If you're new to contributing to Open Source on Github, [this guide](https://guides.github.com/activities/contributing-to-open-source/) can help you get started. We're a warm and welcoming community of open source contributors. Please join. All types of contribution are welcome.

###### This repository is just a small subset of work put together by a much larger pool of voluntary efforts contributed by generous people all around the world. Reach out to us through itechindrustries@gmail.com
