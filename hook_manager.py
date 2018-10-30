class HookManager:

    def __init__(self, func=None):
        if func:
            self.func = func
        self.handlers = {}

    def __get__(self, obj, type=None):
        return self.__class__(self.func.__get__(obj, type))

    def __call__(self, *args, **kw):
        print 'Entering %s' % self.func
        return self.func(*args, **kw)

    def hook_register(self, company_name, hook_type, *args):
        hook_type = company_name + ":" + hook_type
        if hook_type in self.handlers:
            return True
            
    def call(self, company_name, hook_type, *args, **kwargs):
        hook_type = company_name + ":" + hook_type
        if hook_type in self.handlers:
            return self.handlers[hook_type](*args, **kwargs)

    def hook(self, hook_type):
        def registerhandler(handler):
            self.func = handler
            self.handlers[hook_type] = self.__get__(handler)
            return handler
        return registerhandler

    def hook_function(self, hook_type):
        def registerhandler(handler):
            self.handlers[hook_type] = handler
            return handler
        return registerhandler
