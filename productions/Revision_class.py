import numpy as np
from manim import *
from GlyphMapDemo import *
from fixed_fixing import *

class revision1(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES,theta=-120*DEGREES)
        axes=ThreeDAxes(x_range=[-3,3],
                        y_range=[-5,8],
                        z_range=[-2,6],z_length=5,
                        ).add_coordinates()
        axes.get_axis_labels(x_label="x",
                             y_label="y",
                             z_label="z")
        axes.to_edge(DOWN)

        def func1( x, y):
            return np.array([x,y, y- x**2 + 4])


        surf1=Surface(lambda u,v:axes.c2p(*func1(u,v)),
                      u_range=[-2.5,2.5],v_range=[-4,7],
                      checkerboard_colors=[GREEN,YELLOW],fill_opacity=0.8)
        self.add(axes)


        self.play(Create(surf1))
        self.wait()

        def func2(x, y):
            return np.array([x, y, (y - x ** 2 + 4)/2])

        surf2 = Surface(lambda u, v: axes.c2p(*func2(u, v)),
                        u_range=[-2.5, 2.5], v_range=[-4, 7],
                        checkerboard_colors=[BLUE_D,BLUE_B], fill_opacity=0.5)
        self.play(Write(surf2))
        self.wait()

from fixed_fixing import *
class revision2(ThreeDScene):
    def construct(self):
        w1=Tex("Evaluate $I=\int_{-\infty}^{\infty}e^{-x^2}dx.$")
        self.play(Write(w1))
        self.wait()
        self.play(w1.animate.to_edge(UL),lag_ratio=0.2,run_time=2)
        self.wait()


        w2=Tex(r"The integral is difficult to evaluate on its own, \\"
               "so we consider $I^2$ instead.",tex_environment="{minipage}{8cm}").next_to(w1,DOWN).to_edge(LEFT)
        def Rect_fade_in(tex,time):
            self.add(tex)

            rect1 = SurroundingRectangle(tex, fill_opacity=1, color=BLACK, stroke_width=0)

            self.add(rect1)
            self.play(rect1.animate.stretch_to_fit_width(0, about_point=rect1.get_right()), lag_ratio=0.2,
                      run_time=time)

        Rect_fade_in(w2,1.5)
        self.wait(2)

        w3=MathTex(r"I^2=\bigg(\int_{-\infty}^{\infty}e^{-x^2}dx\bigg)\bigg( \int_{-\infty}^{\infty}e^{-y^2}dy\bigg)",
                   font_size=35)
        w3.shift(LEFT*2.5)
        self.play(Write(w3[0][0:3]))
        self.wait()
        self.play(DrawBorderThenFill(w3[0][3:15]),
                  DrawBorderThenFill(w3[0][15:]))
        self.wait()

        w4=MathTex(r"=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}e^{-(x^2+y^2)}dxdy",
                   font_size=35).next_to(w3,RIGHT)
        self.play(TransformByGlyphMap(w3,w4,([4,5,6,7],[1,2,3,4]),
                                      ([8],[9]),([9,10,11],[10,12,13]),
                                      ([12,13],[18,19]),([16,17,18,19],[5,6,7,8]),
                                      ([21,22,23],[14,15,16]),([24,25],[20,21]),
                                      ([0, 1, 2, 3, 14, 15, 20, 26],[]),([],[0,11,17]),
                                      from_copy=True))
        self.wait()

        w5=MathTex("I^2=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}e^{-(x^2+y^2)}dxdy",font_size=35)
        self.play(TransformMatchingShapes(VGroup(w3,w4),w5))
        self.wait(2)
        self.play(VGroup(w1,w2,w5).animate.shift(UP*3.2))
        self.play(w5.animate.to_edge(LEFT))
        self.wait()
        w6=Tex(r"Consider the change of coordinates by setting \\"
               r"$x=rcos\theta,y=rsin\theta$.",font_size=35,
               tex_environment="{minipage}{8cm}").next_to(w5,DOWN).to_edge(LEFT)
        Rect_fade_in(w6,1.5)
        self.wait()
        w7=Tex("This yields",font_size=35).next_to(w6,DOWN).to_edge(LEFT)
        self.play(Write(w7))
        self.wait()

        w8=MathTex(r"I^2&=\int_0^{2\pi}\int_0^{\infty}e^{-r^2}rdrd\theta")
        self.play(TransformByGlyphMap(w5,w8,([0,1,2,3,4,5,6],[0,1,2,3,4,5,6]),
                                      ([7,8,9,10],[7,8,9]),([11,12,13,14,15,16,17,18,19],[10,11,12,13,14]),
                                      ([20,21,22,23],[15,16,17,18]),from_copy=True))
        self.wait()
        w9=MathTex(r"I^2=2\pi \int_0^{\infty}e^{-r^2}rdr")
        self.play(TransformByGlyphMap(w8,w9,([0,1,2],[0,1,2]),
                                      ([3,4,5,6,17,18],[3,4]),
                                      ([7,8,9,10,11,12,13,14,15,16],[5,6,7,8,9,10,11,12,13,14])))
        self.wait()
        w10=MathTex(r"I^2=2\pi \frac{-e^{-r^2}}{2}\bigg \rvert_{0}^{\infty}").shift(LEFT*1)
        self.play(TransformByGlyphMap(w9,w10,([0,1,2,3,4],[0,1,2,3,4]),
                                      ([5],[12,13,14,15]),([6],[16]),([7],[17]),
                                      ([8,9,10,11],[6,7,8,9])))
        self.wait()

        text = MathTex("=\pi").set_opacity(0)
        sq = SurroundingRectangle(text, buff=0.1)
        text.next_to(sq, LEFT, buff=0)
        VGroup(sq,text).next_to(w10,RIGHT,buff=-0.7)
        fade_in_text = always_redraw(lambda:
                                     Intersection(
                                         Union(*text.family_members_with_points()), sq).set_fill(WHITE, 1).set_stroke(
                                         width=0))
        self.add(fade_in_text)
        self.wait()
        self.play(text.animate.shift(RIGHT * text.width), run_time=1)
        self.wait()

        w11=Tex(r"Finally, we have $I=\sqrt{\pi}$.",font_size=35).to_edge(LEFT).shift(DOWN*1.5)
        self.play(Write(w11))
        self.wait(4)

        self.play(
            *[FadeOut(mob,shift=UP*6) for mob in self.mobjects])








        self.set_camera_orientation(phi=90*DEGREES,theta=-90*DEGREES)
        axes=ThreeDAxes(z_range=[-1.5,2])
        graph=axes.plot_parametric_curve(lambda t:np.array([t,0,np.exp(-t**2)]),t_range=[-4,4])
        labels = axes.get_axis_labels(x_label="x", y_label="y",
                                      z_label="z")
        self.play(FadeIn(axes,shift=np.array([0,0,1])))


        self.play(Write(graph,run_time=2))
        self.wait()

        t1=Tex("$f(x)=e^{-x^2}$").to_corner(UL)
        t2=Tex("$z=f(x,y)=e^{-x^2-y^2}$").to_corner(UL)
        self.add_fixed_in_frame_mobjects(t1)



        self.play(Write(t1))
        self.wait()
        self.move_camera(phi=75 * DEGREES, theta=-30 * DEGREES)
        self.wait()
        self.move_camera(zoom=1.5)



        k=ValueTracker(0)
        op=ValueTracker(1)
        self.add(k)
        surf1=always_redraw(lambda :Surface(lambda u,v:axes.c2p(v*np.cos(u),v*np.sin(u),np.exp(-v**2)),resolution=8,
                                            u_range=[0,k.get_value()],v_range=[0,4],checkerboard_colors=[BLUE_D,BLUE_B]).set_opacity(op.get_value()))
        surf2 = always_redraw(lambda: Surface(lambda u, v: axes.c2p(v * np.cos(u), v * np.sin(u), np.exp(-v ** 2)),
                                              u_range=[PI, PI+k.get_value()], v_range=[0, 4],resolution=8,
                                              checkerboard_colors=[BLUE_D, BLUE_B]).set_opacity(op.get_value()))
        surf1.set_z_index(graph.z_index-0.001)
        surf2.set_z_index(graph.z_index - 0.001)
        self.add(surf1)
        self.add(surf2)
        self.play(k.animate.set_value(PI),
                  Rotating(graph,axis=np.array([0,0,1]),radians=PI,about_point=axes.c2p(0,0,0)),
                  rate_func=linear,run_time=4)



        self.play(FadeOut(t1,shift=np.array([-1,0,0])))
        self.add_fixed_in_frame_mobjects(t2)
        self.play(FadeIn(t2,shift=np.array([0,0,-1]),lag_ratio=0.2,
                         run_time=2))
        self.wait()

        self.play(op.animate.set_value(0.6))

        self.wait()


        h = ValueTracker(0)


        for i in (0.25,0.5,0.6, 0.7,0.8, 1, 1.2, 1.3,1.5,1.7,1.8,2):
            cylinder = always_redraw(
                lambda i=i: Surface(
                    lambda u, v: axes.c2p(i * np.cos(u), i * np.sin(u), np.exp(-i ** 2) - v * np.exp(1 - i ** 2)),
                    u_range=[0, 2 * PI], v_range=[0, h.get_value()], resolution=8,
                    checkerboard_colors=[BLUE_D, BLUE_B],stroke_opacity=0,
                    fill_opacity=0.8))
            self.add(cylinder)

        self.play(h.animate.set_value(np.exp(-1)), run_time=2)
        self.wait()



class revision3(Scene):
    def construct(self):
        t1=Tex(r'''Let $D$ be the bounded region in $\mathbb{R}^2$ bounded by the circles 
        $x^2+y^2=2x,x^2+y^2=4x,x^2+y^2=2y$ and $x^2+y^2=6y$. 
        Compute $\iint_{D}\frac{1}{(x^2+y^2)^2}dA.$\\(Note that there is exactly one region whose boundary 
        is composed of 4 pieces, where each piece belongs to one of the circles.)''',
               tex_environment="{minipage}{8cm}")
        self.add(t1)
        rect = SurroundingRectangle(t1,fill_opacity=1,color=BLUE,stroke_width=0)

        self.add(rect)
        self.wait()
        self.play(rect.animate.stretch_to_fit_width(0, about_point=rect.get_right()), lag_ratio=0.2,
                  run_time=1.5)
        self.wait(4)

        self.play(FadeOut(t1,shift=UP*5))
        self.wait()

        t2=Tex(r"Let $u=\frac{x}{x^2+y^2}$ and $v=\frac{y}{x^2+y^2}$.")
        t3=Tex(r"Then the Jacobian is")
        VG1=VGroup(t2,t3).arrange(DOWN,buff=0.3,aligned_edge=LEFT,
                                  center=False)
        VG1.to_edge(LEFT,buff=0.2).shift(UP*3)
        self.play(FadeIn(t2,shift=DOWN*0.5))
        self.wait()
        self.play(Write(t3))
        self.wait()

        t4=MathTex(r'''\frac{\partial(u,v)}{\partial (x,y)}=\begin{vmatrix}
		u_x & u_y\\
		v_x & v_y
	\end{vmatrix}''').shift(LEFT*4.5)
        self.add(t4)

        rect1 = SurroundingRectangle(t4, fill_opacity=1, color=BLACK, stroke_width=0)

        self.add(rect1)
        self.play(rect1.animate.stretch_to_fit_width(0, about_point=rect1.get_right()), lag_ratio=0.2,
                  run_time=1)
        self.wait()

        t5=MathTex(r'''=\begin{vmatrix}
		\frac{y^2-x^2}{(x^2+y^2)^2}& \frac{-2xy}{(x^2+y^2)^2}\\
		\frac{-2xy}{(x^2+y^2)^2}& \frac{x^2-y^2}{(x^2+y^2)^2}
	\end{vmatrix}''').next_to(t4,RIGHT)

        self.play(TransformByGlyphMap(t4,t5,([14,15,16,17],[1,2,3,4,5]),
                                      ([18,19],[6,7,8,9,10,11,12,13,14,15,16,17,18,19]),
                                      ([20,21],[20,21,22,23,24,25,26,27,28,29,30,31,32]),
                                      ([22,23],[33,34,35,36,37,38,39,40,41,42,43,44,45]),
                                      ([24,25],[46,47,48,49,50,51,52,53,54,55,56,57,58,59]),
                                      ([26,27,28,29],[60,61,62,63,64]),
                                      ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], []
                                       ),([],[0]),from_copy=True))
        self.wait()

        t6=MathTex(r"=-\frac{1}{(x^2+y^2)^2}").next_to(t5,RIGHT)
        self.play(Write(t6))
        self.wait()
        t7=Tex(r"So the absolute value of Jacobian is $\frac{1}{(x^2+y^2)^2}$.").to_edge(LEFT,buff=0.2)
        t7.shift(DOWN*2)
        self.play(FadeIn(t7,shift=UP*0.5,lag_ratio=0.3,run_time=2))
        self.wait(4)

        rect2 = Rectangle(color=RED, fill_color=BLACK, width=1e-4,height=50,
                         fill_opacity=1, stroke_width=0).to_edge(LEFT,buff=-1)

        self.add(rect2)
        self.play(rect2.animate.stretch_to_fit_width(20, about_point=rect2.get_left()), lag_ratio=0.3,
                  run_time=2)
        self.wait()

        t8=Tex(r"The boundaries can be rewritten as").to_edge(UL)
        self.play(Write(t8))
        self.wait()
        t9=MathTex(r"u=\frac{1}{2},u=\frac{1}{4},v=\frac{1}{2},v=\frac{1}{6}")
        t9.shift(UP*2)
        self.play(FadeIn(t9,shift=UP*0.5))
        self.wait()
        t10=Tex(r"Therefore, the new region is $R=[\frac{1}{4} , \frac{1}{2}]\times [\frac{1}{6},\frac{1}{2}]$.")
        t10.next_to(t9,DOWN).to_edge(LEFT)
        t10.set_opacity(0)
        sq = SurroundingRectangle(t10, buff=0.1)
        t10.next_to(sq, LEFT, buff=0)
        fade_in_text = always_redraw(lambda:
                                     Intersection(
                                         Union(*t10.family_members_with_points()), sq).set_fill(WHITE, 1).set_stroke(
                                         width=0))
        self.add(fade_in_text)
        self.wait()
        self.play(t10.animate.shift(RIGHT * t10.width), run_time=1.5)
        self.wait()
        t11=Tex(r"This yields").next_to(t10,DOWN).to_edge(LEFT)
        self.play(Write(t11))
        self.wait()
        t12=MathTex(r'''\iint_D\frac{1}{(x^2+y^2)^2}dxdy=\iint_R1dudv=(\frac{1}{2}-\frac{1}{4})
        (\frac{1}{2}-\frac{1}{6})=\frac{1}{12}''').shift(DOWN*1)
        self.play(DrawBorderThenFill(t12))
        self.wait()




        self.play(Circumscribe(t12[0][2]),
                  Circumscribe(t12[0][20]))
        self.play(Circumscribe(t12[0][3:13],color=BLUE),
                  Circumscribe(t12[0][21],color=BLUE))
        self.play(Circumscribe(t12[0][13:17],color=RED),
                  Circumscribe(t12[0][22:26],color=RED))
        self.wait(3)










        MathTex.set_default(font_size=30)
        plane1 = NumberPlane(x_range=[-7, 7],
                             y_range=[-5, 7]
                             )
        self.play(FadeOut(VGroup(t8,t9,fade_in_text,t11,t12),shift=UP*6),
                  FadeIn(plane1,shift=UP))
        self.wait()

        circ1 = plane1.plot_implicit_curve(lambda x, y: x ** 2 + y ** 2 - 2 * x, color=PURPLE)
        circ2 = plane1.plot_implicit_curve(lambda x, y: x ** 2 + y ** 2 - 4 * x, color=RED)
        circ3 = plane1.plot_implicit_curve(lambda x, y: x ** 2 + y ** 2 - 2 * y, color=PURE_GREEN)
        circ4 = plane1.plot_implicit_curve(lambda x, y: x ** 2 + y ** 2 - 6 * y, color=YELLOW)
        lab1 = MathTex("x^2+y^2=2x", color=PURPLE).next_to(circ1)
        lab2 = MathTex("x^2+y^2=4x", color=RED).next_to(circ2, DOWN)
        lab3 = MathTex("x^2+y^2=2y", color=PURE_GREEN).next_to(circ3, LEFT)
        lab4 = MathTex("x^2+y^2=6y", color=YELLOW).next_to(circ4)

        self.play(Write(circ1))
        self.play(Write(lab1))
        self.play(Write(circ2))
        self.play(Write(lab2))
        self.play(Write(circ3))
        self.play(Write(lab3))
        self.play(Write(circ4))
        self.play(Write(lab4))
        self.wait()

        circ_1 = Circle(radius=1).move_to(plane1.c2p(1, 0))
        circ_2 = Circle(radius=2).move_to(plane1.c2p(2, 0))
        circ_3 = Circle(radius=1).move_to(plane1.c2p(0, 1))
        circ_4 = Circle(radius=3).move_to(plane1.c2p(0, 3))
        area = Difference(Intersection(circ_2, circ_4), Union(circ_1, circ_3)
                          , fill_color=BLUE, fill_opacity=0.8)
        self.play(FadeIn(area, lag_ratio=0.2, run_time=2))

        self.wait()
        VG1 = VGroup(plane1,
                     circ_1, circ_3, circ_4, circ_2, circ1, circ4, circ2, circ3,
                     area)
        self.play(FadeOut(VGroup(lab1, lab2, lab3, lab4)),
                  VG1.animate.scale(0.4).to_edge(LEFT))
        self.wait()

        plane2 = Axes(x_range=[0, 1.5, 0.5], y_range=[0, 1, 0.5], y_length=6,
                      x_length=6).to_edge(RIGHT)
        labs = plane2.get_axis_labels(x_label="u", y_label="v")

        self.play(Write(plane2),
                  FadeIn(labs, shift=DOWN * 0.5, lag_ratio=0.2))
        self.wait()
        l1 = DashedLine(start=plane2.c2p(1 / 4, 0),
                        end=plane2.c2p(1 / 4, 1), color=GREEN)
        l2 = DashedLine(start=plane2.c2p(1 / 2, 0),
                        end=plane2.c2p(1 / 2, 1), color=GREEN)
        l3 = DashedLine(start=plane2.c2p(0, 1 / 6),
                        end=plane2.c2p(1.5, 1 / 6), color=YELLOW)
        l4 = DashedLine(start=plane2.c2p(0, 0.5),
                        end=plane2.c2p(1.5, 0.5), color=YELLOW)
        t1 = MathTex(r"\frac{1}{4}").move_to(plane2.c2p(1 / 4, 0)).shift(DOWN * 0.5)
        t2 = MathTex(r"\frac{1}{2}").move_to(plane2.c2p(1 / 2, 0)).shift(DOWN * 0.5)
        t3 = MathTex(r"\frac{1}{6}").move_to(plane2.c2p(0, 1 / 6)).shift(LEFT * 0.5)
        t4 = MathTex(r"\frac{1}{2}").move_to(plane2.c2p(0, 0.5)).shift(LEFT * 0.5)

        self.play(Write(l1))
        self.play(FadeIn(t1, shift=DOWN * 0.5, lag_ratio=0.2))
        self.play(Write(l2))
        self.play(FadeIn(t2, shift=DOWN * 0.5, lag_ratio=0.2))
        self.play(Write(l3))
        self.play(FadeIn(t3, shift=RIGHT * 0.5, lag_ratio=0.15))
        self.play(Write(l4))
        self.play(FadeIn(t4, shift=RIGHT * 0.5, lag_ratio=0.15))
        self.wait()

        Rect = Polygon(plane2.c2p(1 / 4, 1 / 6),
                       plane2.c2p(1 / 4, 1 / 2),
                       plane2.c2p(1 / 2, 1 / 2),
                       plane2.c2p(1 / 2, 1 / 6), fill_color=YELLOW, stroke_color=YELLOW,
                       fill_opacity=0.6)

        self.play(ShowPassingFlash(Rect, run_time=1.5))
        self.play(ReplacementTransform(area.copy(), Rect))

        d1 = Dot(radius=1e-4).move_to(area.get_center()).shift(LEFT * 0.1)
        d2 = Dot(radius=1e-4).move_to(Rect.get_center())
        d3 = Dot(radius=1e-4).move_to(area.get_center())
        d4 = Dot(radius=1e-4).move_to(Rect.get_center()).shift(UP * 0.2)
        A1 = CurvedArrow(start_point=d1.get_center(), end_point=d2.get_center())
        A1.set_color_by_gradient([BLUE, YELLOW])
        A2 = CurvedArrow(start_point=d4.get_center(), end_point=d3.get_center())
        A2.set_color_by_gradient([YELLOW, BLUE])
        self.play(Write(A1))
        self.play(Write(A2))
        self.wait()

























