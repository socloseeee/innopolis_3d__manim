from manim import *
import numpy as mp


class ExpancionAndSections(ThreeDScene):
    def construct(self):
        #self.add(NumberPlane())

        #Круги
        circle_in = Circle(radius=3, color=GREY)
        circle_in.set_stroke(width=2)
        circle_out = Circle(radius=1.5, color=GREY)
        circle_out.set_stroke(width=2.2)

        #Центр окружностей
        O = Dot([0, 0, 0], color=GREY).scale(0.85)
        O.set_stroke(color=WHITE, width=1)

        # Правильный многоугольник
        regular_polygon = RegularPolygon(n=7, color=DARK_BLUE).scale(1.67).shift(UP*0.037)
        regular_polygon.set_stroke(width=2)

        # Точки правильного многоугольника
        A_polygon_dot = Dot(regular_polygon.get_all_points()[0], color=GREY).scale(0.85)
        A_polygon_dot.set_stroke(color=WHITE, width=1)
        B_polygon_dot = Dot(regular_polygon.get_all_points()[3], color=GREY).scale(0.85)
        B_polygon_dot.set_stroke(color=WHITE, width=1)
        C_polygon_dot = Dot(regular_polygon.get_all_points()[7], color=GREY).scale(0.85)
        C_polygon_dot.set_stroke(color=WHITE, width=1)
        D_polygon_dot = Dot(regular_polygon.get_all_points()[11], color=GREY).scale(0.85)
        D_polygon_dot.set_stroke(color=WHITE, width=1)
        E_polygon_dot = Dot(regular_polygon.get_all_points()[15], color=GREY).scale(0.85)
        E_polygon_dot.set_stroke(color=WHITE, width=1)
        F_polygon_dot = Dot(regular_polygon.get_all_points()[19], color=GREY).scale(0.85)
        F_polygon_dot.set_stroke(color=WHITE, width=1)
        G_polygon_dot = Dot(regular_polygon.get_all_points()[23], color=GREY).scale(0.85)
        G_polygon_dot.set_stroke(color=WHITE, width=1)

        # Перпендикуляры
        perp_dot_1 = Dot(Line(A_polygon_dot.get_center(), B_polygon_dot.get_center()).get_center(), radius=0)
        perp_1 = Line(O.get_center(), perp_dot_1.get_center(), color=GREY).set_stroke(width=2)
        perp_dot_2 = Dot(Line(B_polygon_dot.get_center(), C_polygon_dot.get_center()).get_center(), radius=0)
        perp_2 = Line(O.get_center(), perp_dot_2.get_center(), color=GREY).set_stroke(width=2)
        perp_dot_3 = Dot(Line(C_polygon_dot.get_center(), D_polygon_dot.get_center()).get_center(), radius=0)
        perp_3 = Line(O.get_center(), perp_dot_3.get_center(), color=GREY).set_stroke(width=2)
        perp_dot_4 = Dot(Line(D_polygon_dot.get_center(), E_polygon_dot.get_center()).get_center(), radius=0)
        perp_4 = Line(O.get_center(), perp_dot_4.get_center(),color=GREY).set_stroke(width=2)
        perp_dot_5 = Dot(Line(E_polygon_dot.get_center(), F_polygon_dot.get_center()).get_center(), radius=0)
        perp_5 = Line(O.get_center(), perp_dot_5.get_center(),color=GREY).set_stroke(width=2)
        perp_dot_6 = Dot(Line(F_polygon_dot.get_center(), G_polygon_dot.get_center()).get_center(), radius=0)
        perp_6 = Line(O.get_center(), perp_dot_6.get_center(),color=GREY).set_stroke(width=2)
        perp_dot_7 = Dot(Line(G_polygon_dot.get_center(), A_polygon_dot.get_center()).get_center(), radius=0)
        perp_7 = Line(O.get_center(), perp_dot_7.get_center(), color=GREY).set_stroke(width=2)

        # Углы
        Angle_1 = RightAngle(
            Line(perp_dot_1.get_center(), A_polygon_dot.get_center()),
            Line(perp_dot_1.get_center(), O.get_center())
        ).scale(0.85).set_stroke(width=2)
        Angle_2 = RightAngle(
            Line(perp_dot_2.get_center(), B_polygon_dot.get_center()),
            Line(perp_dot_2.get_center(), O.get_center())
        ).scale(0.85).set_stroke(width=2)
        Angle_3 = RightAngle(
            Line(perp_dot_3.get_center(), C_polygon_dot.get_center()),
            Line(perp_dot_3.get_center(), O.get_center())
        ).scale(0.85).set_stroke(width=2)
        Angle_4 = RightAngle(
            Line(perp_dot_4.get_center(), D_polygon_dot.get_center()),
            Line(perp_dot_4.get_center(), O.get_center())
        ).scale(0.85).set_stroke(width=2)
        Angle_5 = RightAngle(
            Line(perp_dot_5.get_center(), E_polygon_dot.get_center()),
            Line(perp_dot_5.get_center(), O.get_center())
        ).scale(0.85).set_stroke(width=2)
        Angle_6 = RightAngle(
            Line(perp_dot_6.get_center(), F_polygon_dot.get_center()),
            Line(perp_dot_6.get_center(), O.get_center())
        ).scale(0.85).set_stroke(width=2)
        Angle_7 = RightAngle(
            Line(perp_dot_7.get_center(), G_polygon_dot.get_center()),
            Line(perp_dot_7.get_center(), O.get_center())
        ).scale(0.85).set_stroke(width=2)

        # Продолжение перпендикуляров
        star_dot_1 = Dot([perp_dot_1.get_x() * 2, perp_dot_1.get_y() * 2, 0], color=DARK_BLUE).scale(0.85)
        star_dot_1.set_stroke(color=WHITE, width=1)
        cont_perp_1 = Line(
            perp_dot_1.get_center(), star_dot_1.get_center(), color=GREY
        ).set_stroke(width=2)
        star_dot_2 = Dot([perp_dot_2.get_x() * 2, perp_dot_2.get_y() * 2, 0], color=DARK_BLUE).scale(0.85)
        star_dot_2.set_stroke(color=WHITE, width=1)
        cont_perp_2 = Line(
            perp_dot_2.get_center(), star_dot_2.get_center(), color=GREY
        ).set_stroke(width=2)
        star_dot_3 = Dot([perp_dot_3.get_x() * 2, perp_dot_3.get_y() * 2, 0], color=DARK_BLUE).scale(0.85)
        star_dot_3.set_stroke(color=WHITE, width=1)
        cont_perp_3 = Line(
            perp_dot_3.get_center(), star_dot_3.get_center(), color=GREY
        ).set_stroke(width=2)
        star_dot_4 = Dot([perp_dot_4.get_x() * 2, perp_dot_4.get_y() * 2, 0], color=DARK_BLUE).scale(0.85)
        star_dot_4.set_stroke(color=WHITE, width=1)
        cont_perp_4 = Line(
            perp_dot_4.get_center(), star_dot_4.get_center(), color=GREY
        ).set_stroke(width=2)
        star_dot_5 = Dot([perp_dot_5.get_x() * 2, perp_dot_5.get_y() * 2, 0], color=DARK_BLUE).scale(0.85)
        star_dot_5.set_stroke(color=WHITE, width=1)
        cont_perp_5 = Line(
            perp_dot_5.get_center(), star_dot_5.get_center(), color=GREY
        ).set_stroke(width=2)
        star_dot_6 = Dot([perp_dot_6.get_x() * 2, perp_dot_6.get_y() * 2, 0], color=DARK_BLUE).scale(0.85)
        star_dot_6.set_stroke(color=WHITE, width=1)
        cont_perp_6 = Line(
            perp_dot_6.get_center(), star_dot_6.get_center(), color=GREY
        ).set_stroke(width=2)
        star_dot_7 = Dot([perp_dot_7.get_x() * 2, perp_dot_7.get_y() * 2, 0], color=DARK_BLUE).scale(0.85)
        star_dot_7.set_stroke(color=WHITE, width=1)
        cont_perp_7 = Line(
            perp_dot_7.get_center(), star_dot_7.get_center(), color=GREY
        ).set_stroke(width=2)

        # Делаем Звезду
        star_line1_l = Line(star_dot_1.get_center(), A_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line1_r = Line(star_dot_1.get_center(), B_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line2_l = Line(star_dot_2.get_center(), B_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line2_r = Line(star_dot_2.get_center(), C_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line3_l = Line(star_dot_3.get_center(), C_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line3_r = Line(star_dot_3.get_center(), D_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line4_l = Line(star_dot_4.get_center(), D_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line4_r = Line(star_dot_4.get_center(), E_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line5_l = Line(star_dot_5.get_center(), E_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line5_r = Line(star_dot_5.get_center(), F_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line6_l = Line(star_dot_6.get_center(), F_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line6_r = Line(star_dot_6.get_center(), G_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line7_l = Line(star_dot_7.get_center(), G_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)
        star_line7_r = Line(star_dot_7.get_center(), A_polygon_dot.get_center(), color=BLUE).set_stroke(width=2)

        star_tooth_1 = Polygon(star_line1_l.start, star_line1_l.end, star_line1_r.end).set_stroke(width=0)
        star_tooth_2 = Polygon(star_line2_l.start, star_line2_l.end, star_line2_r.end).set_stroke(width=0)
        star_tooth_3 = Polygon(star_line3_l.start, star_line3_l.end, star_line3_r.end).set_stroke(width=0)
        star_tooth_4 = Polygon(star_line4_l.start, star_line4_l.end, star_line4_r.end).set_stroke(width=0)
        star_tooth_5 = Polygon(star_line5_l.start, star_line5_l.end, star_line5_r.end).set_stroke(width=0)
        star_tooth_6 = Polygon(star_line6_l.start, star_line6_l.end, star_line6_r.end).set_stroke(width=0)
        star_tooth_7 = Polygon(star_line7_l.start, star_line7_l.end, star_line7_r.end).set_stroke(width=0)

        # Анотация к радиусам
        brace_r = Brace(
            Line(O.get_center(), perp_1.end),
            direction=Line(O.get_center(), perp_1.end).rotate(PI*1.5).get_unit_vector(),
            color=YELLOW
        ).set_stroke(width=0.01)
        brace_r_text = brace_r.get_tex("r").set_color(BLACK)
        brace_r_text_rectangle = SurroundingRectangle(brace_r_text, color=WHITE)
        brace_r_text_rectangle.set_fill(color=WHITE, opacity=1)
        brace_R = Brace(
            Line(perp_1.start, star_dot_1.get_center()),
            direction=Line(perp_1.start, star_dot_1.get_center()).rotate(PI/2).get_unit_vector(),
            color=YELLOW
        ).set_stroke(width=0.01)
        brace_R_text = brace_R.get_tex("R").set_color(BLACK)
        brace_R_text_rectangle = SurroundingRectangle(brace_R_text, color=WHITE)
        brace_R_text_rectangle.set_fill(color=WHITE, opacity=1)

        # Вся анимация
        all_anim_group = Group(
            circle_in, circle_out,
            regular_polygon,
            A_polygon_dot,
            B_polygon_dot,
            C_polygon_dot,
            D_polygon_dot,
            E_polygon_dot,
            F_polygon_dot,
            G_polygon_dot,
            O,
            perp_1,
            perp_2,
            perp_3,
            perp_4,
            perp_5,
            perp_6,
            perp_7,
            perp_dot_1,
            perp_dot_2,
            perp_dot_3,
            perp_dot_4,
            perp_dot_5,
            perp_dot_6,
            perp_dot_7,
            star_dot_1,
            star_dot_2,
            star_dot_3,
            star_dot_4,
            star_dot_5,
            star_dot_6,
            star_dot_7,
            cont_perp_1,
            cont_perp_2,
            cont_perp_3,
            cont_perp_4,
            cont_perp_5,
            cont_perp_6,
            cont_perp_7,
            star_line1_l,
            star_line1_r,
            star_line2_l,
            star_line2_r,
            star_line3_l,
            star_line3_r,
            star_line4_l,
            star_line4_r,
            star_line5_l,
            star_line5_r,
            star_line6_l,
            star_line6_r,
            star_line7_l,
            star_line7_r,
            star_tooth_1,
            star_tooth_2,
            star_tooth_3,
            star_tooth_4,
            star_tooth_5,
            star_tooth_6,
            star_tooth_7,
        )

        # Создание кругов
        self.play(
            Create(circle_in, run_time=2),
            Create(circle_out, run_time=2)
        )
        # Создание точек правильного многоугольника
        self.play(
            FadeIn(
                A_polygon_dot,
                B_polygon_dot,
                C_polygon_dot,
                D_polygon_dot,
                E_polygon_dot,
                F_polygon_dot,
                G_polygon_dot
            )
        )
        # Создание многоугольника и точки центра окружности
        self.play(Create(regular_polygon, run_time=2))
        self.play(regular_polygon.animate.set_fill(color=BLUE, opacity=0.15))
        self.play(FadeIn(O))
        # Создание перпендикуляров из центра на внутреннюю окружность (+ показываем прямые углы)
        self.play(
            Create(perp_1, run_time=2),
            Create(perp_2, run_time=2),
            Create(perp_3, run_time=2),
            Create(perp_4, run_time=2),
            Create(perp_5, run_time=2),
            Create(perp_6, run_time=2),
            Create(perp_7, run_time=2),
        )
        self.play(
            Create(Angle_1, run_time=2),
            Create(Angle_2, run_time=2),
            Create(Angle_3, run_time=2),
            Create(Angle_4, run_time=2),
            Create(Angle_5, run_time=2),
            Create(Angle_6, run_time=2),
            Create(Angle_7, run_time=2)
        )
        self.play(
            Uncreate(Angle_1, run_time=2),
            Uncreate(Angle_2, run_time=2),
            Uncreate(Angle_3, run_time=2),
            Uncreate(Angle_4, run_time=2),
            Uncreate(Angle_5, run_time=2),
            Uncreate(Angle_6, run_time=2),
            Uncreate(Angle_7, run_time=2)
        )
        # Создаём точки для звезды (точки на которые продолжаются перпендикуляры)
        self.play(
            FadeIn(
                star_dot_1,
                star_dot_2,
                star_dot_3,
                star_dot_4,
                star_dot_5,
                star_dot_6,
                star_dot_7,
            )
        )
        # Продолжение перпендикуляров
        self.play(
            Create(cont_perp_1, run_time=2),
            Create(cont_perp_2, run_time=2),
            Create(cont_perp_3, run_time=2),
            Create(cont_perp_4, run_time=2),
            Create(cont_perp_5, run_time=2),
            Create(cont_perp_6, run_time=2),
            Create(cont_perp_7, run_time=2),
        )
        # Создание звезды и заполнение области цветом
        self.play(
            Create(star_line1_l, run_time=2),
            Create(star_line1_r, run_time=2),
            Create(star_line2_l, run_time=2),
            Create(star_line2_r, run_time=2),
            Create(star_line3_l, run_time=2),
            Create(star_line3_r, run_time=2),
            Create(star_line4_l, run_time=2),
            Create(star_line4_r, run_time=2),
            Create(star_line5_l, run_time=2),
            Create(star_line5_r, run_time=2),
            Create(star_line6_l, run_time=2),
            Create(star_line6_r, run_time=2),
            Create(star_line7_l, run_time=2),
            Create(star_line7_r, run_time=2),
        )
        self.play(
            star_tooth_1.animate.set_fill(color=BLUE, opacity=0.1),
            star_tooth_2.animate.set_fill(color=BLUE, opacity=0.1),
            star_tooth_3.animate.set_fill(color=BLUE, opacity=0.1),
            star_tooth_4.animate.set_fill(color=BLUE, opacity=0.1),
            star_tooth_5.animate.set_fill(color=BLUE, opacity=0.1),
            star_tooth_6.animate.set_fill(color=BLUE, opacity=0.1),
            star_tooth_7.animate.set_fill(color=BLUE, opacity=0.1),
        )
        # Создание анимации аннотации для радиусов
        self.play(
            FadeIn(brace_r, brace_R, brace_r_text_rectangle, brace_R_text_rectangle)
        )
        self.play(
            Write(brace_r_text), Write(brace_R_text),
        )
        self.wait(1)
        self.play(
            FadeOut(
                brace_r, brace_R, brace_r_text_rectangle, brace_R_text_rectangle, brace_r_text, brace_R_text
            )
        )
        # Двигаем всё для вывода текста
        self.play(all_anim_group.animate.shift(LEFT*3).scale(0.9))

        # Текст R > 2r
        text1 = MathTex(r"R",  r">",  r"2", r"r").shift(RIGHT*3)
        text1_rectangle = SurroundingRectangle(text1).set_stroke(width=2).set_color(WHITE)
        text1[0].set_color(YELLOW)
        text1[3].set_color(RED)
        R = Line(O.get_center(), star_dot_7.get_center(), color=YELLOW).set_stroke(width=2)
        r = Line(O.get_center(), perp_dot_1.get_center(), color=RED).set_stroke(width=2)

        # Анимация условия радиусов
        self.play(
            Create(R, run_time=2),
            Create(r, run_time=2),
            Write(text1, run_time=2)
        )
        self.play(Create(text1_rectangle, run_time=2))
        self.play(
            Uncreate(text1_rectangle, run_time=2),
            Uncreate(R, run_time=2),
            Uncreate(r, run_time=2),
        )

        # Первое условие
        text2 = MathTex(r"AB=AC").shift(RIGHT*3)
        star_side_1 = star_line1_l.copy()
        star_side_1.set_color(YELLOW)
        star_side_2 = star_line1_r.copy()
        star_side_2.set_color(YELLOW)
        star_dot_1_text = MathTex(r"A").next_to(star_dot_1, UP)
        star_dot_b = MathTex(r"C", color=BLACK).next_to(star_line1_l.get_all_points()[3], RIGHT)
        star_dot_b_rectangle = SurroundingRectangle(star_dot_b).set_stroke(width=2).set_color(WHITE)
        star_dot_b_rectangle.set_fill(color=WHITE, opacity=1)
        star_dot_c = MathTex(r"B", color=BLACK).next_to(star_line1_r.get_all_points()[3], LEFT)
        star_dot_c_rectangle = SurroundingRectangle(star_dot_c).set_stroke(width=2).set_color(WHITE)
        star_dot_c_rectangle.set_fill(color=WHITE, opacity=1)
        self.play(
            ReplacementTransform(text1, text2),
            FadeIn(star_dot_b_rectangle, star_dot_c_rectangle)
        )
        self.play(
            Create(star_side_1, run_time=2), Create(star_side_2, run_time=2),
            FadeIn(star_dot_1_text, star_dot_b, star_dot_c)
        )
        self.wait(1)
        self.play(
            Uncreate(star_side_1, run_time=2), Uncreate(star_side_2, run_time=2),
            FadeOut(
                star_dot_1_text, star_dot_b, star_dot_c, star_dot_b_rectangle, star_dot_c_rectangle
            )
        )

        # Cумма углов 360 градусов \circ
        text3 = MathTex(
            r"\alpha + \beta + \gamma + \delta + \theta + \lambda + \psi < 360^\circ"
        ).shift(RIGHT*3.3).scale(0.8)
        angle1 = Angle(
            star_line1_l,
            star_line1_r,
            other_angle=True
        )
        angle1_text = MathTex(r"\alpha", color=BLACK).next_to(angle1, DOWN + RIGHT*0.2)
        angle1_text_rectangle = SurroundingRectangle(angle1_text).set_stroke(width=0)
        angle1_text_rectangle.set_fill(color=WHITE, opacity=1)
        angle2 = Angle(
            star_line2_l,
            star_line2_r,
            other_angle=True
        )
        angle2_text = MathTex(r"\beta", color=BLACK).next_to(angle2, RIGHT)
        angle2_text_rectangle = SurroundingRectangle(angle2_text).set_stroke(width=0)
        angle2_text_rectangle.set_fill(color=WHITE, opacity=1)
        angle3 = Angle(
            star_line3_l,
            star_line3_r,
            other_angle=True
        )
        angle3_text = MathTex(r"\gamma", color=BLACK).next_to(angle3, RIGHT + UP)
        angle3_text_rectangle = SurroundingRectangle(angle3_text).set_stroke(width=0)
        angle3_text_rectangle.set_fill(color=WHITE, opacity=1)
        angle4 = Angle(
            star_line4_l,
            star_line4_r,
            other_angle=True
        )
        angle4_text = MathTex(r"\delta", color=BLACK).next_to(angle4, UP)
        angle4_text_rectangle = SurroundingRectangle(angle4_text).set_stroke(width=0)
        angle4_text_rectangle.set_fill(color=WHITE, opacity=1)
        angle5 = Angle(
            star_line5_l,
            star_line5_r,
            other_angle=True
        )
        angle5_text = MathTex(r"\theta", color=BLACK).next_to(angle5, UP + LEFT)
        angle5_text_rectangle = SurroundingRectangle(angle5_text).set_stroke(width=0)
        angle5_text_rectangle.set_fill(color=WHITE, opacity=1)
        angle6 = Angle(
            star_line6_l,
            star_line6_r,
            other_angle=True
        )
        angle6_text = MathTex(r"\lambda", color=BLACK).next_to(angle6, LEFT)
        angle6_text_rectangle = SurroundingRectangle(angle6_text).set_stroke(width=0)
        angle6_text_rectangle.set_fill(color=WHITE, opacity=1)
        angle7 = Angle(
            star_line7_l,
            star_line7_r,
            other_angle=True
        )
        angle7_text = MathTex(r"\psi", color=BLACK).next_to(angle7, DOWN + LEFT*0.1)
        angle7_text_rectangle = SurroundingRectangle(angle7_text).set_stroke(width=0)
        angle7_text_rectangle.set_fill(color=WHITE, opacity=1)
        self.play(
            FadeIn(
                angle1, angle2, angle3, angle4, angle5, angle6, angle7,
                angle1_text_rectangle, angle2_text_rectangle, angle3_text_rectangle, angle4_text_rectangle,
                angle5_text_rectangle, angle6_text_rectangle, angle7_text_rectangle
            )
        )
        self.play(
            ReplacementTransform(text2, text3),
            Write(angle1_text, run_time=2),
            Write(angle2_text, run_time=2),
            Write(angle3_text, run_time=2),
            Write(angle4_text, run_time=2),
            Write(angle5_text, run_time=2),
            Write(angle6_text, run_time=2),
            Write(angle7_text, run_time=2)
        )
        self.play(
            FadeOut(
                angle1, angle2, angle3, angle4, angle5, angle6, angle7,
                angle1_text_rectangle, angle2_text_rectangle, angle3_text_rectangle, angle4_text_rectangle,
                angle5_text_rectangle, angle6_text_rectangle, angle7_text_rectangle,
                angle1_text, angle2_text, angle3_text, angle4_text, angle5_text, angle6_text, angle7_text
            )
        )
        self.wait(1)

        line_1 = Line(O.get_center(), G_polygon_dot.get_center(), color=YELLOW).set_stroke(width=2)
        line_2 = Line(O.get_center(), A_polygon_dot.get_center(), color=YELLOW).set_stroke(width=2)
        angle_ = Angle(
            line_1,
            line_2,
        )
        line_3 = Line(star_dot_7.get_center(), G_polygon_dot.get_center(), color=RED)
        line_4 = Line(star_dot_7.get_center(), A_polygon_dot.get_center(), color=RED)
        angle1_ = Angle(
            line_3,
            line_4,
            other_angle=True
        )
        angle_text = MathTex(r"\varepsilon").next_to(angle_, UP)
        angle_text1 = MathTex(r"\omega").next_to(angle1_, DOWN)
        text4 = MathTex(
            r"\varepsilon = \omega, r = R - r \\ \varepsilon < \omega, r < R - r \\ \varepsilon > \omega, r > R - r"
        ).shift(RIGHT*3)

        self.play(
            Create(line_1, run_time=2), Create(line_2, run_time=2),
            Create(line_3, run_time=2), Create(line_4, run_time=2)
        )
        self.play(
            FadeIn(
                angle_, angle1_,
            )
        )
        self.play(
            ReplacementTransform(text3, text4),
            Write(angle_text, run_time=2),
            Write(angle_text1, run_time=2)
        )
        self.wait(1)

        text5 = MathTex(r"\varepsilon + \mu + \nu + \sigma + \xi + \varpi + \upsilon = 360^\circ").shift(RIGHT*3.3).scale(0.83)
        line_3_ = Line(O.get_center(), B_polygon_dot.get_center(), color=YELLOW).set_stroke(width=2)
        line_4_ = Line(O.get_center(), C_polygon_dot.get_center(), color=YELLOW).set_stroke(width=2)
        line_5 = Line(O.get_center(), D_polygon_dot.get_center(), color=YELLOW).set_stroke(width=2)
        line_6 = Line(O.get_center(), E_polygon_dot.get_center(), color=YELLOW).set_stroke(width=2)
        line_7 = Line(O.get_center(), F_polygon_dot.get_center(), color=YELLOW).set_stroke(width=2)
        Angle2 = Angle(
            line_2,
            line_3_,
            radius=0.5
        )
        Angle2_text = MathTex(r"\mu").next_to(Angle2, 0.5*UP + LEFT*0.1)
        Angle3 = Angle(
            line_3_,
            line_4_,
            radius=0.3
        )
        Angle3_text = MathTex(r"\nu").next_to(Angle3, 0.5*LEFT)
        Angle4 = Angle(
            line_4_,
            line_5,
            radius=0.4
        )
        Angle4_text = MathTex(r"\sigma").next_to(Angle4, 0.5*LEFT+DOWN*0.1)
        Angle5 = Angle(
            line_5,
            line_6,
            radius=0.3
        )
        Angle5_text = MathTex(r"\xi").next_to(Angle5, 0.5*DOWN)
        Angle6 = Angle(
            line_6,
            line_7,
            radius=0.4
        )
        Angle6_text = MathTex(r"\varpi").next_to(Angle6, 0.5*DOWN+RIGHT*0.1)
        Angle7 = Angle(
            line_7,
            line_1,
            radius=0.3
        )
        Angle7_text = MathTex(r"\upsilon").next_to(Angle7, 0.5*RIGHT)
        self.play(
            Uncreate(line_3, run_time=2), Uncreate(line_4, run_time=2),
            FadeOut(angle1_, angle_text1),
            Create(line_3_, run_time=2),
            Create(line_4_, run_time=2),
            Create(line_5, run_time=2),
            Create(line_6, run_time=2),
            Create(line_7, run_time=2),
        )
        self.play(
            ReplacementTransform(text4, text5),
            FadeIn(
                Angle2, Angle3, Angle4, Angle5, Angle6, Angle7,
                Angle2_text, Angle3_text, Angle4_text, Angle5_text, Angle6_text, Angle7_text
            )
        )


