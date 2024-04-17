# High quality
# %%manim -qh -v WARNING MainScene

# Low quality
%%manim -ql -v WARNING MainScene


# Imports
# from manim import *
# import math
# import getAxis

config.background_color = "#000000"
config.frame_width = 16
config.frame_height = 16

config.pixel_width = 960
config.pixel_height = 960

init_angle = 60

EQ_1 = [
  MathTex(r'\sin(180^{\circ} + \alpha) = -\sin(\alpha)', font_size = 40, color = WHITE),
  MathTex(r'\cos(180^{\circ} + \alpha) = -\cos(\alpha)', font_size = 40, color = WHITE),
  MathTex(r'\tan(180^{\circ} + \alpha) = \tan(\alpha)', font_size = 40, color = WHITE),
]

EQ_2 = [
  MathTex(r'\sin(180^{\circ} - \alpha) = \sin(\alpha)', font_size = 40, color = WHITE),
  MathTex(r'\cos(180^{\circ} - \alpha) = -\cos(\alpha)', font_size = 40, color = WHITE),
  MathTex(r'\tan(180^{\circ} - \alpha) = -\tan(\alpha)', font_size = 40, color = WHITE),
]

class MainScene(Scene):

  def construct(self):

    #<- Axis, Plane and Origin
    axisAlfa = getAxis()
    axisBeta = getAxis()

    axisAlfa.move_to([-4, 0, 0])
    axisBeta.next_to(axisAlfa, RIGHT, buff=0)

    circleAlfa = Circle(
      arc_center = axisAlfa.get_origin(),
      radius = 1 * axisAlfa.get_x_unit_size(),
      color = WHITE
    )

    circleBeta = Circle(
      arc_center = axisBeta.get_origin(),
      radius = 1 * axisBeta.get_x_unit_size(),
      color = WHITE
    )

    # Angle
    alfa = ValueTracker(init_angle)

    def getLines(angle, axis, sin_color = WHITE, cos_color = WHITE, angle_color = WHITE,  text = ''):

      group = VGroup()

      group.point_1 = Dot(
        point = axis.c2p(math.cos(angle * DEGREES), math.sin(angle * DEGREES)),
        color = BLUE,
        z_index = 10
      )

      group.point_2 = Dot(
        point = axis.c2p(math.cos(angle * DEGREES), 0),
        color = BLUE,
        z_index = 10
      )

      group.line = Line(
        start = axis.get_origin(),
        end = group.point_1.get_center(),
        color = WHITE,
        stroke_width = 5,
        z_index = 5
      )

      group.cos_line = Line(
        start = axis.get_origin(),
        end = group.point_2.get_center(),
        color = cos_color,
        stroke_width = 5,
        z_index = 5
      )

      group.sin_line = Line(
        start = group.point_2.get_center(),
        end = group.point_1.get_center(),
        color = sin_color,
        stroke_width = 5,
        z_index = 5
      )

      group.angle_arc = Arc(
        arc_center = axis.get_origin(),
        start_angle = 0,
        angle = (angle % 360) * DEGREES,
        radius = 0.6,
        color = angle_color
      )
      group.angle_bg = AnnularSector(
        arc_center = axis.get_origin(),
        start_angle = 0,
        angle = (angle % 360) * DEGREES,
        inner_radius = 0,
        outer_radius = 0.6,
        fill_opacity = 0.5,
        color = angle_color
      )

      group.angle_text = MathTex(text, font_size=40, color=WHITE, z_index = 12)

      group.angle_text.next_to(axis.get_origin() + [0.7, 0.3, 0], UR, buff = 0)

      group.add(
        group.line,
        group.point_1,
        group.sin_line,
        group.point_2,
        group.cos_line,
        group.angle_arc,
        group.angle_bg,
        group.angle_text
      )

      return group

    AlfaLines = always_redraw(
      lambda: getLines(
        angle = alfa.get_value(),
        axis = axisAlfa,
        text = r'\alpha',
        sin_color = YELLOW,
        cos_color = RED,
        angle_color = GREEN
      )
    )

    BetaLines = always_redraw(
      lambda: getLines(
        angle = (alfa.get_value() + 180),
        axis = axisBeta,
        text = r'180^{\circ} + \alpha',
        sin_color = YELLOW,
        cos_color = RED,
        angle_color = PURPLE
      )
    )


    # Add elements to Scene
    self.play(
      FadeIn(axisAlfa),
      FadeIn(axisBeta)
    )

    self.play(
      Create(circleAlfa),
      Create(circleBeta),
    )
    
    self.play(
      Create(AlfaLines),
      Create(BetaLines)
    )

    for index, text in enumerate(EQ_1):
      text.move_to([0, -2 - 1 * index, 0])
      self.play(Create(text))

    self.wait(1)

    self.play(
      alfa.animate.set_value(360 + init_angle),
      run_time = 12,
      rate_func = rate_functions.linear
    )

    self.wait(1)

    # Clear previous
    self.play(FadeOut(BetaLines))
    self.remove(BetaLines)

    for index, text in enumerate(EQ_1):
      self.play(FadeOut(text), run_time=0.5)

    self.wait(1)

    # 180 -  alfa
    BetaLines = always_redraw(
      lambda: getLines(
        angle = 180 - alfa.get_value(),
        axis = axisBeta,
        text = r'180^{\circ} - \alpha',
        sin_color = YELLOW,
        cos_color = RED,
        angle_color = PURPLE
      )
    )
    self.play(Create(BetaLines))

    for index, text in enumerate(EQ_2):
      text.move_to([0, -2 - 1 * index, 0])
      self.play(Create(text))

    self.wait(2)
    alfa.set_value(init_angle)

    self.play(
      alfa.animate.set_value(360 + init_angle),
      run_time = 12,
      rate_func = rate_functions.linear
    )

    self.wait(1)

    for index, text in enumerate(EQ_2):
      self.play(FadeOut(text), run_time=0.5)

    self.wait(1)



# MARK: Axis
def getAxis():

  # Axis and Plane config
  x_range = [-1.5, 1.5, 1]
  y_range = [-3.4, 2.6, 1]
  x_length = 8
  y_length = 16

  axis = Axes(x_range, y_range, x_length, y_length,
      tips=False,
      axis_config={
        "include_numbers": False,
        "font_size": 25
      },
    )

  plane = NumberPlane(x_range, y_range, x_length, y_length,
    background_line_style={
      "stroke_color": GRAY,
      "stroke_width": 1,
      "stroke_opacity": 0.6
    }
  )

  origin = Dot(
    point=axis.c2p(0, 0),
    color=BLUE,
    radius=0.1,
    z_index=10
  )

  axis.add(plane, origin)

  return axis
