from manim import *
class Screw(VMobject):
    def __init__(self,**kwargs):
        super().__init__(
            self,
            color=YELLOW_A,
            **kwargs
        )
        points=[]
        for i in range(-4,5):
            if i%2==0:
                second_coord=-4
            else:
                second_coord=4
            point=np.array([i,second_coord,0])
            points.append(point)
        self.set_points_as_corner([
            points
        ])
class ScrewScene(Scene):
    def construct(self):
        screw=Screw()
        self.play(Create(screw))
        self.wait()