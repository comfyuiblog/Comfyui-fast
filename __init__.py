# comfyu_comfyublognode/__init__.py
import os
import sys
import os.path as osp

try:
    comfy_utils = sys.modules["utils"]
except KeyError:
    print("Could not find comfy_utils module")

# Import nodes from temp/temp.py
from .temp.temp import TextInputNode, PreviewVideoNode

# Register nodes in ComfyUI
NODE_CLASS_MAPPINGS = {
    "Text to Prompt": TextInputNode,
    "Preview Video": PreviewVideoNode
}

# Reload comfy_utils module if needed
sys.modules["utils"] = comfy_utils
