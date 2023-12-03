from dataclasses import asdict
import sys
import logging
import json
from typing import Any, Union, Dict
import tiktoken
from diskcache import Cache
import hashlib
import os
import platform
import requests
import yaml

logger = logging.getLogger(__name__)


def num_tokens_from_messages(messages, model="codellama/CodeLlama-34b-Python-hf"):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if (
        model == "codellama/CodeLlama-34b-Python-hf" or True
    ):  # note: future models may deviate from this
        num_tokens = 0
        for message in messages:
            if not isinstance(message, dict):
                message = asdict(message)

            num_tokens += (
                4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            )

            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":  # if there's a name, the role is omitted
                    num_tokens += -1  # role is always required and always 1 token
        num_tokens += 2  # every reply is primed with <im_start>assistant
        return num_tokens


def cache_request(cache: Cache, params: dict, values: Union[Dict, None] = None) -> Any:
    # Generate a unique key for the request

    key = hashlib.md5(json.dumps(params, sort_keys=True).encode("utf-8")).hexdigest()
    # Check if the request is cached
    if key in cache and values is None:
        # print("retrieving from cache")
        return cache[key]

    # Cache the provided values and return them
    if values:
        # print("saving to cache")
        cache[key] = values
    return values


def get_user_cache_dir(app_name: str) -> str:
    system = platform.system()
    if system == "Windows":
        cache_path = os.path.join(os.getenv("LOCALAPPDATA"), app_name, "Cache")
    elif system == "Darwin":
        cache_path = os.path.join(os.path.expanduser("~/Library/Caches"), app_name)
    else:  # Linux and other UNIX-like systems
        cache_path = os.path.join(
            os.getenv("XDG_CACHE_HOME", os.path.expanduser("~/.cache")), app_name
        )
    os.makedirs(cache_path, exist_ok=True)
    return cache_path


def load_config(config_path: str = "LLMX_CONFIG_PATH"):
    try:
        config_path = os.environ.get(config_path, None)
        if config_path is not None:
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    config = yaml.safe_load(f)
                    logger.info(
                        f"Loaded config {config['model']['provider']} from '%s'.",
                        config_path)
                    return config
            except FileNotFoundError as file_not_found:
                logger.info(
                    "Error: Config file not found at '%s'. Please check the LLMX_CONFIG_PATH environment variable. %s",
                    config_path,
                    str(file_not_found))
            except IOError as io_error:
                logger.info(
                    "Error: Could not read the config file at '%s'. %s",
                    config_path, str(io_error))
            except yaml.YAMLError as yaml_error:
                logger.info(
                    "Error: Malformed YAML in config file at '%s'. %s",
                    config_path, str(yaml_error))
        else:
            logger.info(
                "Info:LLMX_CONFIG_PATH environment variable is not set. Please set it to the path of your config file to setup your default model.")
    except Exception as error:
        logger.info("Error: An unexpected error occurred: %s", str(error))

    return None
