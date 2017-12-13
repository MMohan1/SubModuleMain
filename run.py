from routes import app, hm
import os
sub_module_ini = ""
from SubModuleTest import *
from configreader import ConfigReaderWrapper
cfgreader = ConfigReaderWrapper()
app_ini = "app.ini"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
ini_path = APP_ROOT + "/" + app_ini
def overwrite_ini_values():
    project_config = cfgreader.get_config_dict(ini_path)
    if sub_module_ini:
        argument_ini_dict = cfgreader.get_config_dict(sub_module_ini, refresh=True, validate_required=False)
        for sections in argument_ini_dict:
            for sections_key in argument_ini_dict[sections]:
                if argument_ini_dict[sections][sections_key] != project_config[sections][sections_key]:
                    project_config[sections][sections_key] = argument_ini_dict[sections][sections_key]
    return project_config


config_dict = overwrite_ini_values()

if __name__ == "__main__":
    app.run()