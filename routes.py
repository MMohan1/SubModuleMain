from hook_manager import HookManager
hm = HookManager()
import json
from flask import Flask
app = Flask(__name__)
app.debug = 1

@app.route('/')
def hello_world():
    from main import Test
    return Test()


@app.route('/get/ini')
def get_config():
    from run import config_dict
    return json.dumps(config_dict)