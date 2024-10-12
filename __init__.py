import os
import sys  # Missing import added
import folder_paths

now_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = folder_paths.get_input_directory()
output_dir = folder_paths.get_output_directory()

# Attempt to load comfy_utils module
try:
    comfy_utils = sys.modules["utils"]
except KeyError:
    comfy_utils = None
    print("Could not find comfy_utils module")

# Import nodes from temp/temp.py
from .temp.temp import TextInputNode, PreviewVideoNode, LoadVideoNode  # Import LoadVideoNode as well

# Register nodes in ComfyUI
NODE_CLASS_MAPPINGS = {
    "Text to Prompt": TextInputNode,
    "Preview Video": PreviewVideoNode,  # Ensuring class names are consistent
    "Load Video": LoadVideoNode
}

# Reload comfy_utils module if it was loaded
if comfy_utils is not None:
    sys.modules["utils"] = comfy_utils
