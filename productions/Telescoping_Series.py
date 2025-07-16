import math

from manim import *


class Tele(Scene):
    def construct(self):
        title = Tex("Maths in a minute").scale(1.3)
        subtitle = Tex("A Telescoping Series").next_to(title, DOWN).scale(0.7)
        self.play(DrawBorderThenFill(title), run_time=2)
        self.wait()
        self.play(Write(subtitle))
        self.wait()
        self.play(FadeOut(VGroup(title, subtitle)))
        self.wait()



        t1 = Tex(
            r"\renewcommand\baselinestretch{1.5}\selectfont Recall how we solve $\displaystyle \sum_{n=1}^{"
            r"\infty}\frac{1}{n(n+1)}$:\\",
            r"We take out its partial sum $s_{k}$").to_edge(
            UP, buff=0.2)
        t2 = Tex(r'''\begin{equation*}
	\begin{split}
		\sum_{n=1}^{k}{\frac{1}{n(n+1)}}&=\frac{1}{1\times2}+\frac{1}{2\times3}+\frac{1}{3\times4}+\dots+\frac{1}{(k-1)k}+\frac{1}{k(k+1)}\\
		&=1-\frac{1}{2}+\frac{1}{2}-\frac{1}{3}+\frac{1}{3}-\frac{1}{4}+\dots+\frac{1}{k-1}-\frac{1}{k}+\frac{1}{k}-\frac{1}{k+1}\\
		&=1+0+0+0+0-\frac{1}{k+1}=1-\frac{1}{k+1}
	\end{split}
\end{equation*}''').scale(0.8).next_to(t1, DOWN)
        t3 = Tex(
            r"When $k$ tends to $\infty$, $\frac{1}{k+1}$ will tend to 0. Thus $\displaystyle \sum_{n=1}^{"
            r"\infty}\frac{1}{n(n+1)}=1$").next_to(
            t2, DOWN).scale(0.8).shift(UP * 0.2)

        self.play(Write(t1[0]))
        self.play(Write(t1[1]))
        self.wait()

        self.play(DrawBorderThenFill(t2[0][0:14]))
        self.play(Write(t2[0][14:53], run_time=3))
        self.play(Write(t2[0][53]))
        self.play(TransformMatchingShapes(t2[0][14:19].copy(), t2[0][54:59]))
        self.play(TransformMatchingShapes(t2[0][19].copy(), t2[0][59]))
        self.play(TransformMatchingShapes(t2[0][20:25].copy(), t2[0][60:67]))
        self.play(TransformMatchingShapes(t2[0][25].copy(), t2[0][67]))
        self.play(TransformMatchingShapes(t2[0][26:31].copy(), t2[0][68:75]))
        self.play(TransformMatchingShapes(t2[0][31:36].copy(), t2[0][75:80]))
        self.play(TransformMatchingShapes(t2[0][36:44].copy(), t2[0][80:89]))
        self.play(TransformMatchingShapes(t2[0][44].copy(), t2[0][89]))
        self.play(TransformMatchingShapes(t2[0][45:53].copy(), t2[0][90:99]))
        self.play(Write(t2[0][99]))
        self.play(TransformMatchingShapes(t2[0][54].copy(), t2[0][100]))
        self.play(ReplacementTransform(t2[0][55:63].copy(), t2[0][101:103]))
        self.play(ReplacementTransform(t2[0][63:71].copy(), t2[0][103:105]))
        self.play(ReplacementTransform(t2[0][71:85].copy(), t2[0][105:107]))
        self.play(ReplacementTransform(t2[0][85:93].copy(), t2[0][107:109]))
        self.play(TransformMatchingShapes(t2[0][93:99].copy(), t2[0][109:115]))
        self.play(Write(t2[0][115:]))
        self.wait()

        self.play(Write(t3), run_time=3)
        self.wait()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        t4 = Tex(r"This is a typical proof for computing the limit of telescoping series,\\",
                 "next we are going to introduce a visualized version for this particular series.",
                 tex_environment="{minipage}{12cm}",
                 font_size=40)
        self.play(Write(t4[0]))
        self.wait()
        self.play(Write(t4[1]))
        self.wait()
        self.play(Unwrite(t4))

        plane = Axes(x_range=[0, 1.2],
                     y_range=[0, 1.2],
                     x_length=7,
                     y_length=7).add_coordinates().shift(UP * 0.4)
        dot0 = Dot(radius=0.05).move_to(plane.c2p(0, 0))
        dot1 = Dot(radius=0.05).move_to(plane.c2p(1, 1))
        dot2 = Dot().move_to(plane.c2p(1, 0))
        dot3 = Dot().move_to(plane.c2p(0, 1))
        hline = DashedLine(start=dot1, end=dot2)
        vline = DashedLine(start=dot1, end=dot3)
        self.play(Create(plane))
        self.play(DrawBorderThenFill(VGroup(dot1, dot0)))
        self.play(Create(VGroup(hline, vline)))
        funcs = VGroup()
        lab1 = MathTex("y=x").move_to(plane.c2p(0.5, 0.5)).scale(0.8)
        lab2 = MathTex("y=x^2").move_to(plane.c2p(0.618, 0.382)).scale(0.8).shift(UP * 0.2)
        lab3 = MathTex("y=x^3").move_to(plane.c2p(0.7, 0.3)).scale(0.8).shift(UP * 0.2)
        labn = MathTex("y=x^n").move_to(plane.c2p(0.9, 0.1)).scale(0.8).set_z_index(0.001)
        dots = Tex(r"$\ddots$").move_to(plane.c2p(0.8, 0.2)).scale(1.1).set_z_index(0.001)
        labels = VGroup(lab1, lab2, lab3).set_z_index(0.001)
        for i in range(0, 3):
            func = plane.plot(lambda x: x ** (i + 1), x_range=[0, 1]).set_color(YELLOW)
            funcs.add(func)
            self.play(Create(func))
            self.play(Write(labels[i]))

        funcn = plane.plot(lambda x: x ** 10, x_range=[0, 1]).set_color(YELLOW)

        for i in range(3, 6):
            func = plane.plot(lambda x: x ** (i + 1), x_range=[0, 1]).set_color(YELLOW)
            funcs.add(func)
            self.play(Create(func), run_time=0.5)
        self.play(Write(dots))
        self.play(Create(funcn))
        self.play(Write(labn))
        funcs.add(funcn)

        self.wait()
        VG1 = VGroup(labels, dots, labn)
        VG2 = VGroup(plane, funcs, funcn, dot0, dot2, dot3, dot1, vline, hline, VG1)

        self.play(VG2.animate.shift(LEFT * 2.5))

        def emph(mob, color):
            self.wait()
            self.play(
                mob.animate.set_color(color).set_fill(color=color, opacity=0.8),

                run_time=0.5)
            self.play(mob.animate.scale(1.2), rate_func=there_and_back_with_pause, run_time=1)

        t5 = Tex("The key part lies in the area for highlighted regions:",
                 tex_environment="{minipage}{12cm}", font_size=28).to_edge(RIGHT, buff=0.5).shift(UP * 3)
        self.play(Write(t5))
        self.wait()

        func0 = plane.plot(lambda x: x ** 0)

        Reg0 = plane.get_area(graph=func0, bounded_graph=funcs[0])
        T0 = MathTex(r"\int_0^1{(1-x)dx}").set_color(BLUE).next_to(t5, DOWN).scale(0.7)
        emph(Reg0, BLUE)
        self.play(Write(T0))

        Reg1 = plane.get_area(graph=funcs[0], bounded_graph=funcs[1])
        T1 = MathTex(r"\int_0^1{(x-x^2)dx}").next_to(T0, DOWN).set_color(GREEN).scale(0.7)
        emph(Reg1, GREEN)
        self.play(Write(T1))

        Reg2 = plane.get_area(graph=funcs[1], bounded_graph=funcs[2])
        T2 = MathTex(r"\int_0^1{(x^2-x^3)dx}").next_to(T1, DOWN).set_color(RED).scale(0.7)
        emph(Reg2, RED)
        self.play(Write(T2))

        vdots = MathTex(r"\vdots").next_to(T2, DOWN).scale(0.7).set_color(WHITE)
        T3 = MathTex(r"\int_0^1{(x^{n-1}-x^n)dx}").next_to(vdots, DOWN).set_color(
            color_gradient([BLUE, YELLOW], 1)).scale(0.6)
        vdots1 = vdots.copy().next_to(T3, DOWN).scale(0.7)
        for i in range(2, 6):
            reg = plane.get_area(graph=funcs[i], bounded_graph=funcs[i + 1])
            self.play(reg.animate.set_fill(color=color_gradient([BLUE, YELLOW], 1), opacity=0.8))
        Regn = plane.get_area(graph=funcn, x_range=[0, 1])
        self.play(Regn.animate.set_fill(color=color_gradient([BLUE, YELLOW], 1), opacity=0.8))

        self.play(Write(vdots))
        self.play(Write(T3))
        self.play(Write(vdots1))
        self.wait()

        t6 = Tex("Now we sum up all the areas:", font_size=40).to_edge(RIGHT, buff=1).shift(UP * 3)
        self.play(ReplacementTransform(t5, t6))
        t7 = Tex(r'''\begin{equation*}
	\begin{split}
	\text{Sum of areas}&=\int_0^1{(1-x)dx}+\int_0^1{(x-x^2)dx}\\&+\int_0^1{(x^2-x^3)dx}+\dots+\int_0^1{(x^{n-1}-x^n)dx}+\dots\\
	&=\sum_{n=1}^{\infty}{\int_0^1{(x^{n-1}-x^n) dx}}\\
	&=\sum_{n=1}^{\infty}{\left[\frac{x^n}{n}-\frac{x^{n+1}}{n+1}\right]_{x=0}^{x=1}}\\
	&=\sum_{n=1}^{\infty}{(\frac{1}{n}-\frac{1}{n+1})}\\
	&=\sum_{n=1}^{\infty}{\frac{1}{n(n+1)}}
	\end{split}
\end{equation*}''', font_size=25).next_to(t6, DOWN, buff=1)

        VG3 = VGroup(T0, T1, T2, T3, vdots)

        self.play(FadeOut(VGroup(vdots, vdots1)))

        self.play(TransformMatchingShapes(T0, t7[0][11:21]),
                  TransformMatchingShapes(T1, t7[0][22:33]),
                  TransformMatchingShapes(T2, t7[0][34:46]),
                  TransformMatchingShapes(T3, t7[0][51:65]), run_time=1.5)
        self.play(DrawBorderThenFill(VGroup(t7[0][0:11],
                                            t7[0][21], t7[0][33], t7[0][46:51], t7[0][65:69])))
        self.wait()
        self.play(Write(t7[0][69:89], run_time=2))
        self.wait()
        self.play(Write(t7[0][89:116], run_time=2))
        self.wait()
        self.play(Write(t7[0][116:133], run_time=2))
        self.wait()
        self.play(Write(t7[0][133:]))
        self.wait(2)

        t8 = Tex(r"\begin{equation*}\begin{split}\text{Sum of areas}=\sum_{n=1}^{\infty}{\frac{1}{n(n+1)}}\end{"
                 r"split}\end{equation*}").next_to(t6, DOWN, buff=0.1).scale(0.7)
        self.play(ReplacementTransform(t7, t8))
        t9 = Tex(r"\renewcommand\baselinestretch{1.5}\selectfont When all the areas are added up,\\",
                 r"it would actually be equal to the area\\",
                 r"bounded by $x=1$, $y=1$ and the axes.\\",
                 r"Thus $\displaystyle \sum_{n=1}^{\infty}{\frac{1}{n(n+1)}}=1$", tex_environment="{minipage}{9cm}",
                 font_size=35).next_to(t8, DOWN, buff=1).shift(RIGHT * 0.3)
        self.play(Write(t9[0]))
        self.wait()
        self.play(Write(t9[1]))
        self.play(Write(t9[2]))
        self.wait()
        self.play(Write(t9[3]))
        self.wait()

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        Home = "/Users/liuzhonglin/Desktop/Manim/media/External Images"

        svg = SVGMobject(f"{Home}//HKU.svg").scale(2.5).shift(UP * 0.5)
        svg.set_fill(color=WHITE)

        Word = Tex(r'\textbf{Department of Mathematics}', font_size=50).next_to(svg, DOWN)
        Word2 = Tex("The University of Hong Kong").next_to(Word, DOWN)
        substance = VGroup(svg, Word, Word2)
        self.play(DrawBorderThenFill(svg), run_time=3)
        self.play(DrawBorderThenFill(VGroup(Word, Word2)), run_time=2)
        self.play(substance.animate.scale(0.8).shift(LEFT * 3))

        w1 = Tex("Producer: ", "Joe Lynn (BSc)")
        w2 = Tex("Organisation: ")
        icon = ManimBanner(dark_theme=True).scale(0.2)
        w3 = Tex("Production Team").next_to(icon, RIGHT, buff=0.6)
        vg = VGroup(icon, w3)
        w4 = Tex("Supervisor: ", "Dr. Y.M. Chan")
        self.wait()
        w5 = Tex(r"Should you have any interest in making videos of this form, "
                 "feel free to contact us through", " ymchan@maths.hku.hk", tex_environment="{minipage}{6cm}",
                 font_size=35)
        w5[1].set_color(GREEN)
        contact2 = Tex("or", " u3597461@connect.hku.hk", font_size=35)
        contact2[1].set_color(GREEN)
        VGW = VGroup(w1, w2, vg, w4, w5, contact2).arrange(DOWN, buff=0.3, center=False, aligned_edge=LEFT).to_edge(
            RIGHT)
        contact2.shift(RIGHT * 1.4 + UP * 0.2)
        VGW.shift(UP * 2)
        vg.shift(RIGHT * 0.6)
        self.play(Write(w1[0]))
        self.play(Write(w1[1]))
        self.play(Write(w2))
        self.play(icon.create())
        self.play(icon.expand())
        self.play(Write(w3))
        self.play(Write(w4[0]))
        self.play(Write(w4[1]))
        self.wait()

        self.play(Write(w5[0], run_time=4))
        self.wait()
        self.play(DrawBorderThenFill(w5[1]))
        self.play(DrawBorderThenFill(contact2))
        self.wait()


