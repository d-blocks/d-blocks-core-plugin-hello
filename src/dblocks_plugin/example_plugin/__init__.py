from dblocks_plugin.example_plugin.dbi_rewrite_statement import DbiRewrite
from dblocks_plugin.example_plugin.extractor import EverySecondInScope
from dblocks_plugin.example_plugin.file_writer import HelloWriter
from dblocks_plugin.example_plugin.hello import ExamplePlugin

PLUGINS = [
    ExamplePlugin(),
    HelloWriter(),
    EverySecondInScope(),
    DbiRewrite(),
]
