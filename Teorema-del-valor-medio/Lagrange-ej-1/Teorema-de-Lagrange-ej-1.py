# High quality
# %%manim -qh -v WARNING MainScene

# Low quality
%%manim -ql -v WARNING MainScene


# Imports
# from manim import *
# import math

config.background_color = "#000000"
config.frame_width = 15
config.frame_height = 15

config.pixel_width = 960
config.pixel_height = 960

x1 = 4
x2 = 8.5
r1 = 6.25

class MainScene(Scene):

  def construct(self):

    axis = Axes(
      x_range=[-1.5, 15.5, 1],
      y_range=[-2.5, 9.5, 1],
      x_length=15,
      y_length=10,
      tips=False,
      axis_config={
        "include_numbers": True,
        "font_size": 25
      },
    )

    plane = NumberPlane(
      x_range=[-1.5, 15.5, 1],
      y_range=[-2.5, 9.5, 1],
      x_length=15,
      y_length=10,
      background_line_style={
        "stroke_color": GRAY,
        "stroke_width": 1,
        "stroke_opacity": 0.6
      }
    )

    origin = Dot(
      point=axis.c2p(0, 0),
      color=GRAY_A,
      radius=0.1
    )

    # Funcion
    fxTex = MathTex(r'f(x) = -\frac{(x-7)^{2}}{3} + 5', font_size=40, color=WHITE)
    fxTex.move_to(axis.c2p(1, 8) + fxTex.get_critical_point(DR) - fxTex.get_critical_point(ORIGIN))

    def fx(x):
      return -math.pow(x - 7, 2) / 3 + 5

    FX = axis.plot(fx)
    FX2 = axis.plot(fx, x_range=[x1, x2], color=YELLOW, z_index=5)

    X1 = axis.c2p(x1, fx(x1), 0)
    X2 = axis.c2p(x2, fx(x2), 0)

    # Recta secante
    line = Line(
      start=X1 + (X2 - X1) * -0.5,
      end=X1 + (X2 - X1) * 1.5,
      color=GREEN_D
    )

    # Points
    pointX1 = Dot(
      point=X1,
      z_index=10,
      color=RED
    )
    pointX2 = Dot(
      point=X2,
      z_index=10,
      color=RED_B
    )

    pointR1 = Dot(
      point=axis.c2p(r1, fx(r1)),
      z_index=10,
      color=TEAL_B
    )


    modelLine = Line(
      start=X1 + (X2 - X1) * 0.2,
      end=X1 + (X2 - X1) * 1,
      color=BLUE_E
    )
    lineR1 = modelLine.copy().move_to(pointR1.get_center())

    def getLineToAxisX(point, color = GRAY_A, text = None):

      x, y, z = point.get_center()

      line = axis.get_line_from_axis_to_point(
        index=0,
        point=[x, y, z],
        color=color,
        line_config={
          "dash_length": 0.1,
          "stroke_opacity":0.5,
          "dashed_ratio": 0.6
        },
        stroke_width=4
      )

      dot = Dot(line.get_start(), z_index=10, color=color)

      line.add(dot)

      if(text):
        text = MathTex(text, font_size=45, color=color)
        text.next_to(
          dot,
          DOWN,
          buff=0.6
        )
        line.add(text)

      return line


    # Add elements to Scene
    self.play(
      FadeIn(axis),
      FadeIn(plane),
      FadeIn(origin)
    )

    self.play(Create(FX), run_time=2)
    self.play(Create(fxTex))

    self.wait(1)

    self.play(
      FadeIn(pointX1),
      Create(getLineToAxisX(pointX1, pointX1.get_color(), 'a')),
      Create(FX2),
      FadeIn(pointX2),
      Create(getLineToAxisX(pointX2, pointX1.get_color(), 'b')),
    )

    dashedFX = DashedVMobject(FX.copy().set_opacity(0.5),
      num_dashes=200,
      equal_lengths=True,
    )

    self.play(
      FadeOut(FX),
      FadeIn(dashedFX),
    )

    self.wait(1)

    self.play(Create(line))

    self.wait(1)

    self.play(
        FadeIn(pointR1),
        Create(getLineToAxisX(pointR1, pointR1.get_color(), 'c')),
    )

    self.play(
      Create(lineR1),
    )

    self.wait(6)

    self.play(FadeOut(dashedFX))

    self.wait(6)

    self.play(FadeOut(fxTex))

    self.wait(6)

    self.play(
      FadeIn(dashedFX),
    )

    self.wait(6) 