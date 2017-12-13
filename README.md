1. Follow this link for that - https://git-scm.com/book/en/v2/Git-Tools-Submodules
2. How to make an Flask using SubModule and How it will work
    1. Parent Repo
    2. Child Repo
3. The parent app have the basic flak config.
4. There is a hook manager
    1. Used to resister a hook
    2. Used to call registered hook
5. How it will work
    1. In the parent repo basic code will be there, The client spacific code will be in Child repo
    2. In the child repo for a function that we need to call from parent(the cutomization code for parent) have to resister in hook manager.
    3. If the customise code is in function then the @hook_function(“hook_test_resistration_new”) , if it is class function then hook('hook_test_resistration’)
    4. Function or code from we have to call the cutom code we have to call hm.call("hook_test_resistration”) or hm.call("hook_test_resistration_new”).
    5. The hook custom code will always return the output
    6. One hook have one custom code not multiple
    7. The parent config will be rewritten from the child config
6. The projet structure (This could be make according the user also this is a example only) -
    1. SubModuleMain(Parent)
        1.  SubModuleTest/
        2.  README.md
        3.  __init__.py
        4.  config_template.py
        5.  configreader.py
        6.  constants.py
        7.  app.ini
        8.  hook_manager.py
        9.  main.py
        10.  routes.py
        11.  run.py
    2. The SubModuleTest is the child director here and the hook manager class is initiated in the routes files so no the all hooks will be resister at the application start only.
    3. SubModuleTest(Child)
        1.   README.md
        2.    __init__.py
        3.    app.ini
        4.    run.py
        5.    sub_module_routes.py
    4. In the Child directory all the routes and imported in __init__.py file , all the hook class and functions also import there only.
    5. In the parent run.py file the submodule imported as “from SubModuleTest import *"
