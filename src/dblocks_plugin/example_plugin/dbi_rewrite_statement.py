from dblocks_core.config.config import logger
from dblocks_core.model import meta_model, plugin_model


class DbiRewrite(plugin_model.PluginDBIRewriteStatement):

    def rewrite_statement(self, statement: str) -> str:
        """The function comments out bteq directives (naive and very brittle approach)"""
        out_lines = []
        for line in statement.splitlines():
            if line.strip().startswith("."):
                line = "--BTEQ-- " + line
            out_lines.append(line)
        return "\n".join(out_lines) + "\n"
