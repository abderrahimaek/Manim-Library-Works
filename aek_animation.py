from manim import *

class scene1(Scene):
    def construct(self):
        rect= MathTex(r'\mathbb{AEK}')
        rect.scale(3)

        self.play(Write(rect), run_time=2)

        self.wait(1)


      