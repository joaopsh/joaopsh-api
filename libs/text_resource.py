import json
import glob
from pathlib import Path
from libs.language import current_language 

TEXT_RESOURCES_RELATIVE_PATH = 'text_resources/*.json'

class TextResource:
    cached_text_resources = {}    
    
    @classmethod
    def init_app(cls, app):
        
        for file in glob.glob(f'{app.root_path}/{TEXT_RESOURCES_RELATIVE_PATH}' ):
            with open(file) as file:
                resource_name = Path(file.name).stem
                cls.cached_text_resources[resource_name.lower()] = json.load(file)

    @classmethod
    def get_text(cls, text_id:str):
        return cls.cached_text_resources[current_language.lower()][text_id]
