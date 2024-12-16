from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

# 其他路由...

if __name__ == '__main__':
    app.run() 