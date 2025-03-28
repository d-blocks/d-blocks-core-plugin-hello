from pathlib import Path
from textwrap import dedent

from dblocks_core.config.config import logger
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
