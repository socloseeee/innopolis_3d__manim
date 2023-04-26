from manim import *
import numpy as mp


class ExpancionAndSections(ThreeDScene):
    def construct(self):
        cube = Cube()
        cube.generate_points()
        cube.set_fill(opacity=0)
        cube.set_stroke(width=2)
        #cube[1].set_fill(GREEN, opacity=1)
        cube.rotate_about_origin(38 * DEGREES)

        #line_1 = Line(cube[1].get_all_points()[0], cube[1].get_center())
        #line_2 = Line(cube[1].get_all_points()[3], cube[1].get_center())
        #line_3 = Line(cube[1].get_all_points()[7], cube[1].get_center())
        #line_4 = Line(cube[1].get_all_points()[11], cube[1].get_center())

        triangle_1 = Polygon(cube[1].get_all_points()[0], cube[1].get_center(), cube[1].get_all_points()[3],
                             color=WHITE)
        triangle_1.set_fill(GREEN, opacity=0.4)
        cube[4].set_fill(GREEN, opacity=0.4)
        triangle_1.set_stroke(width=2)
        green_side = cube[4].copy()
        green_side.set_stroke(width=2)
        triangle_2 = Polygon(cube[1].get_all_points()[3], cube[1].get_center(), cube[1].get_all_points()[7],
                             color=WHITE)
        triangle_2.set_fill(YELLOW, opacity=0.4)
        triangle_2.set_stroke(width=2)
        cube[3].set_fill(YELLOW, opacity=0.4)
        yellow_side = cube[3].copy()
        yellow_side.set_stroke(width=2)
        triangle_3 = Polygon(cube[1].get_all_points()[7], cube[1].get_center(), cube[1].get_all_points()[11],
                             color=WHITE)
        triangle_3.set_fill(RED, opacity=0.4)
        triangle_3.set_stroke(width=2)
        cube[5].set_fill(RED, opacity=0.4)
        red_side = cube[5].copy()
        red_side.set_stroke(width=2)
        triangle_4 = Polygon(cube[1].get_all_points()[11], cube[1].get_center(), cube[1].get_all_points()[0],
                             color=WHITE)
        triangle_4.set_fill(DARK_BLUE, opacity=0.4)
        triangle_4.set_stroke(width=2)
        cube[2].set_fill(DARK_BLUE, opacity=0.4)
        blue_side = cube[2].copy()
        blue_side.set_stroke(width=2)

        red_part = Group(triangle_3, red_side)
        yellow_part = Group(triangle_2, yellow_side)
        green_part = Group(triangle_1, green_side)
        blue_part = Group(triangle_4, blue_side)

        about_line_r = Line(cube[5].get_all_points()[11] , cube[5].get_all_points()[7], color=WHITE)
        about_line_r.set_stroke(width=2)
        about_line_y = Line(cube[3].get_all_points()[7] , cube[3].get_all_points()[3], color=WHITE)
        about_line_y.set_stroke(width=2)
        about_line_g = Line(cube[4].get_all_points()[3], cube[4].get_all_points()[0], color=WHITE)
        about_line_g.set_stroke(width=2)
        about_line_b = Line(cube[2].get_all_points()[0], cube[2].get_all_points()[11], color=WHITE)
        about_line_b.set_stroke(width=2)
        red_part.add(about_line_r)
        yellow_part.add(about_line_y)
        green_part.add(about_line_g)
        blue_part.add(about_line_b)

        self.move_camera(phi=30 * DEGREES, theta=0 * DEGREES, distance=6)
        self.play(Create(cube))
        # self.play(
        #     Create(line_1, run_time=2),
        #     Create(line_2, run_time=2),
        #     Create(line_3, run_time=2),
        #     Create(line_4, run_time=2)
        # )
        self.play(
            Create(triangle_1),
            Create(triangle_2),
            Create(triangle_3),
            Create(triangle_4)
        )
        # self.play(
        #     Create(about_line_r, run_time=2),
        #     Create(about_line_y, run_time=2),
        #     Create(about_line_g, run_time=2),
        #     Create(about_line_b, run_time=2)
        # )
        #self.add(red_part)

        self.add(red_part, green_part, yellow_part, blue_part)
        self.remove(cube)
        self.play(
            Rotate(
                red_part,
                angle=PI/2,
                about_point=about_line_r.get_center(),
                axis=RIGHT*2 + UP*1.55,
                run_time=2
            ),
            Rotate(
                yellow_part,
                angle=PI / 2,
                about_point=about_line_y.get_center(),
                axis=LEFT*2 + UP * 2.56,
                run_time=2
            ),
            Rotate(
                green_part,
                angle=PI / 2,
                about_point=about_line_g.get_center(),
                axis=LEFT * 2 + DOWN * 1.55,
                run_time=2
            ),
            Rotate(
                blue_part,
                angle=PI / 2,
                about_point=about_line_b.get_center(),
                axis=RIGHT * 2 + DOWN * 2.56,
                run_time=2
            ),
        )
        self.play(
            Rotate(
                red_part[0],
                angle=PI / 2,
                about_point=[red_part[0].get_all_points()[0][0], red_part[0].get_all_points()[0][1],
                             red_part[0].get_all_points()[0][2]],
                axis=RIGHT * 2 + UP * 1.55,
                #run_time=2
            ),
            Rotate(
                yellow_part[0],
                angle=PI / 2,
                about_point=[yellow_part[0].get_all_points()[0][0], yellow_part[0].get_all_points()[0][1],
                             yellow_part[0].get_all_points()[0][2]],
                axis=LEFT * 2 + UP * 2.56,
                #run_time=2
            ),
            Rotate(
                green_part[0],
                angle=PI / 2,
                about_point=[green_part[0].get_all_points()[0][0], green_part[0].get_all_points()[0][1],
                             green_part[0].get_all_points()[0][2]],
                axis=LEFT * 2 + DOWN * 1.55,
                #run_time=2
            ),
            Rotate(
                blue_part[0],
                angle=PI / 2,
                about_point=[blue_part[0].get_all_points()[0][0], blue_part[0].get_all_points()[0][1],
                             blue_part[0].get_all_points()[0][2]],
                axis=RIGHT * 2 + DOWN * 2.56,
                #run_time=2
            )
        )
        all_3d_mobject = Group(blue_part, red_part, green_part, yellow_part)

        #self.add(NumberPlane())
        #self.add(Dot([1, 2, 0]))
        self.wait(1)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, distance=6)
        self.play(all_3d_mobject.animate.rotate(7.1 * DEGREES))
        self.wait(1)

        cuad_1_A = Dot(red_side.get_all_points()[11], color=RED)
        cuad_1_A.set_stroke(color=WHITE, width=1)
        cuad_1_B = Dot(yellow_side.get_all_points()[7], color=RED)
        cuad_1_B.set_stroke(color=WHITE, width=1)
        cuad_1_C = Dot(green_side.get_all_points()[3], color=RED)
        cuad_1_C.set_stroke(color=WHITE, width=1)
        cuad_1_D = Dot(blue_side.get_all_points()[0], color=RED)
        cuad_1_D.set_stroke(color=WHITE, width=1)

        cuad_2_C = Dot(green_side.get_all_points()[7], color=RED)
        cuad_2_C.set_stroke(color=WHITE, width=1)
        cuad_2_D = Dot(green_side.get_all_points()[11], color=RED)
        cuad_2_D.set_stroke(color=WHITE, width=1)

        triangle_1_A = Dot(triangle_1.get_all_points()[3], color=RED)
        triangle_1_A.set_stroke(color=WHITE, width=1)

        cuad_3_C = Dot(yellow_side.get_all_points()[0], color=RED)
        cuad_3_C.set_stroke(color=WHITE, width=1)
        cuad_3_D = Dot(yellow_side.get_all_points()[11], color=RED)
        cuad_3_D.set_stroke(color=WHITE, width=1)

        triangle_2_A = Dot(triangle_2.get_all_points()[3], color=RED)
        triangle_2_A.set_stroke(color=WHITE, width=1)

        cuad_4_C = Dot(red_side.get_all_points()[0], color=RED)
        cuad_4_C.set_stroke(color=WHITE, width=1)
        cuad_4_D = Dot(red_side.get_all_points()[3], color=RED)
        cuad_4_D.set_stroke(color=WHITE, width=1)

        triangle_3_A = Dot(triangle_3.get_all_points()[3], color=RED)
        triangle_3_A.set_stroke(color=WHITE, width=1)

        cuad_5_C = Dot(blue_side.get_all_points()[3], color=RED)
        cuad_5_C.set_stroke(color=WHITE, width=1)
        cuad_5_D = Dot(blue_side.get_all_points()[7], color=RED)
        cuad_5_D.set_stroke(color=WHITE, width=1)

        triangle_4_A = Dot(triangle_4.get_all_points()[3], color=RED)
        triangle_4_A.set_stroke(color=WHITE, width=1)

        self.play(
            FadeIn(
                cuad_1_A, cuad_1_B, cuad_1_C, cuad_1_D,
                cuad_2_C, cuad_2_D,
                cuad_3_C, cuad_3_D,
                cuad_4_C, cuad_4_D,
                cuad_5_C, cuad_5_D,
                triangle_1_A, triangle_2_A, triangle_3_A, triangle_4_A
            )
        )
        cuad_1 = Polygon(
            red_side.get_all_points()[11],
            yellow_side.get_all_points()[7],
            green_side.get_all_points()[0],
            blue_side.get_all_points()[0],
            color=PURPLE
        )
        cuad_2 = Polygon([-1, 0, 0], [0, -1, 0], [-2, -1, 0], [-1, -2, 0])

        quadrat = Square(side_length=6, color=WHITE)
        quadrat.set_stroke(width=2)
        quadrat_A = Dot([quadrat.get_all_points()[0]], color=RED)
        quadrat_A.set_stroke(color=WHITE, width=1)
        quadrat_B = Dot([quadrat.get_all_points()[3]], color=RED)
        quadrat_B.set_stroke(color=WHITE, width=1)
        quadrat_C = Dot([quadrat.get_all_points()[7]], color=RED)
        quadrat_C.set_stroke(color=WHITE, width=1)
        quadrat_D = Dot([quadrat.get_all_points()[11]], color=RED)
        quadrat_D.set_stroke(color=WHITE, width=1)

        self.play(
            Create(quadrat),
            FadeIn(quadrat_A, quadrat_B, quadrat_C, quadrat_D)
        )

        self.play(
            triangle_1.animate.set_fill(opacity=0), green_side.animate.set_fill(opacity=0),
            triangle_2.animate.set_fill(opacity=0), yellow_side.animate.set_fill(opacity=0),
            triangle_3.animate.set_fill(opacity=0), red_side.animate.set_fill(opacity=0),
            triangle_4.animate.set_fill(opacity=0), blue_side.animate.set_fill(opacity=0)
        )

        all_3d_mobject.add(
            cuad_1_A, cuad_1_B, cuad_1_C, cuad_1_D,
            cuad_2_C, cuad_2_D,
            cuad_3_C, cuad_3_D,
            cuad_4_C, cuad_4_D,
            cuad_5_C, cuad_5_D,
            triangle_1_A, triangle_2_A, triangle_3_A, triangle_4_A,
            triangle_1, triangle_2, triangle_3, triangle_4,
            quadrat, quadrat_A, quadrat_B, quadrat_C, quadrat_D,
        )

        self.wait(1)
        self.play(all_3d_mobject.animate.scale(0.85))

        text1 = MathTex(r"2\sqrt{2}").move_to(UP*3.2)
        text2 = MathTex(r"2\sqrt{2}").move_to(LEFT*3.2)
        text3 = MathTex(r"2\sqrt{2}").move_to(RIGHT*3.2)
        text4 = MathTex(r"2\sqrt{2}").move_to(DOWN*3.2)
        self.play(
            Write(text1, run_time=2),
            Write(text2, run_time=2),
            Write(text3, run_time=2),
            Write(text4, run_time=2),
        )

        text5 = MathTex(r"2\sqrt{2} < 3").move_to(RIGHT*3.7)

        all_3d_mobject.add(text1, text2, text3, text4)
        self.play(
            all_3d_mobject.animate.shift(LEFT*2.5),
        )
        self.play(all_3d_mobject[-9:].animate.shift(RIGHT*0.107))
        self.wait(1)
        self.play(Write(text5, run_time=2))
        rectangle = SurroundingRectangle(text5, color=WHITE)
        rectangle.set_stroke(width=2)
        self.play(Create(rectangle, run_time=2))
        self.wait(1)
        self.play(Uncreate(rectangle, run_time=2))
        self.wait(1)
