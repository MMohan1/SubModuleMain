from routes import hm

def Test():
    out_str = "From base Module "
    if hm.call("hook_test_resistration"):
        return out_str + hm.call("hook_test_resistration") + hm.call("hook_test_resistration_new")
