import select

from manim import *
from manim import Tex


class Venn(Scene):
    def construct(self):
        circC = Circle(radius=1.5, fill_color=BLUE, fill_opacity=0.5, stroke_color=WHITE).shift(RIGHT * 1 + DOWN * 1.5)
        circB = Circle(radius=1.5, fill_color=RED, fill_opacity=0.5, stroke_color=WHITE).shift(LEFT * 1 + DOWN * 1.5)
        circA = Circle(radius=1.5, fill_color=GREEN, fill_opacity=0.5, stroke_color=WHITE).shift(
            UP * (3 ** 0.5) + DOWN * 1.5)
        rect1 = Rectangle(width=8, height=5.3).shift(DOWN * 0.6)
        t1 = Tex("Below is the Venn diagram for 3, you can observe that it is consist of 8 parts.").shift(
            UP * 3).scale(0.8)
        self.play(Write(t1), run_time=2)
        self.play(Create(rect1))
        self.wait()
        self.play(DrawBorderThenFill(circA))
        self.play(DrawBorderThenFill(circB))
        self.play(DrawBorderThenFill(circC))
        AeCeB = Difference(Difference(circA, circB), circC)
        lab1 = Tex("1").move_to(AeCeB.get_center())
        AiBeC = Difference(Intersection(circA, circB), circC)
        lab2 = Tex("2").move_to(AiBeC.get_center())
        AiBiC = Intersection(circA, circB, circC)
        lab3 = Tex("3").move_to(AiBiC.get_center())
        AiCeB = Difference(Intersection(circA, circC), circB)
        lab4 = Tex("4").move_to(AiCeB.get_center())
        AeBeC = Difference(circB, Union(circA, circC))
        lab5 = Tex("5").move_to(AeBeC.get_center())
        BiCeA = Difference(Intersection(circC, circB), circA)
        lab6 = Tex("6").move_to(BiCeA.get_center())
        CeBeA = Difference(circC, Union(circA, circB))
        lab7 = Tex("7").move_to(CeBeA.get_center())
        lab8 = Tex("8").move_to(rect1.get_corner(UP + RIGHT)).shift(DOWN * 0.5 + LEFT * 0.5)
        VG1 = VGroup(rect1, circB, circC, circA, lab8, lab7, lab6,
                     lab5, lab4, lab3, lab2, lab1)
        self.play(Write(lab1))
        self.play(Write(lab2))
        self.play(Write(lab3))
        self.play(Write(lab4))
        self.play(Write(lab5))
        self.play(Write(lab6))
        self.play(Write(lab7))
        self.play(Write(lab8))
        self.wait(2)
        self.play(FadeOut(VG1, scale=0.5), Unwrite(t1))

        circ1 = Circle(radius=1.5, fill_color=BLUE, fill_opacity=0.5, stroke_color=WHITE).shift(UP * 1)
        circ2 = Circle(radius=1.5, fill_color=RED, fill_opacity=0.5, stroke_color=WHITE).shift(LEFT * 1)
        circ3 = Circle(radius=1.5, fill_color=YELLOW, fill_opacity=0.5, stroke_color=WHITE).shift(RIGHT * 1)
        circ4 = Circle(radius=1.5, fill_color=GREEN, fill_opacity=0.5, stroke_color=WHITE).shift(DOWN * 1)
        rect2 = Rectangle(width=8, height=5.3)

        T1 = Tex("A").next_to(circ1.get_top(), DOWN)
        T2 = Tex("B").next_to(circ2.get_left(), RIGHT)
        T3 = Tex("C").next_to(circ3.get_right(), LEFT)
        T4 = Tex("D").next_to(circ4.get_bottom(), UP)
        VG2 = VGroup(circ4, circ3, circ2, circ1, rect2, T1, T2, T3, T4)
        self.play(Create(rect2))
        self.play(DrawBorderThenFill(circ1))
        self.play(Write(T1))
        self.play(DrawBorderThenFill(circ2))
        self.play(Write(T2))
        self.play(DrawBorderThenFill(circ3))
        self.play(Write(T3))
        self.play(DrawBorderThenFill(circ4))
        self.play(Write(T4))
        self.wait()
        self.play(VG2.animate.shift(DOWN * 0.7))

        t2 = Tex("Now this is a Venn diagram for 4. Does it contain 16 parts?").shift(UP * 3.2).scale(0.8)
        t3 = Tex("Though symmetry is beautiful, the answer is no.").next_to(t2, DOWN).scale(0.8)
        t4 = Tex("Which part is missing?").shift(UP * 3)
        table0 = Table(
            [["T", "T", "T", "T"],
             ["T", "T", "T", "F"],
             ["T", "T", "F", "T"],
             ["T", "T", "F", "F"],
             ["T", "F", "T", "T"],
             ["T", "F", "T", "F"],
             ["T", "F", "F", "T"],
             ["T", "F", "F", "F"],
             ["F", "T", "T", "T"],
             ["F", "T", "T", "F"],
             ["F", "T", "F", "T"],
             ["F", "T", "F", "F"],
             ["F", "F", "T", "T"],
             ["F", "F", "T", "F"],
             ["F", "F", "F", "T"],
             ["F", "F", "F", "F"]],
            col_labels=[Text("A", color=YELLOW), Text("B", color=YELLOW), Tex("C", color=YELLOW),
                        Tex("D", color=YELLOW)],
            v_buff=0.2, include_outer_lines=True, stroke_width=0.2, line_config={"stroke_width": 1, "color": WHITE}
        ).to_edge(LEFT)

        table0.scale_to_fit_height(6)
        table0.shift(DOWN * 0.5 + LEFT * 1)
        table0.add_highlighted_cell((4, 1), color=BLUE)
        table0.add_highlighted_cell((4, 2), color=BLUE)
        table0.add_highlighted_cell((4, 3), color=BLUE)
        table0.add_highlighted_cell((4, 4), color=BLUE)
        table0.add_highlighted_cell((6, 1), color=BLUE)
        table0.add_highlighted_cell((6, 2), color=BLUE)
        table0.add_highlighted_cell((6, 3), color=BLUE)
        table0.add_highlighted_cell((6, 4), color=BLUE)
        table0.add_highlighted_cell((8, 1), color=BLUE)
        table0.add_highlighted_cell((8, 2), color=BLUE)
        table0.add_highlighted_cell((8, 3), color=BLUE)
        table0.add_highlighted_cell((8, 4), color=BLUE)
        table0.add_highlighted_cell((11, 1), color=BLUE)
        table0.add_highlighted_cell((11, 2), color=BLUE)
        table0.add_highlighted_cell((11, 3), color=BLUE)
        table0.add_highlighted_cell((11, 4), color=BLUE)

        self.play(Write(t2), run_time=2)
        self.wait(2)
        self.play(Write(t3))
        self.wait()
        self.play(ReplacementTransform(VGroup(t2, t3), t4))
        self.wait()
        self.play(VG2.animate.scale(0.8).shift(RIGHT * 1.5))
        self.play(DrawBorderThenFill(table0), run_time=2)
        self.wait()
        self.play(Indicate(table0.get_rows()[3], color=RED),
                  Indicate(table0.get_rows()[5], color=RED),
                  Indicate(table0.get_rows()[7], color=RED),
                  Indicate(table0.get_rows()[10], color=RED))
        self.wait(2)
        self.play(FadeOut(VG2, shift=RIGHT))
        self.play(FadeOut(table0, shift=LEFT))

        t5 = Tex("This is what a valid 4 set Venn diagram looks like:").shift(UP * 3.2)
        self.play(ReplacementTransform(t4, t5))
        self.wait()
        Rect = Rectangle(width=8, height=5.6).shift(DOWN * 1)
        A = Ellipse(width=2.5, height=5, stroke_color=RED).rotate(35 * DEGREES).shift(DOWN * 0.5)
        B = A.copy().shift(DOWN * 1, LEFT * 1).set_stroke(color=BLUE)
        C = Ellipse(width=2.5, height=5, stroke_color=GREEN).rotate(-35 * DEGREES).shift(DOWN * 0.5)
        D = C.copy().shift(DOWN * 1, RIGHT * 1).set_stroke(color=YELLOW)
        tA = Tex("A").next_to(A.get_top(), LEFT, buff=1.8).scale(0.8)
        tB = Tex("B").next_to(B.get_top(), LEFT, buff=1.8).scale(0.8)
        tC = Tex("C").next_to(C.get_top(), RIGHT, buff=1.8).scale(0.8)
        tD = Tex("D").next_to(D.get_top(), RIGHT, buff=1.8).scale(0.8)
        VG3 = VGroup(A, B, C, D, tD, tC, tB, tA, Rect).shift(UP * 0.5)
        self.play(Create(Rect))
        self.play(DrawBorderThenFill(A))
        self.play(Write(tA))
        self.play(DrawBorderThenFill(B))
        self.play(Write(tB))
        self.play(DrawBorderThenFill(C))
        self.play(Write(tC))
        self.play(DrawBorderThenFill(D))
        self.play(Write(tD))

        VG4 = VGroup(A, B, C, D, Rect)
        table = Table([["A", "B", "C", "D"],
                       ["T", "F", "F", "F"],
                       ["F", "F", "T", "F"],
                       ["F", "T", "F", "F"],
                       ["T", "T", "F", "F"],
                       ["T", "F", "T", "F"],
                       ["F", "F", "T", "T"],
                       ["F", "F", "F", "T"],
                       ["F", "T", "T", "F"],
                       ["T", "T", "T", "F"],
                       ["T", "T", "T", "T"],
                       ["T", "F", "T", "T"],
                       ["T", "F", "T", "F"],
                       ["F", "T", "T", "T"],
                       ["T", "T", "F", "T"],
                       ["F", "T", "F", "T"],
                       ["F", "F", "F", "F"]]).to_edge(LEFT)
        table.set(width=7)
        self.play(VG3.animate.scale(0.8).to_edge(RIGHT).shift(UP * 0.2))
        t6 = Tex("Rows of truth table").next_to(VG3, LEFT, buff=1.5).shift(UP * 2)

        self.play(Write(t6))

        row0 = table.get_rows()[0].next_to(VG3, LEFT, buff=1).shift(UP * 1)
        self.play(DrawBorderThenFill(row0))

        def emph(mob, color):
            self.play(
                mob.animate.set_color(color).set_fill(color=color, opacity=1),
                rate_func=rate_functions.smooth,
                run_time=1)

        T1 = Tex(r"$A\setminus (B \cup C \cup D)$").set_color(YELLOW).next_to(t5, DOWN)
        Reg1 = Difference(A, Union(B, C, D))

        T2 = Tex(r"$C\setminus (A \cup B \cup D)$").set_color(YELLOW).next_to(t5, DOWN)
        Reg2 = Difference(C, Union(A, B, D))
        T3 = Tex(r"$B\setminus (A \cup C \cup D)$").set_color(YELLOW).next_to(t5, DOWN)
        Reg3 = Difference(B, Union(A, C, D))

        T4 = Tex(r"$(A\cap B)\setminus (C\cup D)$").set_color(YELLOW).next_to(t5, DOWN)
        Reg4 = Difference(Intersection(A, B), Union(C, D))

        T5 = Tex(r"$(A\cap C)\setminus (B\cup D)$").set_color(YELLOW).next_to(t5, DOWN)
        Reg5 = Difference(Intersection(A, C), Union(B, D))

        T6 = Tex(r"$(C\cap D)\setminus (A\cup B)$").set_color(YELLOW).next_to(t5, DOWN)
        Reg6 = Difference(Intersection(D, C), Union(B, A))

        T7 = Tex(r"$D\setminus (A\cup B \cup C)$").set_color(YELLOW).next_to(t5, DOWN)
        Reg7 = Difference(D, Union(A, B, C))

        T8 = Tex(r"$(B\cap C) \setminus (A\cup D)$").set_color(YELLOW).next_to(t5, DOWN)
        Reg8 = Difference(Intersection(B, C), Union(A, D))

        T9 = Tex(r"$(A\cap B \cap C)\setminus D$").set_color(YELLOW).next_to(t5, DOWN)
        Reg9 = Difference(Intersection(A, B, C), D)

        T10 = Tex(r"$A\cap B\cap C\cap D$").set_color(YELLOW).next_to(t5, DOWN)
        Reg10 = Intersection(A, B, C, D)

        T11 = Tex(r"$(A\cap C \cap D)\setminus B$").set_color(YELLOW).next_to(t5, DOWN)
        Reg11 = Difference(Intersection(A, C, D), B)

        T12 = Tex(r"$(A\cap D) \setminus (B\cup C)$").set_color(YELLOW).next_to(t5, DOWN)
        Reg12 = Difference(Intersection(A, D), Union(B, C))

        T13 = Tex(r"$(B\cap C\cap D)\setminus A$").set_color(YELLOW).next_to(t5, DOWN)
        Reg13 = Difference(Intersection(B, C, D), A)

        T14 = Tex(r"$(A\cap B\cap D)\setminus C$").set_color(YELLOW).next_to(t5, DOWN)
        Reg14 = Difference(Intersection(B, A, D), C)

        T15 = Tex(r"$(B\cap D)\setminus (A\cup C)$").set_color(YELLOW).next_to(t5, DOWN)
        Reg15 = Difference(Intersection(B, D), Union(A, C))

        T16 = Tex(r"$(A\cup B\cup C\cup D)^{c}$").set_color(YELLOW).next_to(t5, DOWN)
        Reg16 = Difference(Rect, Union(A, B, C, D))

        text = ["0111", "1101", "1011", "0011", "0101", "1100", "1110", "1001", "0001", "0000", "0100", "0110", "1000",
                "0010", "1010", "1111"]

        for binary_str in sorted(text, key=lambda x: int(x, 2)):
            i = text.index(binary_str)
            self.play(Write(locals()["T" + str(i + 1)]))
            emph(locals()["Reg" + str(i + 1)], color=color_gradient((YELLOW, BLUE), 2))
            self.play(FadeIn(table.get_rows()[i + 1].set_color(PURE_GREEN).next_to(row0, DOWN, buff=1), shift=UP))

            self.play(Indicate(table.get_rows()[i + 1], color=RED))
            self.wait(2)
            self.play(FadeOut(table.get_rows()[i + 1], shift=UP))
            self.play(FadeOut(locals()["T" + str(i + 1)]), FadeOut(locals()["Reg" + str(i + 1)]))
        self.wait()



