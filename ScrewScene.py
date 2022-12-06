from manim import *
class Screw(VMobject):
    def __init__(self,**kwargs):
        super().__init__(
            
            color=YELLOW_A,
            **kwargs
        )
        self.set_points_as_corners([
            RIGHT,LEFT
        ])
class ScrewScene(Scene):
    def construct(self):
        screw=Screw()
        self.play(Create(screw))
        self.wait()