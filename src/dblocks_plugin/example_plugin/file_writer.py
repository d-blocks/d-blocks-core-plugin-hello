from pathlib import Path
from textwrap import dedent

from dblocks_core import logger
from dblocks_core.model import meta_model, plugin_model


class HelloWriter(plugin_model.PluginFSWriter):
    def before(
        self,
        path: Path,
        obj: meta_model.DescribedObject,
        ddl: str,
        **kwargs,
    ) -> str:
        """
        This function is executed before the file is written do disk (and returns the DDL script).
        The function is expected to return back either:
            - the DDL script (string), or
            - None, if the DDL script should not be changed.
        """
        logger.info(
            dedent(
                f"""
            Hello!
            path is : {path.as_posix()}
            obj is : {obj.identified_object.database_name}.{obj.identified_object.object_name}
            """
            )
        )
        try:
            content = path.read_text(encoding="utf-8", errors="strict")
        except FileNotFoundError:
            # the file does not exist, return None, which indicates we did not change the DDL
            return None

        content = _do_something_on_ddl(content)
        return content

    def after(
        self,
        path: Path,
        obj: meta_model.DescribedObject,
        **kwargs,
    ):
        """This function is executed after the file is written do disk."""
        logger.info(
            dedent(
                f"""
            Hello!
            path is : {path.as_posix()}
            obj is : {obj.identified_object.database_name}.{obj.identified_object.object_name}
            """
            )
        )


def _do_something_on_ddl(content: str) -> str:
    # do something with the content
    header = "-- changed the ddl"
    if header not in content:
        content = header + "\n" + content
    return content
