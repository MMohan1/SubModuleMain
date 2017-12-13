import os,sys
from ConfigParser import SafeConfigParser
import config_template

config_template_dict=config_template.template_dict

class ConfigReaderWrapper():
    """
    """
    def __init__(self):
        self.cfgdict = None

    

    def _read_configurations_from_ini(self, inifilepath):
        if not inifilepath.endswith('.ini'):
            print "Configrations could only be read from an 'ini' file"
            sys.exit(1)
        if not os.path.exists(inifilepath):
            print 'No such config file %s' % (inifilepath)
            sys.exit(1)
        cfg = SafeConfigParser()
        cfg.read(inifilepath)
        cfg_ini_dict = self._config_as_dict(cfg)
        return cfg_ini_dict


    def _validate_config_dict(self, config_dict):
        for key in config_template_dict.keys():
            if key in config_dict:
                template_value_dict = config_template_dict[key]
                for inner_key in template_value_dict:
                    if not inner_key in config_dict[key]:
                        print 'Missing key for %s is added Key-%s' %(key,inner_key)
                        config_dict[key][inner_key]=template_value_dict[inner_key]
            else:
                print "Adding ",key
                config_dict[key]=config_template_dict[key]
        return config_dict

    def _config_as_dict(self, cfg):
        """
        """
        cfg_dict = {}
        for section in cfg.sections():
            cfg_dict[section] = {}
            for k, v in cfg.items(section):
                cfg_dict[section][k] = v
        return cfg_dict
        
    def get_config_dict(self, inifilepath, ha_constants=None, refresh=False,validate_required=True):
        if refresh:
            self.cfgdict = None
        if not self.cfgdict:
            cfg_ini_dict = self._read_configurations_from_ini(inifilepath)
            if not validate_required:
                return cfg_ini_dict
            self.cfgdict = self._validate_config_dict(cfg_ini_dict)
        return self.cfgdict

