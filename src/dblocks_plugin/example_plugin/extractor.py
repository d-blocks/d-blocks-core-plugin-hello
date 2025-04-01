from dblocks_core.config.config import logger
from dblocks_core.model import meta_model, plugin_model


class EverySecondInScope(plugin_model.PluginExtractIsInScope):
    def __init__(self):
        self.counter = 0

    def is_in_scope(
        self,
        obj: meta_model.IdentifiedObject,
        **kwargs,
    ) -> bool:
        self.counter = self.counter + 1
        if self.counter % 2 == 1:
            logger.info(
                f"Keep in scope: {obj.object_type}: {obj.database_name}.{obj.object_name}"
            )
            return True
        logger.warning(
            f"DESCOPE: {obj.object_type}: {obj.database_name}.{obj.object_name}"
        )
        return False
