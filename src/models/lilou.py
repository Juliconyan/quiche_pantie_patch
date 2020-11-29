from PIL import Image
from src.models.amanatsu import patcher


class patcher(patcher):
    def __init__(self, body='./body/body_lilou.png', **options):
        super().__init__(**options)
        self.name = "リル"
        self.body = Image.open(body)
        self.body_size = self.body.size
