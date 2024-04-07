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
x2 = 8
r1 = 6

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
    fxTex = MathTex(r'f(x) = \frac{(x-8)^{2}}{5} + \frac{9}{2}', font_size=37, color=WHITE)
    fxTex.move_to(axis.c2p(10.5, 5) + fxTex.get_critical_point(DR) - fxTex.get_critical_point(ORIGIN))


    gxTex = MathTex(r'g(x) = -\frac{(x-7)^{2}}{4} + 3', font_size=37, color=WHITE)
    gxTex.move_to(axis.c2p(10.5, 3) + gxTex.get_critical_point(DR) - gxTex.get_critical_point(ORIGIN))


    def fx(x):
      return -math.pow(x - 7, 2) / 4 + 3

    def gx(x):
      return math.pow(x - 8, 2) / 5 + 4.5

    FX = axis.plot(fx, color=YELLOW_A)
    acotFX = axis.plot(fx, x_range=[x1, x2], color=YELLOW_A, z_index=5)
    GX = axis.plot(gx, color=PURPLE_E)
    acotGX = axis.plot(gx, x_range=[x1, x2], color=PURPLE_E, z_index=5)

    FX1 = axis.c2p(x1, fx(x1), 0)
    FX2 = axis.c2p(x2, fx(x2), 0)
    GX1 = axis.c2p(x1, gx(x1), 0)
    GX2 = axis.c2p(x2, gx(x2), 0)

    # Recta secante
    line1 = Line(
      start=FX1 + (FX2 - FX1) * -0.5,
      end=FX1 + (FX2 - FX1) * 1.5,
      color=GREEN_D
    )
    line2 = Line(
      start=GX1 + (GX2 - GX1) * -0.5,
      end=GX1 + (GX2 - GX1) * 1.5,
      color=GREEN_D
    )

    # Points
    pointFX1 = Dot(
      point=FX1,
      z_index=10,
      color=RED
    )
    pointFX2 = Dot(
      point=FX2,
      z_index=10,
      color=RED_B
    )
    pointGX1 = Dot(
      point=GX1,
      z_index=10,
      color=RED
    )
    pointGX2 = Dot(
      point=GX2,
      z_index=10,
      color=RED_B
    )

    pointR1 = Dot(
      point=axis.c2p(r1, fx(r1)),
      z_index=10,
      color=TEAL_B
    )
    pointR2 = Dot(
      point=axis.c2p(r1, gx(r1)),
      z_index=10,
      color=TEAL_B
    )

    lineR1 = Line(
      start=FX1 + (FX2 - FX1) * 0.2,
      end=FX1 + (FX2 - FX1) * 1,
      color=BLUE_E
    )
    lineR1.move_to(pointR1.get_center())

    lineR2 = Line(
      start=GX1 + (GX2 - GX1) * 0.2,
      end=GX1 + (GX2 - GX1) * 1,
      color=BLUE_E
    )
    lineR2.move_to(pointR2.get_center())

    def getLineToAxisX(point, color = GRAY_A, text = None, hide_line = False):

      x, y, z = point.get_center()

      line = axis.get_line_from_axis_to_point(
        index=0,
        point=[x, y, z],
        color=color,
        line_config={
          "dash_length": 0.1,
          "stroke_opacity": 0.5 if not hide_line else 0,
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

    self.play(Create(FX), Create(GX), run_time=2)
    self.play(Create(fxTex), Create(gxTex))

    self.wait(1)

    self.play(
      FadeIn(pointFX1),
      Create(getLineToAxisX(pointFX1, pointFX1.get_color(), hide_line=True)),
      FadeIn(pointGX1),
      Create(getLineToAxisX(pointGX1, pointGX1.get_color(), 'a')),
      Create(acotFX),
      Create(acotGX),
      FadeIn(pointFX2),
      Create(getLineToAxisX(pointFX2, pointFX1.get_color(), hide_line=True)),
      FadeIn(pointGX2),
      Create(getLineToAxisX(pointGX2, pointGX1.get_color(), 'b')),
    )

    dashedFX = DashedVMobject(FX.copy().set_opacity(0.5),
      num_dashes=180,
      equal_lengths=True,
    )

    dashedGX = DashedVMobject(GX.copy().set_opacity(0.5),
      num_dashes=180,
      equal_lengths=True,
    )

    self.play(
      FadeOut(FX),
      FadeIn(dashedFX),
      FadeOut(GX),
      FadeIn(dashedGX),
    )

    self.wait(1)

    self.play(Create(line1), Create(line2))

    self.wait(1)

    self.play(
        FadeIn(pointR1),
        Create(getLineToAxisX(pointR1, pointR1.get_color(), hide_line=True)),
        FadeIn(pointR2),
        Create(getLineToAxisX(pointR2, pointR2.get_color(), 'c')),
    )

    self.play(
      Create(lineR1),
      Create(lineR2)
    )

    self.wait(6)

    self.play(FadeOut(dashedFX), FadeOut(dashedGX))

    self.wait(6)

    self.play(FadeOut(fxTex), FadeOut(gxTex))

    self.wait(6)

    self.play(
      FadeIn(dashedFX),
      FadeIn(dashedGX),
    )

    self.wait(6)    