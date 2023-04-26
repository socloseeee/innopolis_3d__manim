from manim import *
from numpy import linalg as LA

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class GetIntersections:
    def get_coord_from_proportion(self,vmob,proportion):
        return vmob.point_from_proportion(proportion)

    def get_points_from_curve(self, vmob, dx=0.005):
        coords = []
        for point in Range(0, 1, dx):
            dot = Dot(self.get_coord_from_proportion(vmob,point))
            coords.append(dot.get_center())
        return coords

    def get_intersections_between_two_vmobs(self, vmob1, vmob2,
                                            tolerance=0.05,
                                            radius_error=0.2,
                                            use_average=True,
                                            use_first_vmob_reference=False):
        coords_1 = self.get_points_from_curve(vmob1)
        coords_2 = self.get_points_from_curve(vmob2)
        intersections = []
        for coord_1 in coords_1:
            for coord_2 in coords_2:
                distance_between_points = LA.norm(coord_1 - coord_2)
                if use_average:
                    coord_3 = (coord_2 - coord_1) / 2
                    average_point = coord_1 + coord_3
                else:
                    if use_first_vmob_reference:
                        average_point = coord_1
                    else:
                        average_point = coord_2
                if len(intersections) > 0 and distance_between_points < tolerance:
                    last_intersection=intersections[-1]
                    distance_between_previus_point = LA.norm(average_point - last_intersection)
                    if distance_between_previus_point > radius_error:
                        intersections.append(average_point)
                if len(intersections) == 0 and distance_between_points < tolerance:
                    intersections.append(average_point)
        return intersections

class Trident_example2(ThreeDScene, GetIntersections):
    def construct(self):
        circle1 = Circle(radius=1.75, color=GREY).set_stroke(width=2).shift(1.4*(UP+0.6*RIGHT))
        O = Dot(circle1.get_center(), color=DARK_BLUE).set_stroke(width=1.5, color=WHITE).scale(0.75)
        O_text = MathTex(r"O", color=BLUE).next_to(O, UP).scale(0.75)

        circle2 = Circle(radius=1.75, color=GREY).set_stroke(width=2).shift(1.4*(0.15*LEFT+1.10*DOWN))
        O_hatch = Dot(circle2.get_center(), color=DARK_BLUE).set_stroke(width=1.5, color=WHITE).scale(0.75)
        O_hatch_text = MathTex(r"O'", color=BLUE).next_to(O_hatch, DOWN).scale(0.75)

        tangent1 = TangentLine(circle2, alpha=0.0546, length=11)
        tangent2 = TangentLine(circle2, alpha=0.4276, length=11)

        A = Dot(tangent1.get_center(), color=GREEN).set_stroke(width=1.5, color=WHITE).scale(0.75)
        A_text = MathTex(r"A", color=BLUE).next_to(A, RIGHT).scale(0.75)
        B = Dot(tangent2.get_center(), color=BLUE).set_stroke(width=1.5, color=WHITE).scale(0.75)
        B_text = MathTex(r"B", color=BLUE).next_to(B, LEFT).scale(0.75)
        C = Dot(
            line_intersection(
                [tangent1.start, tangent1.end],
                [tangent2.start, tangent2.end]
            ),
            color=GREY
        ).set_stroke(width=1.5, color=WHITE).scale(0.75)
        C_text = MathTex(r"C", color=BLUE).next_to(C, UP).scale(0.75)

        CB_tangent = Line(C.get_center(), tangent2.get_end(), color=GREY).set_stroke(width=2)
        CA_tangent = Line(C.get_center(), tangent1.get_start(), color=GREY).set_stroke(width=2)

        X, Y = [
            Dot(
                color=GREY
            ).set_stroke(
                width=1.5,
                color=WHITE
            ).scale(0.75).move_to(point) for point in self.get_intersections_between_two_vmobs(circle1, circle2)
        ]
        X_text = MathTex(r"X", color=GREY).next_to(X, DOWN).scale(0.75)
        Y_text = MathTex(r"Y", color=GREY).next_to(Y, DOWN).scale(0.75)

        A_hatch = [
            Dot(
                color=GREEN
            ).set_stroke(
                width=1.5,
                color=WHITE
            ).scale(0.75).move_to(point) for point in self.get_intersections_between_two_vmobs(circle1, CB_tangent)
        ][1]
        A_hatch_text = MathTex(r"A'", color=GREEN).next_to(A_hatch, LEFT).scale(0.75)
        B_hatch = [
            Dot(
                color=GREY
            ).set_stroke(
                width=1.5,
                color=WHITE
            ).scale(0.75).move_to(point) for point in self.get_intersections_between_two_vmobs(circle1, CA_tangent)
        ][1]
        B_hatch_text = MathTex(r"B'", color=GREY).next_to(B_hatch, 0.1*(1.55*UP+RIGHT)).scale(0.75)

        OA_hatch = Line(O.get_center(), A_hatch.get_center(), color=GREY).set_stroke(width=2)
        A_hatchO = Line(A_hatch.get_center(), O_hatch.get_center(), color=GREY).set_stroke(width=2)
        O_hatch_A = Line(O_hatch.get_center(), A.get_center(), color=GREY).set_stroke(width=2)

        XY = Line(X.get_center(), Y.get_center(), color=GREY).set_stroke(width=2)

        all_anim = Group(
            A, A_text, B, B_text, C, C_text,
            O, O_text, O_hatch, O_hatch_text,
            CB_tangent, CA_tangent,
            #tangent1, tangent2,
            #ABC,
            circle1, circle2,
            X, Y, X_text, Y_text,
            A_hatch, B_hatch, A_hatch_text, B_hatch_text,
            OA_hatch, A_hatchO, O_hatch_A,
            XY
        )
        #self.add(*all_anim)

        self.play(FadeIn(O, O_text, O_hatch, O_hatch_text))
        self.play(
            Create(circle1, run_time=2),
            Create(circle2, run_time=2)
        )
        self.play(FadeIn(X, Y, X_text, Y_text, A, A_text, A_hatch, A_hatch_text))
        self.play(
            Create(OA_hatch, run_time=2),
            Create(O_hatch_A, run_time=2),
            Create(XY, run_time=2),
        )
        text = MathTex(
            r"A'", r"O", r"=", r"O'", r"A", r"=", r"XY", r"=", r"1"
        ).shift(RIGHT*3.3)
        text[0].set_color(GREEN)
        text[1].set_color(BLUE)
        text[3].set_color(BLUE)
        text[4].set_color(BLUE)
        text[6].set_color(GREY)

        self.play(
            Group(
                circle1, circle2,
                A, O, A_hatch, O_hatch, A_text, O_text, A_hatch_text, O_hatch_text, X, Y, X_text, Y_text,
                OA_hatch, O_hatch_A, XY
            ).animate.shift(LEFT*3)
        )
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))

        all_anim.shift(LEFT*3)
        Group(
            circle1, circle2,
            A, O, A_hatch, O_hatch, A_text, O_text, A_hatch_text, O_hatch_text, X, Y, X_text, Y_text,
            OA_hatch, O_hatch_A, XY
        ).shift(RIGHT * 3)

        self.play(FadeIn(C, C_text))
        self.play(
            Create(CA_tangent, run_time=2),
            Create(CB_tangent, run_time=2),
            FadeIn(B, B_text)
        )
        # \Omega
        circle1_text = MathTex(r"\Omega", color=PURPLE).move_to(circle1.get_center()).shift(0.85*(UP+RIGHT))
        circle2_text = MathTex(r"\Omega'", color=PURPLE).move_to(circle2.get_center()).shift(0.85*(DOWN+LEFT))
        text1 = MathTex(r"\overrightarrow{\rm CA}", r"\cap", r"\Omega", r"=", r"B'").shift(RIGHT*3)
        text1[0].set_color(BLUE)
        text1[2].set_color(PURPLE)
        text1[4].set_color(GREY)
        circle1_ex = circle1.copy().set_color(PURPLE).set_stroke(width=4)
        CA_tangent_ex = CA_tangent.copy().set_color(BLUE)
        self.play(
            FadeIn(
                circle1_text,
                circle2_text,
                B_hatch, B_hatch_text
            ),
            Create(CA_tangent_ex, run_time=2),
            Create(circle1_ex, run_time=2),
            Write(text1)
        )
        ACB_angle = Angle(
            Line(C.get_center(), B.get_center()),
            Line(C.get_center(), A.get_center()),
            radius=0.4
        )
        CO_hatch = Line(C.get_center(), O_hatch.get_center(), color=GREY).set_stroke(width=2)
        K = [Dot(color=YELLOW).set_stroke(
                width=1.5,
                color=WHITE
            ).move_to(point).scale(0.75) for point in self.get_intersections_between_two_vmobs(CO_hatch, circle1)][1]
        K_text = MathTex(r"K", color=YELLOW).next_to(K, 0.1*RIGHT+UP*1.5).scale(0.75)
        text2 = MathTex(r"CO'", r"\cap", r"\Omega", r"=", r"K").shift(RIGHT*3)
        text2[0].set_color(BLUE)
        text2[2].set_color(PURPLE)
        text2[4].set_color(YELLOW)
        self.play(
            Uncreate(CA_tangent_ex, run_time=2),
            Create(ACB_angle, run_time=2),
            Create(CO_hatch, run_time=2)
        )
        CO_hatch_ex = CO_hatch.copy().set_color(BLUE)
        self.play(
            FadeIn(K, K_text),
            ReplacementTransform(text1, text2),
            Create(CO_hatch_ex, run_time=2),
            #Create(circle1_ex, run_time=2)
        )
        self.wait(1)
        text3 = MathTex(r"A'", r"K", r"=", r"K", r"B'").shift(RIGHT*3)
        text3[0].set_color(GREEN)
        text3[1].set_color(YELLOW)
        text3[3].set_color(YELLOW)
        text3[4].set_color(GREY)
        KA_hatch_arc = ArcBetweenPoints(A_hatch.get_center(), K.get_center(), radius=circle1.radius, color=YELLOW).set_stroke(width=4)
        KB_hatch_arc = ArcBetweenPoints(K.get_center(), B_hatch.get_center(), radius=circle1.radius, color=YELLOW).set_stroke(width=4)

        self.play(

            Create(KA_hatch_arc, run_time=2),
            Create(KB_hatch_arc, run_time=2),
            ReplacementTransform(text2, text3)
        )
        self.play(
            Uncreate(KA_hatch_arc, run_time=2),
            Uncreate(KB_hatch_arc, run_time=2)
        )
        self.play(
            Uncreate(circle1_ex, run_time=2),
        )
        OO_hatch = Line(O.get_center(), O_hatch.get_center(), color=RED).set_stroke(width=2)
        text4 = MathTex(r"OO'", r"=", r"2").shift(RIGHT*3)
        text4[0].set_color(RED)
        self.play(
            Create(OO_hatch, run_time=2),
            ReplacementTransform(text3, text4)
        )
        text5 = MathTex(r"O'", r"K", r"*", r"O'C", r"=2").shift(RIGHT*3)
        O_hatchK = Line(O_hatch.get_center(), K.get_center(), color=YELLOW).set_stroke(width=2)
        text5[0].set_color(BLUE)
        text5[1].set_color(YELLOW)
        text5[3].set_color(BLUE)
        self.wait(1)
        self.play(
            ReplacementTransform(text4, text5),
            Create(O_hatchK, run_time=2)
        )
        A_hatch_CO_hatch = Angle(
            Line(C.get_center(), A_hatch.get_center()),
            Line(C.get_center(), O_hatch.get_center()),
            radius=0.7
        )
        A_hatch_CO_hatch_text = MathTex(r"\gamma", color=WHITE).next_to(A_hatch_CO_hatch, 0.1*DOWN).scale(0.75)
        text6 = MathTex(r"\angle{", r"A'", "CO'}", r"=", r"\gamma").shift(RIGHT*3)
        text6[1].set_color(GREEN)
        text6[2].set_color(BLUE)
        O_hatchB = Line(O_hatch.get_center(), B.get_center(), color=BLUE).set_stroke(width=2)
        self.play(Create(A_hatch_CO_hatch, run_time=2))
        self.play(ReplacementTransform(text5, text6), FadeIn(A_hatch_CO_hatch_text))
        text7 = MathTex(r"\sin{\gamma}", r"=", r"\frac{O'B}{CO'}", r"=", r"\frac{1}{CO'}").shift(RIGHT*3)
        text7[2][0:3].set_color(BLUE)
        text7[2][4:7].set_color(BLUE)
        text7[4][2:].set_color(BLUE)
        self.wait(1)
        self.play(
            Create(O_hatchB, run_time=2),
            ReplacementTransform(text6, text7)
        )
        text8 = MathTex(
            r"A'K", r"=", r"2", r"*", r"OC", r"*", r"\sin{\gamma}", r"=",
            r"\frac{2}{CO'}", r"=", r"O'K"
        ).shift(RIGHT*3).scale(0.85)
        text8[0].set_color(LIGHT_BROWN)
        text8[4].set_color(RED)
        text8[8][1:].set_color(BLUE)
        text8[-1].set_color(YELLOW)
        A_hatchK = Line(A_hatch.get_center(), K.get_center(), color=LIGHT_BROWN).set_stroke(width=2)
        OC = Line(O.get_center(), C.get_center(), color=RED).set_stroke(width=2)
        self.play(
            Create(A_hatchK, run_time=2),
            Create(OC, run_time=2),
            ReplacementTransform(text7, text8)
        )
        A_hatchB_hatch = Line(A_hatch.get_center(), B_hatch.get_center(), color=GREEN).set_stroke(width=2)
        C_hatch = Dot([-2.2, -0.07, 0], color=PINK).set_stroke(
                width=1.5,
                color=WHITE
            ).scale(0.75)
        C_hatch_text = MathTex(r"C'", color=PINK).next_to(C_hatch, 0.1*(0.75*UP)).scale(0.75)
        self.play(
            Group(circle2, K_text).animate.shift(UP*0.05),
            Group(CB_tangent,X,X_text,ACB_angle, A_hatch_CO_hatch).animate.shift(LEFT*0.03),
            Create(A_hatchB_hatch, run_time=2)
        )
        text9 = MathTex(
            r"A'B'", r"\cap", r"\Omega'", r"=", r"C'"
        ).shift(RIGHT*3)
        text9[0].set_color(GREEN)
        text9[2].set_color(PURPLE)
        text9[4].set_color(PINK)
        self.play(
            FadeIn(C_hatch, C_hatch_text),
            ReplacementTransform(text8, text9)
        )
        self.wait(1)
        A_hatchO_hatch = Line(A_hatch.get_center(), O_hatch.get_center(), color=GREEN).set_stroke(width=2)
        C_hatchO_hatch = Line(C_hatch.get_center(), O_hatch.get_center(), color=PINK).set_stroke(width=2)
        O_hatchB_hatch = Line(O_hatch.get_center(), B_hatch.get_center(), color=BLUE).set_stroke(width=2)

        A_hatchO_hatchA_angle = Angle(
            Line(O_hatch.get_center(), A.get_center()),
            Line(O_hatch.get_center(), A_hatch.get_center())
        )
        AO_hatchC_hatch_angle = Angle(
            Line(O_hatch.get_center(), C_hatch.get_center()),
            Line(O_hatch.get_center(), A.get_center()),
            other_angle=True,
            radius=0.5
        )
        C_hatchO_hatchB_angle = Angle(
            Line(O_hatch.get_center(), C_hatch.get_center()),
            Line(O_hatch.get_center(), B.get_center()),
            radius=0.6
        )
        CB_hatchA_hatch_angle = Angle(
            Line(B_hatch.get_center(), C.get_center()),
            Line(B_hatch.get_center(), A_hatch.get_center()),
            radius=0.9
        )
        CA_hatchB_hatch_angle = Angle(
            Line(A_hatch.get_center(), C.get_center()),
            Line(A_hatch.get_center(), B_hatch.get_center()),
            other_angle=True
        )
        O_hatchA_hatchO_angle = Angle(
            Line(A_hatch.get_center(), O.get_center()),
            Line(A_hatch.get_center(), O_hatch.get_center()),
            other_angle=True,
            radius=0.5
        )
        O_hatchA_hatchB_hatch_angle = Angle(
            Line(A_hatch.get_center(), O_hatch.get_center()),
            Line(A_hatch.get_center(), B_hatch.get_center()),
            radius=0.6
        )
        B_hatchA_hatchO_angle = Angle(
            Line(A_hatch.get_center(), O.get_center()),
            Line(A_hatch.get_center(), B_hatch.get_center()),
            other_angle=True,
            radius=0.7
        )
        C_hatchO_hatchA_hatch_angle = Angle(
            Line(O_hatch.get_center(), A_hatch.get_center()),
            Line(O_hatch.get_center(), C_hatch.get_center()),
            other_angle=True,
            radius=0.7
        )
        BCA_angle = Angle(
            Line(C.get_center(), A.get_center()),
            Line(C.get_center(), B.get_center())
        )
        text10 = MathTex(
            r"\angle{A'O'A}", r"=", r"\angle{AO'C'}", r"+", r"\frac{1}{2}", r"\angle{C'O'B}",
            r"=", r"\angle{CB'A'}", r"+", r"\frac{1}{2}", r"\angle{CA'B'}", r"\\",
            r"\angle{O'A'O}", r"=", r"\angle{O'A'B'}", r"+", r"\angle{B'A'O}", r"=",
            r"\frac{\pi}{2}", r"-", r"\angle{C'O'A'}", r"+", r"\frac{\pi}{2}", r"-",
            r"\angle{BCA}\\",r"=", r"\pi", r"-", r"\angle{BCA}", r"-", r"\frac{1}{2}",
            r"\angle{CA'B'}", r"=", r"\angle{CB'A'}", r"+", r"\frac{1}{2}", r"\angle{CA'B'}"

        ).shift(RIGHT*3).scale(0.53)
        text10[0][1:3].set_color(GREEN), text10[14][1:3].set_color(BLUE)
        text10[0][3:5].set_color(BLUE),  text10[14][3:5].set_color(GREEN)
        text10[0][5].set_color(BLUE),    text10[14][5].set_color(GREY)
        text10[2][1].set_color(BLUE),    text10[14][6].set_color(GREY)
        text10[2][2:4].set_color(BLUE),  text10[16][1:3].set_color(GREY)
        text10[2][4].set_color(BLUE),    text10[16][3:5].set_color(GREEN)
        text10[2][5].set_color(BLUE),    text10[16][5].set_color(BLUE)
        text10[5][1:3].set_color(PINK),  text10[20][1:3].set_color(PINK)
        text10[0][3:5].set_color(BLUE),  text10[20][3:5].set_color(BLUE)
        text10[0][5].set_color(BLUE),    text10[20][5].set_color(GREEN)
        text10[2][1].set_color(BLUE),    text10[20][6].set_color(GREEN)
        text10[5][3:5].set_color(BLUE),  text10[24][1:4].set_color(BLUE)
        text10[5][5].set_color(BLUE),    text10[28][1:4].set_color(BLUE)
        text10[7][1].set_color(BLUE),    text10[31][1].set_color(BLUE)
        text10[7][2:4].set_color(GREY),  text10[31][2:4].set_color(GREEN)
        text10[7][4].set_color(GREEN),   text10[31][4].set_color(GREY)
        text10[7][5].set_color(GREEN),   text10[31][5].set_color(GREY)
        text10[10][1].set_color(BLUE),   text10[33][1].set_color(BLUE)
        text10[10][2:4].set_color(GREEN),text10[33][2:4].set_color(GREY)
        text10[10][4].set_color(GREY),   text10[33][4].set_color(GREEN)
        text10[10][5].set_color(GREY),   text10[33][5].set_color(GREEN)
        text10[12][1:3].set_color(BLUE), text10[36][1].set_color(BLUE)
        text10[12][3:5].set_color(GREEN),text10[36][2:4].set_color(GREEN)
        text10[12][5].set_color(BLUE),   text10[36][4].set_color(GREY)
        text10[36][5].set_color(GREY)


        self.play(
            FadeOut(
                #ACB_angle,
                A_hatch_CO_hatch,
                A_hatch_CO_hatch_text
            ),
            Create(A_hatchO_hatch, run_time=2),
            Create(C_hatchO_hatch, run_time=2),
            Create(O_hatchB_hatch, run_time=2),
        )
        self.play(
            Create(A_hatchO_hatchA_angle, run_time=2),
            Create(AO_hatchC_hatch_angle, run_time=2),
            Create(C_hatchO_hatchB_angle, run_time = 2),
            Create(CB_hatchA_hatch_angle, run_time = 2),
            Create(CA_hatchB_hatch_angle, run_time = 2),
            Create(O_hatchA_hatchO_angle, run_time = 2),
            Create(O_hatchA_hatchB_hatch_angle, run_time = 2),
            Create(B_hatchA_hatchO_angle, run_time=2),
            Create(C_hatchO_hatchA_hatch_angle, run_time=2),
            ReplacementTransform(text9, text10)
        )
        self.wait(1)
        self.play(
            FadeOut(
                ACB_angle,
                A_hatchO_hatchA_angle,
                AO_hatchC_hatch_angle,
                C_hatchO_hatchB_angle,
                CB_hatchA_hatch_angle,
                CA_hatchB_hatch_angle,
                O_hatchA_hatchO_angle,
                O_hatchA_hatchB_hatch_angle,
                B_hatchA_hatchO_angle,
                C_hatchO_hatchA_hatch_angle,
            )
        )
        eq_1 = Group(
            Line(
                Line(O.get_center(), A_hatch.get_center()).get_center(),
                Line(O.get_center(), A_hatch.get_center()).shift(0.25 * (0.1 *RIGHT + UP)).get_center()
            ),
            Line(
                Line(O.get_center(), A_hatch.get_center()).get_center(),
                Line(O.get_center(), A_hatch.get_center()).shift(0.25 * (0.1 *LEFT + DOWN)).get_center()
            )
        )
        eq_2 = Group(
            Line(
                Line(O_hatch.get_center(), A.get_center()).get_center(),
                Line(O_hatch.get_center(), A.get_center()).shift(0.25 * (0.1 *LEFT +  UP)).get_center()
            ),
            Line(
                Line(O_hatch.get_center(), A.get_center()).get_center(),
                Line(O_hatch.get_center(), A.get_center()).shift(0.25 * (0.1 *RIGHT + DOWN)).get_center()
            )
        )
        text11 = MathTex(r"O'A", r"=", r"OA'").shift(RIGHT*3)
        text11[0].set_color(BLUE)
        text11[2].set_color(BLUE)
        text12 = MathTex(r"AA'", r"=", r"OO'", r"=", r"\sqrt{3}").shift(RIGHT*3)
        text12[0].set_color(GOLD)
        text12[2].set_color(RED)
        AA_hatch = Line(A.get_center(), A_hatch.get_center(), color=GOLD).set_stroke(width=2)
        self.play(
            *[Create(elem, run_time=2) for elem in eq_1],
            *[Create(elem, run_time=2) for elem in eq_2],
            ReplacementTransform(text10, text11)
        )
        self.wait(2)
        self.play(
            *[Uncreate(elem, run_time=2) for elem in eq_1],
            *[Uncreate(elem, run_time=2) for elem in eq_2],
            Create(AA_hatch, run_time=2),
            ReplacementTransform(text11, text12)
        )
        self.wait(1)
