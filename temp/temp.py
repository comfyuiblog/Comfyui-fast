import os

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


class PreviewVideoNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video": ("VIDEO",), 
            }
        }

    CATEGORY = "Comfyuiblog"  
    DESCRIPTION = "hello world!"  

    RETURN_TYPES = () 
    OUTPUT_NODE = True  

    FUNCTION = "load_video"  

    def load_video(self, video):
 
        video_name = os.path.basename(video)
        video_path_name = os.path.basename(os.path.dirname(video))
        
    
        print(f"Processing video: {video_name} in directory: {video_path_name}")
        
     

NODE_CLASS_MAPPINGS = {
    "Text to Prompt": TextInputNode,
    "Preview Video": PreviewVideoNode
}
