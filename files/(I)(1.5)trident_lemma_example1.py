from manim import *
import numpy as mp


class Trident_example1(ThreeDScene):
    def construct(self):
        inscribed_circle = Circle(color=GREY).set_stroke(width=2)
        I = Dot(inscribed_circle.get_center(), color=GREY).set_stroke(width=1, color=WHITE)
        I_text = MathTex(r"I", color=GREY).next_to(I, DOWN).scale(0.9)

        tangent1 = TangentLine(inscribed_circle, alpha=0.165, length=7.5)
        tangent2 = TangentLine(inscribed_circle, alpha=0.425, length=7)
        tangent3 = Line([-2, -1.05, 0], [4, -0.95, 0], color=WHITE)
        C = Dot(
            line_intersection(
                [tangent1.start, tangent1.end],
                [tangent2.start, tangent2.end]
            ),
            color=DARK_BLUE
        ).set_stroke(width=1, color=WHITE)
        C_text = MathTex(r"C", color=BLUE).next_to(C, UP).scale(0.9)
        A = Dot(
            line_intersection(
                [tangent2.start, tangent2.end],
                [tangent3.start, tangent3.end]
            ),
            color=DARK_BLUE
        ).set_stroke(width=1, color=WHITE)
        A_text = MathTex(r"A", color=BLUE).next_to(A, LEFT).scale(0.9)
        B = Dot(
            line_intersection(
                [tangent3.start, tangent3.end],
                [tangent1.start, tangent1.end]
            ),
            color=DARK_BLUE
        ).set_stroke(width=1, color=WHITE)
        B_text = MathTex(r"B", color=BLUE).next_to(B, RIGHT).scale(0.9)
        ABC = Polygon(A.get_center(), B.get_center(), C.get_center(), color=GREY).set_stroke(width=2)

        circumscribed_circle = Circle.from_three_points(A.get_center(), B.get_center(), C.get_center(), color=GREY).set_stroke(width=2)

        AC_arc = ArcBetweenPoints(C.get_center(), A.get_center(), radius=circumscribed_circle.radius)
        BC_arc = ArcBetweenPoints(B.get_center(), C.get_center(), radius=circumscribed_circle.radius)
        K = Dot(
            AC_arc.get_end_anchors()[3],
            color=DARK_BLUE
        ).set_stroke(width=1, color=WHITE)
        K_text = MathTex(r"K", color=BLUE).next_to(K, LEFT).scale(0.9)
        P = Dot(
            BC_arc.get_end_anchors()[3],
            color=DARK_BLUE
        ).set_stroke(width=1, color=WHITE)
        P_text = MathTex(r"P", color=BLUE).next_to(P, RIGHT).scale(0.9)
        KP = Line(K.get_center(), P.get_center(), color=GREY).set_stroke(width=2)

        N = Dot(
            line_intersection(
                [A.get_center(), C.get_center()],
                [K.get_center(), P.get_center()]
            ),
            color=GREEN
        ).set_stroke(width=1, color=WHITE)
        N_text =MathTex(r"N", color=GREEN).next_to(N, 0.85*DOWN+RIGHT*0.01).scale(0.9)

        all_anim = Group(
            inscribed_circle, circumscribed_circle,
            I, I_text, K, K_text, P, P_text, N, N_text,
            KP,
            #AC_arc, BC_arc,
            #tangent1, tangent2, tangent3,
            A, B, C, A_text, B_text, C_text,
            ABC,
        ).shift(LEFT)

        self.play(FadeIn(A, B, C, A_text, B_text, C_text))
        self.play(Create(ABC, run_time=2))

        C_angle = RightAngle(
            Line(C.get_center(), A.get_center()),
            Line(C.get_center(), B.get_center()),
            length=0.25
        )
        self.play(Create(C_angle, run_time=2))
        self.play(Create(circumscribed_circle, run_time=2))
        self.play(FadeIn(K, P, K_text, P_text))
        self.play(Create(KP, run_time=2))
        self.play(FadeIn(N, N_text))
        self.play(Create(inscribed_circle, run_time=2))
        self.play(FadeIn(I, I_text))
        IN = Line(I.get_center(), N.get_center(), color=GREY).set_stroke(width=2)
        IC = Line(I.get_center(), C.get_center(), color=GREY).set_stroke(width=2)
        self.play(Create(IN, run_time=2), Create(IC, run_time=2))
        NIC_angle = Angle(
            IN, IC, other_angle=True
        )
        self.play(Create(NIC_angle, run_time=2))
        all_anim.add(
            C_angle, IN, IC, NIC_angle
        )
        self.play(all_anim.animate.shift(LEFT*2.6))
        text = MathTex(r"\angle", r"{NIC}", r"-", r"?").shift(RIGHT*3.3)
        text[1].set_color(GREEN)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text, NIC_angle))
        all_anim.remove(NIC_angle)
        IA = Line(I.get_center(), A.get_center(), color=GREY).set_stroke(width=2)
        IB = Line(I.get_center(), B.get_center(), color=GREY).set_stroke(width=2)
        self.play(Create(IA, run_time=2), Create(IB, run_time=2))
        all_anim.add(
            IA, IB
        )
        self.play(all_anim.animate.scale(0.9))
        circumscribed_circle_AIC = DashedVMobject(
            Circle.from_three_points(
                A.get_center(), I.get_center(), C.get_center(), color=RED
            ).set_stroke(width=2)
        )
        circumscribed_circle_BIC = DashedVMobject(
            Circle.from_three_points(
                B.get_center(), I.get_center(), C.get_center(), color=RED
            ).set_stroke(width=2)
        )
        AIC = Polygon(A.get_center(), I.get_center(), C.get_center()).set_stroke(width=2)
        AIC.set_fill(RED, opacity=0.5)
        BIC = Polygon(B.get_center(), I.get_center(), C.get_center()).set_stroke(width=2)
        BIC.set_fill(RED, opacity=0.5)
        self.play(
            Create(AIC, run_time=2),
            Create(BIC, run_time=2),
            Create(circumscribed_circle_AIC, run_time=2),
            Create(circumscribed_circle_BIC, run_time=2)
        )
        self.play(
            Uncreate(AIC, run_time=2),
            Uncreate(BIC, run_time=2),
            Uncreate(circumscribed_circle_AIC, run_time=2),
            Uncreate(circumscribed_circle_BIC, run_time=2)
        )
        text1 = MathTex(r"KP", r"\perp", r"CI").shift(RIGHT*3.3)
        text1[0].set_color(BLUE)
        text1[2].set_color(BLUE)
        right_angle_KPCI = RightAngle(
            Line(
                line_intersection(
                    [K.get_center(), P.get_center()],
                    [I.get_center(), C.get_center()]
                ),
                P.get_center()
            ),
            Line(
                line_intersection(
                    [K.get_center(), P.get_center()],
                    [I.get_center(), C.get_center()]
                ),
                I.get_center()
            ),
            length=0.3
        )
        self.play(
            Write(text1),
            Create(right_angle_KPCI, run_time=2)
        )
        self.wait(1)
        inscribed_circle_ex = inscribed_circle.copy().set_color(YELLOW)
        text2 = MathTex(r"\angle", r"{NIC}", r"=", r"45^\circ").shift(RIGHT*3.3)
        text2[1].set_color(GREEN)
        NIC_angle_ex = Angle(
            Line(I.get_center(), C.get_center()),
            Line(I.get_center(), N.get_center()),
            radius=0.5
        )
        self.play(
            Create(NIC_angle_ex, run_time=2),
            Create(inscribed_circle_ex, run_time=2),
            ReplacementTransform(text1, text2)
        )
        self.play(
            Uncreate(inscribed_circle_ex, run_time=2)
        )

