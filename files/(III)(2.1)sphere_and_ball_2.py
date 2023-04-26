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


class sphere_and_ball_2(ThreeDScene, GetIntersections):
    def construct(self):
        # Точки | Dots
        A = Dot([4, -1.8, 0], color=RED).set_stroke(width=1.5, color=WHITE).scale(0.75)
        B = Dot([0, -2.8, 0], radius=0.05)
        C = Dot([-4, 1.2, 0], radius=0.05)
        D = Dot([-1, 3.2, 0], radius=0.05)

        # Подписываем и создаём анимаю для точки А | Sign and create animation for point A
        A_text = MarkupText('<i>S</i>', font_size=30).next_to(A, RIGHT)
        A_group = AnimationGroup(FadeIn(A_text, run_time=3), Create(A, run_time=2))

        # Лучи образующие трёхгранный угол | Rays forming a trihedral angle
        AC = Line([4, -1.8, 0], [-4, 1.2, 0], color=RED).set_stroke(width=2)        # AC
        AB = Line([4, -1.8, 0], [0, -2.8, 0], color=RED).set_stroke(width=2)        # AB
        AD = Line([4, -1.8, 0], [-1, 3.2, 0], color=RED).set_stroke(width=2)        # AD

        # Плоскости | Planes:
        ABC = Polygon([4, -1.8, 0], [0, -2.8, 0], [-4, 1.2, 0])
        ACD = Polygon([4, -1.8, 0], [-4, 1.2, 0], [-1, 3.2, 0])
        ABD = Polygon([4, -1.8, 0], [0, -2.8, 0], [-1, 3.2, 0])
        ABC.set_stroke(width=0)
        ACD.set_stroke(width=0)
        ABD.set_stroke(width=0)

        # Анимация лучей | Ray animation
        self.play(
            Create(AC, run_time=3),
            Create(AB, run_time=3),
            Create(AD, run_time=3),
        )
        self.wait(1)

        # Анимация создания и подписи точки А | Animation of creation and signature of point A
        self.play(A_group)

        circle = Circle.from_three_points(
            [1.8, 0.4, 0],
            AB.get_all_points()[2],
            [-1, -1, 0],
            color=GREEN
        ).set_stroke(width=2)
        ellips = DashedVMobject(
            Ellipse(
                color=GREEN,
                width=circle.radius*2,
                height=1,
            )
        ).set_stroke(width=2)
        ellips.set_x(circle.get_x())
        ellips.set_y(circle.get_y())
        O = Dot(circle.get_center(), color=PURPLE).set_stroke(width=1.5, color=WHITE).scale(0.75)
        O_text = MathTex(r"O").next_to(O, DOWN)

        Y, X = [
           Dot(
               color=DARK_BLUE
           ).set_stroke(
               width=1.5,
               color=WHITE
           ).scale(0.75).move_to(point) for point in
           self.get_intersections_between_two_vmobs(circle, AC)
        ]
        AX = Line(X.get_center(), A.get_center(), color=RED).set_stroke(width=2)
        XY = DashedLine(X.get_center(), Y.get_center(), color=RED).set_stroke(width=2)
        YC = Line(Y.get_center(), C.get_center(), color=RED).set_stroke(width=2)
        self.play(
            Create(circle, run_time=2),
            Create(ellips, run_time=2),
            AC.animate.become(XY),
        )
        self.play(
            Create(AX, run_time=2),
            Create(YC, run_time=2)
        )
        self.play(
            FadeIn(O, O_text),
        )

        self.play(
            Create(ABC.set_fill(BLUE, opacity=0.3), run_time=5),
            Create(ACD.set_fill(LIGHT_GREY, opacity=0.3), run_time=5),
            Create(ABD.set_fill(GREEN, opacity=0.3), run_time=5),
        )

        ellips_cutting = Ellipse(
            width=2.85,
            height=1
        )
        ellips_cutting.set_x(1)
        ellips_cutting.set_y(-1.05)
        ellips_cutting.rotate(60*DEGREES)
        ellips_cutting_dashed = DashedVMobject(ellips_cutting)

        dot1A = Dot(ellips_cutting.get_all_points()[0], color=BLUE).set_stroke(width=1.5,color=WHITE).scale(0.75)
        A1_text = MathTex(r"A").next_to(dot1A, UP)
        dot2B = Dot(ellips_cutting.get_all_points()[16], color=BLUE).set_stroke(width=1.5,color=WHITE).scale(0.75)
        B2_text = MathTex(r"B").next_to(dot2B, DOWN)
        dot3C = Dot(ellips_cutting.get_all_points()[21], color=BLUE).set_stroke(width=1.5,color=WHITE).scale(0.75)
        C3_text = MathTex(r"C").next_to(dot3C, DOWN)

        SO = DashedLine(A.get_center(), O.get_center(), color=RED).set_stroke(width=2)
        self.play(
            Create(ellips_cutting_dashed, run_time=2),
            Create(SO, run_time=2)
        )
        self.wait(1)
        self.play(
            FadeIn(
                dot1A, dot2B, dot3C,
                A1_text, B2_text, C3_text
            )
        )
        SA = Line(A.get_center(), dot1A.get_center()).set_stroke(width=2)
        SB = Line(A.get_center(), dot2B.get_center()).set_stroke(width=2)
        SC = Line(A.get_center(), dot3C.get_center()).set_stroke(width=2)

        X1 = [
            Dot(
                color=DARK_BLUE
            ).set_stroke(
                width=1.5,
                color=WHITE
            ).scale(0.75).move_to(point) for point in
            self.get_intersections_between_two_vmobs(circle, SA)
        ][0]
        X2 = [
            Dot(
                color=DARK_BLUE
            ).set_stroke(
                width=1.5,
                color=WHITE
            ).scale(0.75).move_to(point) for point in
            self.get_intersections_between_two_vmobs(circle, SB)
        ][0]
        X3 = [
            Dot(
                color=DARK_BLUE
            ).set_stroke(
                width=1.5,
                color=WHITE
            ).scale(0.75).move_to(point) for point in
            self.get_intersections_between_two_vmobs(circle, SC)
        ][0]
        SX1 = Line(X1.get_center(), A.get_center(), color=YELLOW).set_stroke(width=2)
        SX2 = Line(X2.get_center(), A.get_center(), color=YELLOW).set_stroke(width=2)
        SX3 = Line(X3.get_center(), A.get_center(), color=YELLOW).set_stroke(width=2)
        X1A = DashedLine(X1.get_center(), dot1A.get_center(), color=YELLOW).set_stroke(width=2)
        X2B = DashedLine(X2.get_center(), dot2B.get_center(), color=YELLOW).set_stroke(width=2)
        X3C = DashedLine(X3.get_center(), dot3C.get_center(), color=YELLOW).set_stroke(width=2)
        OA = DashedLine(O.get_center(), dot1A.get_center(), color=BLUE).set_stroke(width=2)
        OB = DashedLine(O.get_center(), dot2B.get_center(), color=BLUE).set_stroke(width=2)
        OC = DashedLine(O.get_center(), dot3C.get_center(), color=BLUE).set_stroke(width=2)

        SAO = RightAngle(
            Line(dot1A.get_center(), A.get_center()),
            Line(dot1A.get_center(), O.get_center())
        )
        SBO = RightAngle(
            Line(dot2B.get_center(), A.get_center()),
            Line(dot2B.get_center(), O.get_center())
        )
        SCO = RightAngle(
            Line(dot3C.get_center(), A.get_center()),
            Line(dot3C.get_center(), O.get_center())
        )
        text = MathTex(
            r"\angle{SAO} = 90^\circ\\",
            r"\angle{SBO} = 90^\circ\\",
            r"\angle{SCO} = 90^\circ\\"
        ).shift(RIGHT*3.6)
        self.wait(1)

        self.play(
            Group(
                A, A_text, AB, AX, XY, YC, AD, ABC, ACD, ABD, SO, AC, O, O_text,
                circle, ellips_cutting_dashed, ellips,
                dot1A, dot2B, dot3C, A1_text, B2_text, C3_text
                #SAO, SBO, SCO,
                #SX1, X1A, SX2, X2B, SX3, X3C
            ).animate.shift(LEFT*3)
        )
        Group(
            OA, OB, OC,
            SX1, X1A, SX2, X2B, SX3, X3C, ellips_cutting,
            SAO, SBO, SCO,
        ).shift(LEFT*3)

        self.wait(1)
        self.play(
            Create(SX1, run_time=2),
            Create(X1A, run_time=2),
            Create(OA, run_time=2)
        )
        self.play(
            Create(SAO),
            Write(text[0])
        )
        self.wait(1)
        self.play(
            Create(SX2, run_time=2),
            Create(X2B, run_time=2),
            Create(OB, run_time=2),
            Create(SX3, run_time=2),
            Create(X3C, run_time=2),
            Create(OC, run_time=2)
        )
        self.play(
            Create(SBO),
            Create(SCO),
            Write(text[1:])
        )
        SAO_triangle = Polygon(A.get_center(), dot1A.get_center(), O.get_center()).set_stroke(width=0).set_fill(RED, opacity=0.7)
        SBO_triangle = Polygon(A.get_center(), dot2B.get_center(), O.get_center()).set_stroke(width=0).set_fill(YELLOW, opacity=0.7)
        SCO_triangle = Polygon(A.get_center(), dot3C.get_center(), O.get_center()).set_stroke(width=0).set_fill(BLUE, opacity=0.7)
        self.wait(1)
        self.play(
            Create(SAO_triangle, run_time=2),
            Create(SBO_triangle, run_time=2),
            Create(SCO_triangle, run_time=2),
        )
        self.play(
            Uncreate(SAO_triangle, run_time=2),
            Uncreate(SBO_triangle, run_time=2),
            Uncreate(SCO_triangle, run_time=2),
        )
        AO_ex = Line(O.get_center(), dot1A.get_center()).set_stroke(width=2).set_color(RED)
        BO_ex = Line(O.get_center(), dot2B.get_center()).set_stroke(width=2).set_color(YELLOW)
        CO_ex = Line(O.get_center(), dot3C.get_center()).set_stroke(width=2).set_color(BLUE)

        text1 = MathTex(r"AO", r"=", r"BO", r"=", r"CO", r"=r").shift(RIGHT*3.4).scale(1.3)
        text1[0].set_color(RED)
        text1[2].set_color(YELLOW)
        text1[4].set_color(BLUE)

        self.play(
            Create(AO_ex, run_time=2),
            Create(BO_ex, run_time=2),
            Create(CO_ex, run_time=2),
            ReplacementTransform(text, text1)
        )
        text2 = MathTex(r"\triangle{SAO}", r"=", r"\triangle{SBO}", r"=", r"\triangle{SCO}").shift(RIGHT * 3.4)
        text2[0].set_color(RED)
        text2[2].set_color(YELLOW)
        text2[4].set_color(BLUE)
        SAO_triangle_ex = Polygon(A.get_center(), dot1A.get_center(), O.get_center()).set_stroke(width=0).set_fill(RED, opacity=0.7)
        SBO_triangle_ex = Polygon(A.get_center(), dot2B.get_center(), O.get_center()).set_stroke(width=0).set_fill(YELLOW, opacity=0.7)
        SCO_triangle_ex = Polygon(A.get_center(), dot3C.get_center(), O.get_center()).set_stroke(width=0).set_fill(BLUE, opacity=0.7)
        self.play(
            Create(SAO_triangle_ex, run_time=2),
            Create(SBO_triangle_ex, run_time=2),
            Create(SCO_triangle_ex, run_time=2),
            Uncreate(AO_ex, run_time=2),
            Uncreate(BO_ex, run_time=2),
            Uncreate(CO_ex, run_time=2),
            ReplacementTransform(text1, text2)
        )
        self.play(
            Uncreate(SAO_triangle_ex, run_time=2),
            Uncreate(SBO_triangle_ex, run_time=2),
            Uncreate(SCO_triangle_ex, run_time=2),
        )
        self.wait(1)
        AC = DashedLine(dot1A.get_center(), dot3C.get_center(), color=BLUE).set_stroke(width=2)

        SO_ex = DashedLine(A.get_center(), O.get_center(), color=WHITE).set_stroke(width=2)
        text3 = MathTex(r"SO", r"\perp", r"ABC").shift(RIGHT*3).scale(1.3)
        text3[2].set_color(PINK)
        ABC_triangle = Polygon(dot1A.get_center(), dot2B.get_center(), dot3C.get_center()).set_stroke(width=0).set_fill(PINK, opacity=0.7)
        self.play(
            ReplacementTransform(text2, text3),
            Create(SO_ex),
            Create(ABC_triangle, run_time=2)
        )
        text4 = MathTex(r"^\circ").shift(RIGHT*3.4).scale(3.2)
        text4.set_color(PINK)
        ellips_cutting.set_stroke(width=0)
        self.play(Uncreate(ABC_triangle, run_time=2),)
        self.play(
            ellips_cutting.animate.set_fill(PINK, opacity=0.7),
            ReplacementTransform(text3[-1], text4)
        )


        #self.add(NumberPlane())
        self.wait(1)

