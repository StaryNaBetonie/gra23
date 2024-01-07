class Animation:
    def __init__(self, images, duration=5, loop=True) -> None:
        self.images = images
        self.duration = duration
        self.loop = loop
        self.done = False
        self.frame = 0
    
    def image(self):
        return self.images[int(self.frame / self.duration)]

    def copy(self):
        return Animation(self.images, self.duration, self.loop)

    def update(self):
        if self.loop: self.frame = (self.frame + 1) % (self.duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.duration * len(self.images) - 1)
            if self.frame >= self.duration * len(self.images) - 1:
                self.done = True