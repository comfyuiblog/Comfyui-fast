import os
import folder_paths

now_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = folder_paths.get_input_directory()
output_dir = folder_paths.get_output_directory()

class TextInputNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "user_text": ("STRING", {
                    "default": "Enter your prompt here...",
                    "multiline": True
                })
            }
        }

    RETURN_TYPES = ("TEXT",)
    FUNCTION = "get_text"
    CATEGORY = "Comfyuiblog"

    def get_text(self, user_text):
        return (user_text,)

class LoadVideoNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video_path": ("STRING", {
                    "default": "path/to/video.mp4",
                    "multiline": False
                })
            }
        }

    RETURN_TYPES = ("VIDEO",)
    FUNCTION = "load_video"
    CATEGORY = "Comfyuiblog"

    def load_video(self, video_path):
        # Ensure the video path exists
        if os.path.exists(video_path):
            return (video_path,)
        else:
            return ("Video file not found",)

class PreviewVideoNode:  # Fixed class name from PreViewVideo to PreviewVideoNode
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video": ("VIDEO",),
            }
        }

    CATEGORY = "Comfyuiblog"
    DESCRIPTION = "Preview the selected video file."

    RETURN_TYPES = ()
    OUTPUT_NODE = True
    FUNCTION = "preview_video"

    def preview_video(self, video):
        video_name = os.path.basename(video)
        video_path_name = os.path.basename(os.path.dirname(video))
        return {"ui": {"video": [video_name, video_path_name]}}


# Update NODE_CLASS_MAPPINGS to include LoadVideoNode and others
NODE_CLASS_MAPPINGS = {
    "Text to Prompt": TextInputNode,
    "Preview Video": PreviewVideoNode,  # Ensure this matches the class name
    "Load Video": LoadVideoNode  # Ensure this is added
}

prompt_sr = 16000
WEB_DIRECTORY = "./web"
