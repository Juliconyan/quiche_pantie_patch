from PIL import Image


class patcher():
    def __init__(self, name, body="./body/body.png", pantie_position=[0, 0], options=[]):
        self.name = name
        self.body = Image.open(body)
        self.body_size = self.body.size
        self.pantie_position = pantie_position
        self.options = options

    def convert(self, image):
        return image

    def patch(self, image, transparent=False):
        image = self.convert(image)
        if transparent:
            patched = Image.new("RGBA", self.body_size)
        else:
            patched = self.body.copy()
            
        patched.paste(image, self.pantie_position, image)
        return patched

    def save(self, image, fname):
        image.save(fname)
