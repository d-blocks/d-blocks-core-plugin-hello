from dblocks_core.model import plugin_model


class ExamplePlugin(plugin_model.PluginHello):
    """
    This is the example plugin for d-blocks-core.

    Args:
        plugin_model (_type_): _description_
    """

    def hello(self) -> str:
        return "Hello, world!"
