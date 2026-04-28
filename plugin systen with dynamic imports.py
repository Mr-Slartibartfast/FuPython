import importlib
import os

PLUGIN_FOLDER = "plugins"

class PluginManager:
    def __init__(self):
        self.plugins = []

    def load_plugins(self):
        for file in os.listdir(PLUGIN_FOLDER):
            if file.endswith(".py"):
                module_name = file[:-3]
                module = importlib.import_module(f"{PLUGIN_FOLDER}.{module_name}")
                if hasattr(module, "run"):
                    self.plugins.append(module)

    def run_all(self):
        for plugin in self.plugins:
            plugin.run()

if __name__ == "__main__":
    manager = PluginManager()
    manager.load_plugins()
    manager.run_all()