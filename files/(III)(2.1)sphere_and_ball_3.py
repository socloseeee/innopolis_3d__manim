from manim import *
from math import sqrt
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


class sphere_and_ball_3(ThreeDScene, GetIntersections):
    def construct(self):
        circle = Circle(radius=3, arc_center=ORIGIN).set_stroke(width=2)
        ellips = Ellipse(
                color=RED,
                width=circle.radius*2,
                height=1,
            )
        ellips_dashed = DashedVMobject(
            ellips
        ).set_stroke(width=2)
        self.play(
            Create(circle, run_time=2),
            Create(ellips_dashed, run_time=2)
        )
        r = Line(ORIGIN, LEFT*3, color=YELLOW).set_stroke(width=2)
        r_text = MathTex(r"1").next_to(r, UP)
        self.play(
            Create(r, run_time=2),
            FadeIn(r_text)
        )
        O = Dot(circle.get_center(), color=RED).set_stroke(width=1.5, color=WHITE).scale(0.75)
        O_text = MathTex(r"O").next_to(O, RIGHT)
        BC_ellips = ellips.copy().set_color(BLUE).set_stroke(width=2).shift(DOWN * 1.5).scale(0.855)

        A = Dot([0, 2.55, 0], color=GREY).set_stroke(width=1.5, color=WHITE).scale(0.75)
        A_text = MathTex(r"A").next_to(A, UP)
        B = Dot(BC_ellips.get_all_points()[20], color=GREY).set_stroke(width=1.5, color=WHITE).scale(0.75)
        B_text = MathTex(r"B").next_to(B, (LEFT+DOWN))
        C = Dot(BC_ellips.get_all_points()[27], color=GREY).set_stroke(width=1.5, color=WHITE).scale(0.75)
        C_text = MathTex(r"C").next_to(C, (RIGHT+DOWN))
        AB = ArcBetweenPoints(A.get_center(), B.get_center(), radius=3).set_stroke(width=2.5)
        CA = ArcBetweenPoints(C.get_center(), A.get_center(), radius=3).set_stroke(width=2.5)
        BC = ArcBetweenPoints(B.get_center(), C.get_center(), radius=7).set_stroke(width=2.5)
        BC.set_y(BC.get_y() + 0.02)

        x = 68.5
        AB_ellips = DashedVMobject(
            Ellipse(width=5.25, height=4.1).rotate(x*DEGREES).set_stroke(width=2).set_color(BLUE)
        )
        CA_ellips = DashedVMobject(
            Ellipse(width=5.25, height=4.1).rotate((180-x) * DEGREES).set_stroke(width=2).set_color(BLUE)
        )
        BC_ellips = ellips.copy().set_color(BLUE).set_stroke(width=2).shift(DOWN*1.5).scale(0.855)
        self.wait(1)
        self.play(FadeOut(r, r_text))
        self.wait(1)
        self.play(
            Create(AB_ellips, run_time=2),
            Create(CA_ellips, run_time=2),
            Create(BC_ellips, run_time=2),
        )
        self.play(FadeIn(A, B, C))
        self.play(
            Uncreate(AB_ellips, run_time=2),
            Uncreate(CA_ellips, run_time=2),
            Uncreate(BC_ellips, run_time=2),
            FadeIn(BC, CA, AB)
        )
        self.play(
            FadeIn(A, B, C, A_text, B_text, C_text),
        )
        #self.add(NumberPlane())
        self.wait(1)
        self.play(
            Group(
                circle, ellips_dashed, AB, BC, CA, A, B, C, A_text, B_text, C_text
            ).animate.shift(LEFT*3)
        )
        Group(O_text, ellips, O).shift(LEFT*3)
        text = MathTex(r"AB < \pi \\AC < \pi \\ BC < \pi").shift(RIGHT*3).scale(1.3)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeIn(O, O_text), FadeOut(text))
        self.wait(1)
        arc_conf = {"stroke_width": 0}
        poly_conf = {"stroke_width": 0, "stroke_color": WHITE,
                     "fill_opacity": 0.5, "color": WHITE}
        a = A.get_center()
        b = B.get_center()
        c = C.get_center()
        AB_arc = ArcBetweenPoints(a, b, radius=3, **arc_conf)
        CA_arc = ArcBetweenPoints(c, a, radius=3, **arc_conf)
        BC_arc = ArcBetweenPoints(b, c, radius=7, **arc_conf)
        ABC = ArcPolygonFromArcs(AB_arc, CA_arc, BC_arc, **poly_conf)
        text1 = MathTex(
            r"\pi=S_{ABC} = \angle{A} + \angle{B} + \angle{C} - \pi \\",
            r"\angle{A} + \angle{B} + \angle{C}=2\pi"
        ).shift(RIGHT*3.5).scale(0.85)
        self.play(FadeIn(ABC), Write(text1[0]))
        A_angle = Angle(
            Line(A.get_center(), RIGHT*0.6 + UP*1.3),
            Line(A.get_center(), LEFT*10),
            other_angle=True
        )
        B_angle = Angle(
            Line(B.get_center(), B.copy().shift(LEFT*0.135+UP*0.3).get_center()),
            Line(B.get_center(), B.copy().shift(RIGHT*0.3+ DOWN*0.05).get_center()),
            other_angle=True
        )
        C_angle = Angle(
            Line(C.get_center(), C.copy().shift(UP*0.3+RIGHT*0.13).get_center()),
            Line(C.get_center(), C.copy().shift(LEFT*0.3+DOWN*0.05).get_center())
        )
        self.wait(1)
        self.play(
            FadeOut(ABC),
            Write(text1[1]),
            Create(A_angle, run_time=2),
            Create(B_angle,run_time=2),
            Create(C_angle, run_time=2),
        )
        self.play(FadeOut(A_angle, B_angle, C_angle, text1))
        AB_arc = ArcBetweenPoints(A.get_center(), B.get_center(), radius=3).set_stroke(width=2.5)
        OA_arc = ArcBetweenPoints(O.get_center(), A.get_center(), radius=100).set_stroke(width=0)
        #AO_arc = ArcBetweenPoints(A.get_center(), O.get_center(), radius=100)
        BO = DashedLine(B.get_center(), O.get_center()).set_stroke(width=2.5)
        AO = DashedLine(A.get_center(), O.get_center()).set_stroke(width=2.5)
        BO_arc = ArcBetweenPoints(B.get_center(), O.get_center(), radius=100).set_stroke(width=0)
        OAB = ArcPolygonFromArcs(AB_arc, OA_arc, BO_arc, **poly_conf)
        D = Dot([ellips.get_all_points()[10][0]+0.65, ellips.get_all_points()[10][1]-0.3, 0], color=PURPLE).set_stroke(width=1.5, color=WHITE).scale(0.75)
        D_text = MathTex(r"D").next_to(D, UP + LEFT*0.1)
        d = D.get_center()
        self.play(
            Create(AO, run_time=2),
            Create(BO, run_time=2),
        )
        # #self.add(D)
        self.play(
            Create(OAB, run_time=2),
            FadeIn(D, D_text)
        )
        self.play(
            Uncreate(OAB, run_time=2)
        )
        # DX = ArcBetweenPoints(D.get_center(), [-6, 0.05, 0], radius=3).set_stroke(width=2.5)
        # XB = ArcBetweenPoints([-6, -0.1, 0], [B.get_x(), B.get_y() + 0.01, 0], radius=4).set_stroke(width=2.5)
        AD = DashedVMobject(ArcBetweenPoints(A.get_center(), D.get_center(), radius=3).set_stroke(width=2.5))
        DB = DashedVMobject(ArcBetweenPoints(D.get_center(), B.get_center(), radius=2).set_stroke(width=2.5))
        # DX_dashed = DashedVMobject(DX, num_dashes=10)
        # XB_dashed = DashedVMobject(XB, num_dashes=10)
        self.wait(1)
        self.play(
            Create(AD, run_time=2),
            Create(DB, run_time=2),
            # Create(DX_dashed, run_time=2),
            # Create(XB_dashed, run_time=2)
        )

        text2 = MathTex(
            r"\angle{DAB}=\angle{CBA}\\",
            r"\angle{DBA}=\angle{CAB}"
        ).shift(RIGHT*3.3)
        DAB_angle = Angle(
            Line(A.get_center(), [-4, 2.1, 0]),
            Line(A.get_center(), [-3.6, 1.75, 0]),
            radius=1
        )
        CBA_angle =Angle(
            Line(B.get_center(), [-5.03, -1.3, 0]),
            Line(B.get_center(), [-4.5, -1.87, 0]),
            other_angle=True,
            radius=0.45
        )
        DBA_angle =Angle(
            Line(B.get_center(), [-4.67, -0.77, 0]),
            Line(B.get_center(), [-4.99, -1.3, 0]),
            radius=1
        )
        CAB_angle =Angle(
            Line(A.get_center(), [-3.58, 2.35, 0]),
            Line(A.get_center(), [-2.4, 2.35, 0]),
        )
        self.play(
            Write(text2),
            Create(DAB_angle, run_time=2),
            Create(CBA_angle, run_time=2),
            Create(DBA_angle, run_time=2),
            Create(CAB_angle, run_time=2)
        )
        AB_arc = ArcBetweenPoints(a, b, radius=3, **arc_conf)
        CA_arc = ArcBetweenPoints(c, a, radius=3, **arc_conf)
        BC_arc = ArcBetweenPoints(b, c, radius=7, **arc_conf)
        poly_conf = {"stroke_width": 0, "stroke_color": WHITE,
                     "fill_opacity": 1, "color": WHITE}
        ABC = ArcPolygonFromArcs(AB_arc, CA_arc, BC_arc, **poly_conf)
        AD_arc = ArcBetweenPoints(A.get_center(), D.get_center(), radius=3).set_stroke(width=0)
        DB_arc = ArcBetweenPoints(D.get_center(), B.get_center(), radius=2).set_stroke(width=0)

        # DX_arc = DX.copy().set_stroke(width=0)
        # XB_arc = XB.copy().set_stroke(width=0)
        AB_arc =ArcBetweenPoints(A.get_center(), B.get_center(), radius=3).set_stroke(width=0)
        poly_conf1 = {"stroke_width": 0, "stroke_color": WHITE,
                     "fill_opacity": 0.75, "color": BLUE}
        ABD = ArcPolygonFromArcs(AD_arc, DB_arc, AB_arc, **poly_conf1)
        text3 = MathTex(r"\triangle{ABC}", r"=",r"\triangle{BAD}").shift(RIGHT*3).scale(1.3)
        text3[2].set_color(BLUE)

        DA_arc = ArcBetweenPoints(d, a, radius=3).set_stroke(width=0)
        BD_arc = ArcBetweenPoints(b, d, radius=2).set_stroke(width=0)
        AB_arc = ArcBetweenPoints(a, b, radius=3).set_stroke(width=0)
        poly_conf1 = {"stroke_width": 0, "stroke_color": WHITE,
                     "fill_opacity": 1, "color": BLUE}
        ABD = ArcPolygonFromArcs(AB_arc, DA_arc, BD_arc, **poly_conf1)

        poly_conf2 = {"stroke_width": 0, "stroke_color": WHITE,
                      "fill_opacity": 1, "color": WHITE}
        DC_arc = ArcBetweenPoints(D.get_center(), C.get_center(), radius=3).set_stroke(width=0)
        CA_arc = ArcBetweenPoints(C.get_center(), A.get_center(), radius=3).set_stroke(width=0)
        AD_arc = ArcBetweenPoints(A.get_center(), D.get_center(), radius=2).set_stroke(width=0)
        ADC = ArcPolygonFromArcs(AD_arc, DC_arc, CA_arc, **poly_conf2)

        poly_conf3 = {"stroke_width": 0, "stroke_color": WHITE,
                      "fill_opacity": 1, "color": WHITE}
        CD_arc1 = ArcBetweenPoints(C.get_center(), D.get_center(), radius=3).set_stroke(width=0)
        DB_arc1 = ArcBetweenPoints(D.get_center(), B.get_center(), radius=3).set_stroke(width=0)
        BC_arc1 = ArcBetweenPoints(B.get_center(), C.get_center(), radius=7.5).set_stroke(width=0)
        BDC = ArcPolygonFromArcs(DB_arc1, CD_arc1, BC_arc1, **poly_conf3)
        #self.wait(1)
        self.play(
            Create(ABD, run_time=2),
            Create(ADC, run_time=2),
            Create(BDC, run_time=2),
            #Create(ABC, run_time=2),
            FadeIn(D, D_text.set_color(BLACK)),
            ReplacementTransform(text2, text3),
        )
        self.wait(1)
        self.play(ABD.animate.set_fill(color=WHITE, opacity=1))
        self.wait(1)
        self.remove(BDC, ADC, ABD)
        self.add(ABC)
        self.play(
            D_text.animate.set_color(WHITE),
            FadeOut(ABC)
        )
        self.wait(1)
        # DX_ex = DX.copy().set_color(GREEN)
        # XB_ex = XB.copy().set_color(GREEN)
        DB_ex = DB.copy().set_color(GREEN)
        AC_ex = CA.copy().set_color(YELLOW)
        AD_ex = DashedVMobject(ArcBetweenPoints(A.get_center(), D.get_center(), radius=3).set_stroke(width=2).set_color(BLUE))
        BC_ex = BC.copy().set_color(PINK)
        text4 = MathTex(
            r"BD", r"=", r"AC", r"\\", r"AD", r"=", r"BC"
        ).shift(3.3*RIGHT).scale(1.3)
        text4[0].set_color(GREEN)
        text4[2].set_color(YELLOW)
        text4[4].set_color(BLUE)
        text4[6].set_color(PINK)
        self.play(
            ReplacementTransform(text3, text4),
            Create(AC_ex, run_time=2),
            Create(AD_ex, run_time=2),
            Create(BC_ex, run_time=2),
            Create(DB_ex, run_time=2)
        )
        self.play(FadeOut(CBA_angle, DBA_angle, CAB_angle, DAB_angle))
        DBC_angle = Angle(
            Line(B.get_center(), [B.copy().get_x(), B.copy().get_y() + 0.01, 0]),
            Line(B.get_center(), [B.copy().get_x() + 0.15, B.copy().get_y() - 0.031, 0]),
            radius=0.3,
            other_angle=True
        )
        ACB_angle = Angle(
            Line(C.get_center(), [C.copy().get_x() - 0.25, C.copy().get_y() - 0.06, 0]),
            Line(C.get_center(), [C.copy().get_x()+0.045, C.copy().get_y()+0.1, 0]),
            radius=0.3,
            other_angle=True
        )
        DAC_angle = Angle(
            Line(A.get_center(), [-3.39, 2.15, 0]),
            Line(A.get_center(), [-2.4, 2.3, 0]),
            #other_angle=True
        )
        self.wait(1)
        text5 = MathTex(r"\angle{DAC}=\angle{DBC}=\angle{ACB}").shift(RIGHT*3.4)
        self.play(
            FadeOut(AC_ex, AD_ex, BC_ex, DB_ex),
            FadeIn(DBC_angle, ACB_angle, DAC_angle),
            ReplacementTransform(text4, text5)
        )
        #CD_ex = ArcBetweenPoints(C.get_center(), D.get_center(), radius=3).set_stroke(width=2).set_color(BLUE)
        self.wait(1)
        CD = DashedVMobject(ArcBetweenPoints(C.get_center(), D.get_center(), radius=3).set_stroke(width=2))
        self.play(
            Create(CD, run_time=2),
            FadeOut(DBC_angle, ACB_angle, DAC_angle),
            FadeOut(O, O_text, AO, BO)
        )
        AB_arc = ArcBetweenPoints(a, b, radius=3, **arc_conf)
        CA_arc = ArcBetweenPoints(c, a, radius=3, **arc_conf)
        BC_arc = ArcBetweenPoints(b, c, radius=7, **arc_conf)
        poly_conf = {"stroke_width": 0, "stroke_color": WHITE,
                     "fill_opacity": 1, "color": WHITE}
        ABC = ArcPolygonFromArcs(AB_arc, CA_arc, BC_arc, **poly_conf)

        DA_arc = ArcBetweenPoints(d, a, radius=3).set_stroke(width=0)
        BD_arc = ArcBetweenPoints(b, d, radius=2).set_stroke(width=0)
        AB_arc = ArcBetweenPoints(a, b, radius=3).set_stroke(width=0)
        poly_conf1 = {"stroke_width": 0, "stroke_color": WHITE,
                     "fill_opacity": 1, "color": BLUE}
        ABD = ArcPolygonFromArcs(AB_arc, DA_arc, BD_arc, **poly_conf1)

        poly_conf2 = {"stroke_width": 0, "stroke_color": WHITE,
                      "fill_opacity": 1, "color": RED}
        DC_arc = ArcBetweenPoints(D.get_center(), C.get_center(), radius=3).set_stroke(width=0)
        CA_arc = ArcBetweenPoints(C.get_center(), A.get_center(), radius=3).set_stroke(width=0)
        AD_arc = ArcBetweenPoints(A.get_center(), D.get_center(), radius=2).set_stroke(width=0)
        ADC = ArcPolygonFromArcs(AD_arc, DC_arc, CA_arc, **poly_conf2)

        poly_conf3 = {"stroke_width": 0, "stroke_color": WHITE,
                      "fill_opacity": 1, "color": YELLOW}
        CD_arc1 = ArcBetweenPoints(C.get_center(), D.get_center(), radius=3).set_stroke(width=0)
        DB_arc1 = ArcBetweenPoints(D.get_center(), B.get_center(), radius=3).set_stroke(width=0)
        BC_arc1 = ArcBetweenPoints(B.get_center(), C.get_center(), radius=7.5).set_stroke(width=0)
        BDC = ArcPolygonFromArcs(DB_arc1, CD_arc1, BC_arc1, **poly_conf3)
        text6 = MathTex(
            r"\triangle{CDA}", r"=", r"\triangle{DCB}", r"=",
            r"\triangle{BAD}", r"=", r"\triangle{ABC}",

        ).shift(RIGHT*3.5).scale(0.75)
        text6[0].set_color(RED)
        text6[2].set_color(YELLOW)
        text6[4].set_color(BLUE)
        text6[6].set_color(WHITE)
        self.wait(1)
        self.play(
            ReplacementTransform(text5, text6[:5]),
            Create(ABD, run_time=2),
            Create(ADC, run_time=2),
            Create(BDC, run_time=2),
            #Create(ABC, run_time=2),
            FadeIn(D, D_text.set_color(BLACK))
        )
        self.wait(1)
        self.play(
            Write(text6[5:]),
            Create(ABC, run_time=2),
        )
        self.wait(1)
        self.play(Uncreate(ABC, run_time=2))

        # self.wait(1)
        #self.add(NumberPlane())
        self.wait(1)