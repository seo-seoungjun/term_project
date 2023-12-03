from ...utils import load_config
from .hf_textgen import HFTextGenerator
import logging

logger = logging.getLogger(__name__)


def llm(provider: str = None, **kwargs):

    # load config
    if provider is None:
        # attempt to load config from environment variable LLMX_CONFIG_PATH
        config = load_config()
        if config:
            provider = config["model"]["provider"]
            kwargs = config["model"]["parameters"]
    if provider is None:
        logger.info("No provider specified. Defaulting to 'huggingface'.")
        provider = "huggingface"
    
    if provider.lower() == "huggingface" or provider.lower() == "default":
        return HFTextGenerator(**kwargs)

    else:
        raise ValueError(
            f"Invalid provider '{provider}'.  Supported provider is only 'huggingface' due to open source licensing."
        )
