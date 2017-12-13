from hook_manager import HookManager
hm = HookManager()
from flask import Flask
app = Flask(__name__)
app.debug = 1

@app.route('/')
def hello_world():
    from main import Test
    return Test()
