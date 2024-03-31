import math
from manim import*
import numpy as np

class Dancetitle(Scene):
    def construct(self):
        tit= Text("The Dance of Cos & Sin").scale(1.5)
        self.play(Write(tit), rate_func=smooth, run_time=2)
        self.wait(10)
        self.remove(tit, run_time=10)


class CosSin(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-10, 10, 2],
            y_range=[-2, 2, 1],
            tips=False,
            axis_config={"color": WHITE,"include_numbers": True},
            y_axis_config={"include_numbers": True},

        )
      

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: math.cos(x) , color=RED, use_smoothing=True )
        graph1 = ax.plot(lambda x: math.sin(x) ,color=BLUE, use_smoothing=False )
        self.play(Write(ax),rate_func=smooth, run_time=10)
        self.play(Write(graph), rate_func=smooth, run_time=10)
        self.play(Write(graph1), run_time=10)

class FIN(Scene):
    def construct(self):
        rect= MathTex(r'\mathbb{AEK}')
        rect.scale(3)

        self.play(Write(rect), run_time=2)
        self.wait(1)
        self.remove(rect)
