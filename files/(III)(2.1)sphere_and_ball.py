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


class sphere_and_ball(ThreeDScene, GetIntersections):
    def construct(self):
        sphere = Sphere(radius=3)
        self.play(FadeIn(sphere, run_time=2))
        self.wait(1)
        #self.play(sphere.animate.rotate(45*DEGREES))
        self.play(
            # FadeIn(Dot([1, 2, 0])),
            Rotate(
                sphere,
                angle=(PI / 0.5),
                about_point=sphere.get_center(),
                axis=LEFT * 2,
                run_time=2
            )
        )
        circle = Circle(radius=3, arc_center=sphere.get_center()).set_stroke(width=2)
        ellips = DashedVMobject(
            Ellipse(
                color=RED,
                width=sphere.radius*2,
                height=1,
            )
        ).set_stroke(width=2)

        # arc_in = ArcBetweenPoints(
        #     [-3, 0, 0], [3, 0, 0],
        #     radius=sphere.radius+5.5,
        #     #angle=TAU/2
        # )
        # arc_out = DashedVMobject(
        #     ArcBetweenPoints(
        #         [3, 0, 0], [-3, 0, 0],
        #         radius=sphere.radius+5.5,
        #         #angle=TAU/3
        #     )
        # )
        self.play(FadeIn(circle))
        O = Dot(circle.get_center(), color=RED).set_stroke(width=1.5, color=WHITE).scale(0.75)
        self.play(FadeOut(sphere))
        self.play(FadeIn(O))
        self.play(
            # Create(arc_in, run_time=2),
            # Create(arc_out, run_time=2),
            Create(ellips, run_time=2),
        )
        #self.add(Dot(ellips.get_all_points()[40]))
        #ellips_dashed = DashedVMobject(Mobject().set_points(ellips.get_all_points()[40:59]))
        #self.play(Create(ellips_dashed))
        # Dot(ellips.get_all_points()[40])
        # Dot(ellips.get_all_points()[0])
        self.wait(1)
        r = Line(ORIGIN, [0, -3, 0], color=YELLOW).set_stroke(width=2)
        r_text = MathTex(r"2").next_to(r.get_center(), RIGHT)
        self.play(Create(r, run_time=2))
        self.play(FadeIn(r_text))
        ellips_cutting = Ellipse(
                width=3*sqrt(1.85),
                height=1,
                arc_center=1.5*(LEFT+UP),
                color=GREEN
            ).set_stroke(width=2)
        ellips_cutting.rotate(45*DEGREES)
        ellips_cutting_dashed = DashedVMobject(
            ellips_cutting
        )
        #ellips_cutting.set_fill(GREEN, opacity=0.3)

        self.play(Create(ellips_cutting_dashed))

        d = Line(ORIGIN, 1.5*(LEFT+UP), color=GREEN).set_stroke(width=2)
        d_text = MathTex(r"1").next_to(d.get_center(), RIGHT)

        self.wait(1)
        self.play(
            Create(d, run_time=2),
            FadeIn(d_text)
        )

        A, extra1, extra2, B = [
            Dot(
                color=DARK_BLUE
            ).set_stroke(
                width=1.5,
                color=WHITE
            ).scale(0.75).move_to(point) for point in self.get_intersections_between_two_vmobs(circle, ellips_cutting)
        ][0:4]
        A_text = MathTex(r"A", color=WHITE).next_to(A, UP).scale(0.75)
        B_text = MathTex(r"B", color=WHITE).next_to(B, LEFT).scale(0.75)
        self.wait(1)
        self.play(FadeIn(A, B, A_text, B_text))

        AB_small = ArcBetweenPoints(
            A.get_center(),
            B.get_center(),
            radius=sphere.radius,
            color=YELLOW
        )
        self.play(Create(AB_small, run_time=2))
        self.play(Uncreate(AB_small, run_time=2))
        self.wait(1)
        ellips_cutting.set_stroke(width=0)
        self.play(ellips_cutting.animate.set_fill(BLUE, opacity=0.5))
        self.wait(1)
        AB_big = Arc(
            arc_center=[-0.05, 0.05, 0],
            radius=sphere.radius,
            color=YELLOW,
            start_angle=1.99*PI,
            angle=PI*1.52
        )
        AB_big.rotate(180*DEGREES)
        self.play(Create(AB_big, run_time=2))
        self.play(Uncreate(AB_big, run_time=2))
        self.wait(1)
        O_text = MathTex(r"O", color=WHITE).next_to(O, RIGHT).scale(0.75)
        self.play(FadeIn(O_text))
        self.play(
            FadeOut(ellips_cutting_dashed, ellips_cutting, ellips)
        )
        self.wait(1)
        AB = Line(A.get_center(), B.get_center(), color=BLUE).set_stroke(width=2)
        d_new = Line(
            ORIGIN,
            line_intersection(
                [ORIGIN, 2*(LEFT+UP)],
                [A.get_center(), B.get_center()]
            ),
            color=GREEN
        ).set_stroke(width=2)
        self.play(Create(AB, run_time=2),
                  d.animate.become(d_new))
        self.wait(1)
        self.play(Group(circle, AB, A, B, A_text, B_text, r, r_text, d_new, d, d_text, O, O_text).animate.shift(LEFT*3))
        text = MathTex(r"\cap",r"AB",  r"=", r"120^\circ").shift(RIGHT*3.5).scale(1.75)
        self.wait(1)
        AB_ex = ArcBetweenPoints(
            A.get_center(),
            B.get_center(),
            radius=circle.radius,
            color=YELLOW
        )
        self.play(Write(text), Create(AB_ex, run_time=2))
        self.wait(1)
        text1 = MathTex(r"\frac{4\pi}{3}").shift(RIGHT*4).scale(2)
        self.play(ReplacementTransform(text[-1], text1.shift(RIGHT*1.15)))
