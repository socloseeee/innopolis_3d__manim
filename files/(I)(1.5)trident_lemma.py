from manim import *
import numpy as mp


class Trident_(ThreeDScene):
    def construct(self):
        inscribed_circle = Circle(color=GREY).set_stroke(width=2)
        O = Dot(inscribed_circle.get_center(), color=DARK_BLUE).set_stroke(width=1, color=WHITE)
        O_text = MathTex(r"O", color=BLUE).next_to(O, UP).scale(0.9)

        tangent1 = TangentLine(inscribed_circle, alpha=0.115, length=4.5)
        tangent2 = TangentLine(inscribed_circle, alpha=0.425, length=4.5)
        tangent3 = Line([-2, -1, 0], [2.5, -1, 0], color=WHITE)
        A = Dot(
            line_intersection(
                [tangent1.start, tangent1.end],
                [tangent2.start, tangent2.end]
            ),
            color=DARK_BLUE
        ).set_stroke(width=1, color=WHITE)
        A_text = MathTex(r"A", color=BLUE).next_to(A, UP).scale(0.9)
        B = Dot(
            line_intersection(
                [tangent2.start, tangent2.end],
                [tangent3.start, tangent3.end]
            ),
            color=DARK_BLUE
        ).set_stroke(width=1, color=WHITE)
        B_text = MathTex(r"B", color=BLUE).next_to(B, LEFT).scale(0.9)
        C = Dot(
            line_intersection(
                [tangent3.start, tangent3.end],
                [tangent1.start, tangent1.end]
            ),
            color=DARK_BLUE
        ).set_stroke(width=1, color=WHITE)
        C_text = MathTex(r"C", color=BLUE).next_to(C, RIGHT).scale(0.9)
        BC = Line(B.get_center(), C.get_center(), color=BLUE).set_stroke(width=2)
        ABC = Polygon(A.get_center(), B.get_center(), C.get_center(), color=GREY).set_stroke(width=2)

        circumscribed_circle = Circle.from_three_points(A.get_center(), B.get_center(), C.get_center(), color=GREY).set_stroke(width=2)

        C_ray = Line(
            [C.get_x(), C.get_y(), 0],
            [
                C.get_x() + (C.get_x() - A.get_x())*2,
                C.get_y() + (C.get_y() - A.get_y())*2,
                0
            ],
            color=GREY
        ).set_stroke(width=2)
        B_ray = Line(
            [B.get_x(), B.get_y(), 0],
            [
                B.get_x() + (B.get_x() - A.get_x())*2,
                B.get_y() + (B.get_y() - A.get_y())*2,
                0
            ],
            color=GREY
        ).set_stroke(width=2)

        B_angle = Angle(
            Line(B.get_center(), C.get_center()),
            B_ray,
            other_angle=True
        )
        C_angle = Angle(
            Line(C.get_center(), B.get_center()),
            C_ray
        )

        bisect_b = Line(
            B.get_center(),
            [
                B_angle.get_center()[0] + (B_angle.get_center()[0] - B.get_center()[0]) * 30,
                B_angle.get_center()[1] + (B_angle.get_center()[1] - B.get_center()[1]) * 30,
                0
            ]
        )
        bisect_c = Line(
            C.get_center(),
            [
                C_angle.get_center()[0] + (C_angle.get_center()[0] - C.get_center()[0]) * 30,
                C_angle.get_center()[1] + (C_angle.get_center()[1] - C.get_center()[1]) * 30,
                0
            ]
        )

        excircle_center = Dot(
            line_intersection(
                [bisect_b.start, bisect_b.end],
                [bisect_c.start, bisect_c.end]
            )
        )

        excircle = Circle(radius=-1 - excircle_center.get_y() - 0.69, color=GREY).set_stroke(width=2)
        excircle.set_x(excircle_center.get_x() - 0.15)
        excircle.set_y(excircle_center.get_y() + 0.7)
        P = Dot(excircle.get_center(), color=DARK_BLUE).set_stroke(width=1, color=WHITE)
        P_text = MathTex(r"P", color=BLUE).next_to(P, DOWN).scale(0.9)

        OP = Line(O.get_center(),  P.get_center(), color=GREY).set_stroke(width=2)
        tangent_down_circumscribed = TangentLine(circumscribed_circle, alpha=0.75)

        L = Dot(
            line_intersection(
                [tangent_down_circumscribed.start, tangent_down_circumscribed.end],
                [A.get_center(), P.get_center()]
            ),
            color=GREY
        ).set_stroke(width=1, color=WHITE)
        L_text = MathTex(r"L", color=GREY).next_to(L, 0.1*(DOWN+LEFT)).scale(0.9)

        BL = Line(L.get_center(), B.get_center(), color=GREY).set_stroke(width=2)
        CL = Line(L.get_center(), C.get_center(), color=GREY).set_stroke(width=2)

        BC_arc = ArcBetweenPoints(B.get_center(), C.get_center(), radius=circumscribed_circle.radius, color=BLUE).set_stroke(width=2)

        LO = Line(L.get_center(), O.get_center(), color=GREEN).set_stroke(width=2)
        LP = Line(L.get_center(), P.get_center(), color=GREEN).set_stroke(width=2)

        all_anim = Group(
            inscribed_circle,
            circumscribed_circle,
            excircle,
            ABC, A_text, B_text, C_text, A, B, C, O, P, O_text, P_text, OP,
            C_ray, B_ray,
            L, L_text,
            BL, CL, BC,
            BC_arc,
            LO, LP
        )
        all_anim.shift(UP * 1.7 + LEFT * 0.5).scale(0.9)

        text = MathTex(r"LO", r"=", r"LB", r"=", r"LC", r"=", r"LP").shift(RIGHT*3.3)
        text[0].set_color(GREEN)
        text[2].set_color(GREEN)
        text[4].set_color(GREEN)
        text[6].set_color(GREEN)

        # Анимация
        self.play(FadeIn(O, O_text))
        self.play(Create(inscribed_circle, run_time=2))
        self.play(
            Create(ABC, run_time=2),
            FadeIn(A, B, C, A_text, B_text, C_text)
        )
        self.play(ABC.animate.set_fill(BLUE, opacity=0.2))
        self.play(
            Create(B_ray, run_time=2),
            Create(C_ray, run_time=2)
        )
        self.play(FadeIn(P, P_text))
        self.play(Create(excircle, run_time=2))
        self.play(Create(OP, run_time=2))
        self.play(
            FadeIn(BC),
        )
        self.play(FadeIn(L, L_text))
        self.play(Create(circumscribed_circle, run_time=2))
        self.play(Create(BC_arc, run_time=2))
        self.play(Uncreate(BC_arc, run_time=2))
        self.play(
            Create(BL, run_time=2),
            Create(CL, run_time=2)
        )
        self.play(
            BL.animate.set_color(GREEN),
            CL.animate.set_color(GREEN),
            FadeIn(LO, LP)
        )
        self.play(all_anim.animate.shift(LEFT * 2.5))
        self.play(Write(text))
        self.wait(1)

        AO = Line(A.get_center(), O.get_center(), color=BLUE).set_stroke(width=2).scale(0.9)
        A_angle = Angle(
            Line(A.get_center(), B.get_center()),
            Line(A.get_center(), C.get_center())
        )
        text1 = MathTex(r"BL", r"=", r"CL").shift(RIGHT*3.3)
        text1[0].set_color(GREY)
        text1[2].set_color(GREY)
        #all_anim.shift(UP*1.7 + LEFT*0.5).scale(0.9)

        BO = Line(B.get_center(), O.get_center(), color=BLUE).set_stroke(width=2).scale(0.9)

        eq_1 = Group(
            Line(
                Line(B.get_center(), L.get_center()).get_center(),
                Line(B.get_center(), L.get_center()).shift(0.17 * (UP+RIGHT)).get_center()
            ),
            Line(
                Line(B.get_center(), L.get_center()).get_center(),
                Line(B.get_center(), L.get_center()).shift(0.17 * (DOWN + LEFT)).get_center()
            )

        )
        eq_3 = Group(
            Line(
                Line(L.get_center(), C.get_center()).get_center(),
                Line(L.get_center(), C.get_center()).shift(0.17 * (DOWN + RIGHT)).get_center()
            ),
            Line(
                Line(L.get_center(), C.get_center()).get_center(),
                Line(L.get_center(), C.get_center()).shift(0.17 * (UP + LEFT)).get_center()
            )
        )

        self.play(
            Create(A_angle),
            Create(AO, run_time=2),
            O_text.animate.shift(RIGHT*0.23),
            ReplacementTransform(text, text1),
            BL.animate.set_color(GREY),
            CL.animate.set_color(GREY),
            FadeOut(LO, LP),
            *[Create(elem, run_time=2) for elem in eq_1],
            *[Create(elem, run_time=2) for elem in eq_3]
        )
        LO.set_color(GREY)
        LP.set_color(GREY)
        BOL_angle = Angle(
            Line(O.get_center(), B.get_center()),
            Line(O.get_center(), L.get_center()),
            radius=0.3,
        )
        ABC_angle = Angle(
            Line(B.get_center(), A.get_center()),
            Line(B.get_center(), C.get_center()),
            other_angle=True
        )
        text2 = MathTex(
            r"\angle{BOL}", r"=", r"\frac{1}{2}",
            r"\angle{A}", r"+", r"\frac{1}{2}" , r"\angle{ABC}"
        ).shift(RIGHT*3.55).scale(0.9)
        text2[0].set_color(BLUE)
        text2[3].set_color(BLUE)
        text2[6].set_color(BLUE)
        self.play(
            Create(BO, run_time=2),
        )
        self.play(
            FadeOut(eq_1, eq_3),
            Create(BOL_angle),
            Create(ABC_angle),
            ReplacementTransform(text1, text2)
        )
        self.wait(2)
        LBO_angle = Angle(
            Line(B.get_center(), L.get_center()),
            Line(B.get_center(), O.get_center()),
            radius=0.5
        )
        LBC_angle = Angle(
            Line(B.get_center(), L.get_center()),
            Line(B.get_center(), C.get_center()),
            radius=0.3
        )
        CBO_angle = Angle(
            Line(B.get_center(), C.get_center()),
            Line(B.get_center(), O.get_center()),
            radius=0.6
        )
        LAC_angle = Angle(
            Line(A.get_center(), L.get_center()),
            Line(A.get_center(), C.get_center())
        )

        text4 = MathTex(
            r"\angle{LBC}", r"=", r"\angle{LAC}"
        ).shift(RIGHT*3.45+UP*0.5)
        text4[0].set_color(BLUE)
        text4[2].set_color(BLUE)
        text3 = MathTex(
            r"\angle{LBO}", r"=", r"\angle{LBC}", r"+", r"\angle{CBO}",
            r"=", r"\frac{1}{2}", r"\angle{A}", r"+", r"\frac{1}{2}" , r"\angle{ABC}"
        ).shift(RIGHT*3.45).scale(0.68)
        text3[0].set_color(BLUE)
        text3[2].set_color(BLUE)
        text3[4].set_color(BLUE)
        text3[7].set_color(BLUE)
        text3[10].set_color(BLUE)

        LC_arc = ArcBetweenPoints(L.get_center(), C.get_center(), radius=circumscribed_circle.radius - 0.25,
                                  color=YELLOW).set_stroke(width=2)
        #LC_ex = CL.copy().set_color(YELLOW)

        self.play(
            Create(LBO_angle, run_time=2),
            Create(LBC_angle, run_time=2),
            Create(CBO_angle, run_time=2),
            ReplacementTransform(text2, text3)
        )
        self.wait(2)
        self.play(
            Uncreate(A_angle, run_time=2),
            Uncreate(ABC_angle, run_time=2),
            Uncreate(BOL_angle, run_time=2),
            Uncreate(LBO_angle, run_time=2),
            #Uncreate(LBC_angle, run_time=2),
            Uncreate(CBO_angle, run_time=2)
        )
        self.play(
            Create(LC_arc, run_time=2),
            ReplacementTransform(text3, text4),
            Create(LAC_angle, run_time=2),
        )
        self.wait(2)
        self.play(
            Uncreate(LC_arc, run_time=2),
            Uncreate(LBC_angle, run_time=2),
            Uncreate(LAC_angle, run_time=2),
        )
        self.wait(1)

        BLO = Polygon(B.get_center(), L.get_center(), O.get_center())
        BLO.set_stroke(width=0)
        BLO.set_fill(YELLOW, opacity=0.5)
        text5 = MathTex(
            r"BL", r"=", r"OL", r"=", r"CL"
        ).shift(RIGHT*3.45+UP*0.5)
        text5[0].set_color(GREEN)
        text5[2].set_color(GREEN)
        text5[4].set_color(GREEN)
        eq_2 = Group(
            Line(
                Line(L.get_center(), O.get_center()).get_center(),
                Line(L.get_center(), O.get_center()).shift(0.25 * (RIGHT+ 0.1 * UP)).get_center()
            ),
            Line(
                Line(L.get_center(), O.get_center()).get_center(),
                Line(L.get_center(), O.get_center()).shift(0.25 * (LEFT + 0.1 * DOWN)).get_center()
            )
        )

        self.play(
            *[Create(elem, run_time=2) for elem in eq_1],
            *[Create(elem, run_time=2) for elem in eq_2],
            Create(BLO, run_time=2),
            BL.animate.set_color(GREEN),
            LO.animate.set_color(GREEN),
            ReplacementTransform(text4, text5[:3])
        )
        self.play(
            Uncreate(BLO, run_time=2),
        )
        self.play(
            Write(text5[3:]),
            *[Create(elem, run_time=2) for elem in eq_3],
            CL.animate.set_color(GREEN),
        )
        all_anim.add(eq_1, eq_2, eq_3, BO, AO)

        self.play(all_anim.animate.shift(UP*0.6). scale(0.9))

        text6 = MathTex(
            r"K", r"\in", r"\overrightarrow{\rm AB}",
        ).shift(RIGHT*3.45+UP*0.5)
        text6[0].set_color(RED)
        text6[2].set_color(BLUE)
        K = Dot(B_ray.get_all_points()[2], color=RED).set_stroke(width=1, color=WHITE).scale(0.8)
        K_text = MathTex(r"K", color=RED).next_to(K, LEFT).scale(0.8)
        BP = Line(B.get_center(), P.get_center(), color=GREY).set_stroke(width=1.5)
        self.play(
            FadeOut(
                eq_1, eq_2, eq_3
            )
        )
        self.play(
            FadeIn(K, K_text),
            ReplacementTransform(text5, text6),
            Create(BP, run_time=2)
        )
        self.wait(2)

        LBP_angle = Angle(
            Line(B.get_center(), L.get_center()),
            Line(B.get_center(), P.get_center()),
            radius=1.1,
            other_angle=True,
            color=GREEN
        )
        KBC_angle = Angle(
            Line(B.get_center(), C.get_center()),
            Line(B.get_center(), K.get_center()),
            radius=0.8,
            other_angle=True,
            color=RED
        )
        KBP_angle = Angle(
            Line(B.get_center(), P.get_center()),
            Line(B.get_center(), K.get_center()),
            radius=0.5,
            other_angle=True,
            color=RED
        )
        BPA_angle = Angle(
            Line(P.get_center(), A.get_center()),
            Line(P.get_center(), B.get_center()),
            color=BLUE,
            radius=0.75
        )
        A_new_angle = Angle(
            Line(A.get_center(), B.get_center()),
            Line(A.get_center(), C.get_center()),
            color=BLUE,
            radius=0.5
        )
        text7 = MathTex(
            r"\angle{LBP}", r"=", r"\frac{1}{2}", r"\angle{KBC}", r"-", r"\frac{1}{2}",
            r"\angle{A}", r"\\",
            r"\angle{KBP}", r"=", r"\frac{1}{2}", r"\angle{A}", r"+", r"\frac{1}{2}" ,
            r"\angle{BPA}", r"\\",
            r"\frac{1}{2}", r"\angle{KBC}", r"-", r"\frac{1}{2}", r"\angle{A}", r"=",
            r"\angle{BPA}"
        ).shift(RIGHT*3.45+UP*0.5).scale(0.8)

        BPA = Polygon(B.get_center(), P.get_center(), A.get_center())
        BPA.set_stroke(width=2)
        BPA.set_fill(color=YELLOW, opacity=0.5)
        text7[0].set_color(GREEN)
        text7[3].set_color(RED)
        text7[6].set_color(BLUE)
        text7[8].set_color(RED)
        text7[11].set_color(BLUE)
        text7[14].set_color(BLUE)
        text7[17].set_color(RED)
        text7[20].set_color(BLUE)
        text7[22].set_color(BLUE)
        self.play(
            Create(LBP_angle, run_time=2),
            Create(KBC_angle, run_time=2),
            Create(KBP_angle, run_time=2),
            Create(BPA_angle, run_time=2),
            Create(A_new_angle, run_time=2),
            ReplacementTransform(text6, text7[:15])
        )
        self.play(
            Create(BPA, run_time=2),
            FadeIn(text7[15:])
        )
        eq_4 = Group(
            Line(
                Line(L.get_center(), P.get_center()).get_center(),
                Line(L.get_center(), P.get_center()).shift(0.25 * (RIGHT+ 0.1 * UP)).get_center()
            ),
            Line(
                Line(L.get_center(), P.get_center()).get_center(),
                Line(L.get_center(), P.get_center()).shift(0.25 * (LEFT+ 0.1 * DOWN)).get_center()
            )
        )
        text8 = MathTex(
            r"BL", r"=",  r"PL"
        ).shift(RIGHT*3.45+UP*0.5)
        text8.set_color(GREEN)
        text8[1].set_color(WHITE)
        text9 = MathTex(
            r"LO", r"=",  r"LB", r"=", r"LC", r"=", r"LB"
        ).shift(RIGHT*3.45+UP*0.5)
        text9.set_color(GREEN)
        text9[1].set_color(WHITE)
        text9[3].set_color(WHITE)
        text9[5].set_color(WHITE)
        self.play(
            Uncreate(BPA, run_time=2),
            Uncreate(LBP_angle, run_time=2),
            Uncreate(KBC_angle, run_time=2),
            Uncreate(KBP_angle, run_time=2),
            Uncreate(BPA_angle, run_time=2),
            Uncreate(A_new_angle, run_time=2),
        )
        self.play(
            *[Create(elem, run_time=2) for elem in eq_1],
            *[Create(elem, run_time=2) for elem in eq_4],
            ReplacementTransform(text7, text8),
            LP.animate.set_color(GREEN)
        )
        self.play(
            *[Create(elem, run_time=2) for elem in eq_2],
            *[Create(elem, run_time=2) for elem in eq_3],
            ReplacementTransform(text8, text9)
        )
        self.wait(1)
