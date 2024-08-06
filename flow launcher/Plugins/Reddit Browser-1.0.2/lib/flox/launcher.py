# -*- coding: utf-8 -*-
import json
import sys

"""
Slightly modified wox.py credit: https://github.com/Wox-launcher/Wox
"""

class Launcher(object):
    """
    Launcher python plugin base
    """

    def __init__(self, API):
        rpc_request = {'method': 'query', 'parameters': ['']}
        if len(sys.argv) > 1:
            rpc_request = json.loads(sys.argv[1])
        # proxy is not working now
        # self.proxy = rpc_request.get("proxy",{})
        request_method_name = rpc_request.get("method")
        #transform query and context calls to internal flox methods
        if request_method_name == 'query' or request_method_name == 'context_menu':
            request_method_name = f"_{request_method_name}"
        request_parameters = rpc_request.get("parameters")

        request_method = getattr(self, request_method_name)
        try:
            results = request_method(*request_parameters)
        except Exception as e:
            try:
                self.logger.exception(f'Exception while calling method: {request_method_name}')
            except AttributeError:
                pass
            raise
        if request_method_name == "_query" or request_method_name == "_context_menu":
            print(json.dumps({"result": results}))

    def query(self,query):
        """
        sub class need to override this method
        """
        return []

    def context_menu(self, data):
        """
        optional context menu entries for a result
        """
        return []

    def debug(self,msg):
        """
        alert msg
        """
        print("DEBUG:{}".format(msg))
        sys.exit()

    def change_query(self, query, requery=False):
        """
        change query
        """
        print(json.dumps({"method": f"{self.api}.ChangeQuery","parameters":[query,requery]}))

    def shell_run(self, cmd):
        """
        run shell commands
        """
        print(json.dumps({"method": f"{self.api}.ShellRun","parameters":[cmd]}))

    def close_app(self):
        """
        close launcher
        """
        print(json.dumps({"method": f"{self.api}.CloseApp","parameters":[]}))

    def hide_app(self):
        """
        hide launcher
        """
        print(json.dumps({"method": f"{self.api}.HideApp","parameters":[]}))

    def show_app(self):
        """
        show launcher
        """
        print(json.dumps({"method": f"{self.api}.ShowApp","parameters":[]}))

    def show_msg(self, title, sub_title, ico_path=""):
        """
        show messagebox
        """
        print(json.dumps({"method": f"{self.api}.ShowMsg","parameters":[title,sub_title,ico_path]}))

    def open_setting_dialog(self):
        """
        open setting dialog
        """
        self.logger.debug(json.dumps({"method": f"{self.api}.OpenSettingDialog","parameters":[]}))
        print(json.dumps({"method": f"{self.api}.OpenSettingDialog","parameters":[]}))

    def start_loadingbar(self):
        """
        start loading animation in wox
        """
        print(json.dumps({"method": f"{self.api}.StartLoadingBar","parameters":[]}))

    def stop_loadingbar(self):
        """
        stop loading animation in wox
        """
        print(json.dumps({"method": f"{self.api}.StopLoadingBar","parameters":[]}))

    def reload_plugins(self):
        """
        reload all launcher plugins
        """
        print(json.dumps({"method": f"{self.api}.ReloadPlugins","parameters":[]}))
