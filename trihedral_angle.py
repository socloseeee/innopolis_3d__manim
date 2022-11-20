from manim import *
import numpy as np


class Corner(Scene):
    def construct(self):

        # Точки | Dots
        A = Dot([4, -1.8, 0], radius=0.05)
        #B = Dot([0, -2.8, 0], radius=0.05)
        #C = Dot([-4, 1.2, 0], radius=0.05)
        #D = Dot([-1, 3.2, 0], radius=0.05)

        # Подписываем и создаём анимаю для точки А | Sign and create animation for point A
        A_text = MarkupText('<i>A</i>', font_size=30).next_to(A, RIGHT)
        A_group = AnimationGroup(FadeIn(A_text, run_time=3), Create(A, run_time=2))

        # Лучи образующие трёхгранный угол | Rays forming a trihedral angle
        AC = Line([4, -1.8, 0], [-4, 1.2, 0], color=RED)        # AC
        AB = Line([4, -1.8, 0], [0, -2.8, 0], color=RED)        # AB
        AD = Line([4, -1.8, 0], [-1, 3.2, 0], color=RED)        # AD

        # Плоскости | Planes:
        ABC = Polygon([4, -1.8, 0], [0, -2.8, 0], [-4, 1.2, 0])
        ACD = Polygon([4, -1.8, 0], [-4, 1.2, 0], [-1, 3.2, 0])
        ABD = Polygon([4, -1.8, 0], [0, -2.8, 0], [-1, 3.2, 0])
        ABC.set_stroke(width=0)
        ACD.set_stroke(width=0)
        ABD.set_stroke(width=0)

        # Угол-альфа (Создание + анимация) | Angle-alpha (Creation + Animation)
        AC_AD_angle = Angle(AC, AD, radius=1.8, other_angle=True)
        AC_AD_angle_letter = MathTex(r"\alpha").next_to(AC_AD_angle, (LEFT * 0.9) + (0.0001 * UP))
        AC_AD_group = AnimationGroup(
            Create(AC_AD_angle, run_time=2),
            FadeIn(AC_AD_angle_letter, run_time=2)
        )

        # Угол-бетта (Создание + анимация) | Angle-betta (Creation + Animation)
        AB_AC_angle = Angle(AB, AC, radius=2.8, other_angle=True)
        AB_AC_angle_letter = MathTex(r"\beta").next_to(AB_AC_angle, LEFT * 0.9)
        AB_AC_group = AnimationGroup(
            Create(AB_AC_angle, run_time=2),
            FadeIn(AB_AC_angle_letter, run_time=2)
        )

        # Угол-гамма (Создание + анимация) | Angle-Gamma (Creation + Animation)
        AB_AD_angle = Angle(AB, AD, radius=0.8, other_angle=True)
        AB_AD_angle_letter = MathTex(r"\gamma").next_to(AB_AD_angle, LEFT * 0.9)
        AB_AD_group = AnimationGroup(
            Create(AB_AD_angle, run_time=2),
            FadeIn(AB_AD_angle_letter, run_time=2)
        )

        # Анимация лучей | Ray animation
        self.play(
            Create(AC, run_time=3),
            Create(AB, run_time=3),
            Create(AD, run_time=3),
        )
        self.wait(1)

        # Анимация выделения углов | Corner Selection Animation
        self.play(
            AC_AD_group,
            AB_AC_group,
            AB_AD_group,
        )
        self.wait(1)

        # Анимация создания и подписи точки А | Animation of creation and signature of point A
        self.play(A_group)

        # Удаляем луч AC, дабы создать объёмность впоследствии выделив при помощи анимации грани
        # Delete the AC ray in order to create three-dimensionality later by selecting the edges using animation
        self.play(FadeOut(AC, run_time=1))
        AC = DashedLine([4, -1.8, 0], [-4, 1.2, 0], color=RED)
        self.play(
            Create(ABC.set_fill(BLUE, opacity=0.3), run_time=5),
            Create(ACD.set_fill(GREEN, opacity=0.3), run_time=5),
            Create(ABD.set_fill(RED, opacity=0.3), run_time=5),
            Create(AC,run_time=3)
        )

        # Рассматриваем с позиции плоскости угла 𝛾 | View from the position of the angle plane 𝛾
        A_new = Dot([3, -2, 0], radius=0.05)
        A_text_new = MarkupText('<i>A</i>', font_size=30).next_to(A_new, RIGHT)
        A_group_new = AnimationGroup(FadeIn(A_text_new, run_time=3), Create(A_new, run_time=2))

        B_new = Dot([-3, -2, 0], radius=0.05)
        D_new = Dot([-1, 2, 0], radius=0.05)

        # Создаём анимацию выделения угла α и площади его покрытия
        # Create an animation of selecting the angle α and the area of its coverage
        ABD_new = Polygon(
            [A_new.get_x(), A_new.get_y(), 0],  # A
            [B_new.get_x(), B_new.get_y(), 0],  # B
            [D_new.get_x(), D_new.get_y(), 0])  # D
        ABD_new.set_fill(RED, opacity=0.3)
        ABD_new.set_stroke(RED)

        AB_AD_angle_new = Angle(
            Line([A_new.get_x(), A_new.get_y(), 0], [B_new.get_x(), B_new.get_y(), 0]),
            Line([A_new.get_x(), A_new.get_y(), 0], [D_new.get_x(), D_new.get_y(), 0]),
            radius=3, other_angle=True)
        AB_AD_angle_letter_new = MathTex(r"\gamma").next_to(AB_AD_angle_new, LEFT * 0.9)
        AB_AD_group_new = AnimationGroup(
            Create(AB_AD_angle_new, run_time=2),
            FadeIn(AB_AD_angle_letter_new, run_time=2)
        )

        # Сдвиг влево | Shift left
        self.play(Group(ABC, ACD, ABD, AC, AB, AD,
                  AC_AD_angle, AC_AD_angle_letter,
                  AB_AC_angle, AB_AC_angle_letter,
                  AB_AD_angle, AB_AD_angle_letter,
                  A, A_text
                  ).animate.shift(LEFT*3).scale(0.8))

        # Текст и его иллюстрация | Text and illustration
        a,b,c = 'α', 'β', 'γ'
        first_text = MarkupText(f'<i>{a} ≤ {b} ≤ {c}</i>').scale(0.8)
        self.wait(2)

        self.play(Write(first_text.shift(RIGHT*3 + UP)))
        self.wait(2)

        self.play(FadeOut(first_text, run_time=2))
        self.wait(2)

        # Сдвиг обратно в центр | Shift back to center
        self.play(Group(ABC, ACD, ABD, AC, AB, AD,
                        AC_AD_angle, AC_AD_angle_letter,
                        AB_AC_angle, AB_AC_angle_letter,
                        AB_AD_angle, AB_AD_angle_letter,
                        A, A_text
                        ).animate.shift(RIGHT * 3).scale(1.2))

        # Трансформация | Transformation
        self.play(ReplacementTransform(
            Group(ABC, ACD, ABD, AC, AB, AD,
                  AC_AD_angle, AC_AD_angle_letter,
                  AB_AC_angle, AB_AC_angle_letter,
                  AB_AD_angle, AB_AD_angle_letter,
                  A, A_text
                  ),
            ABD_new
        ), A_group_new
        )

        # Делим прямую BD на 10 равных частей для будущей проекции
        # Divide the line BD into 10 equal parts for the future projection
        BD_new_x = np.linspace(B_new.get_x(), D_new.get_x(), 10)
        BD_new_y = np.linspace(B_new.get_y(), D_new.get_y(), 10)

        # Угол β | Angle β
        ABC_new = Polygon(
            [A_new.get_x(), A_new.get_y(), 0],  # A
            [BD_new_x[6], BD_new_y[6], 0],      # B
            [B_new.get_x(), B_new.get_y(), 0])  # D
        ABC_new.set_fill(BLUE, opacity=0.3)
        ABC_new.set_stroke(width=0)

        # Создаём анимацию выделения угла β и площади его покрытия
        # Create an animation of selecting the angle β and the area of its coverage
        AB_AC_angle_new = Angle(
            Line([A_new.get_x(), A_new.get_y(), 0], [B_new.get_x(), B_new.get_y(), 0]),
            Line([A_new.get_x(), A_new.get_y(), 0], [BD_new_x[6], BD_new_y[6], 0]),
            radius=2.2, other_angle=True)
        AB_AC_angle_letter_new = MathTex(r"\beta'").next_to(AB_AC_angle_new, LEFT * 0.9)
        AB_AC_group_new = AnimationGroup(
            Create(AB_AC_angle_new, run_time=2),
            FadeIn(AB_AC_angle_letter_new, run_time=2)
        )

        # Угол α | Angle α
        ACD_new = Polygon(
            [A_new.get_x(), A_new.get_y(), 0],  # A
            [BD_new_x[4], BD_new_y[4], 0],      # B
            [B_new.get_x(), B_new.get_y(), 0])  # D
        ACD_new.set_fill(GREEN, opacity=0.3)
        ACD_new.set_stroke(width=0)

        # Создаём анимацию выделения угла α и площади его покрытия
        # Create an animation of selecting the angle β and the area of its coverage
        AC_AD_angle_new = Angle(
            Line([A_new.get_x(), A_new.get_y(), 0], [B_new.get_x(), B_new.get_y(), 0]),
            Line([A_new.get_x(), A_new.get_y(), 0], [BD_new_x[4], BD_new_y[4], 0]),
            radius=1.4, other_angle=True)
        AC_AD_angle_letter_new = MathTex(r"\alpha'").next_to(AC_AD_angle_new, LEFT * 0.9)
        AC_AD_group_new = AnimationGroup(
            Create(AC_AD_angle_new, run_time=2),
            FadeIn(AC_AD_angle_letter_new, run_time=2)
        )

        # Выделяем область ортоганальной проекции угла β | Select the area of the orthogonal projection of the angle β
        betta_dash_line = DashedLine([A_new.get_x(), A_new.get_y(), 0], [BD_new_x[6], BD_new_y[6], 0], color=RED)
        self.play(Create(betta_dash_line, run_time=1),
            Create(ABC_new, run_time=2)
        )

        # Выделяем область ортоганальной проекции угла α | Select the area of the orthogonal projection of the angle α
        alpha_dash_line = DashedLine([A_new.get_x(), A_new.get_y(), 0], [BD_new_x[4], BD_new_y[4], 0], color=RED)
        self.play(Create(alpha_dash_line, run_time=1),
                  Create(ACD_new, run_time=2)
                  )

        self.play(AB_AD_group_new)
        self.play(AB_AC_group_new)
        self.play(AC_AD_group_new)

        # Сдвиг влево | Shift left
        self.play(Group(
            A_new, A_text_new,
            ABD_new, AB_AD_angle_new, AB_AD_angle_letter_new,
            ABC_new, AB_AC_angle_new, AB_AC_angle_letter_new,
            ACD_new, AC_AD_angle_new, AC_AD_angle_letter_new,
            alpha_dash_line, betta_dash_line
        ).animate.shift(LEFT*3).scale(0.8))
        self.wait(1)

        show_ABC = ABC_new.copy()
        show_ACD = ACD_new.copy()

        show_ABC.set_fill(YELLOW)
        show_ACD.set_fill(YELLOW)

        # Текст | Text
        second_text = MarkupText(f'<i>{a}′, {b}′ – ортогональные проекции соответственно углов'
                                 f' {a}, {b} на плоскость угла {c}</i>').scale(0.3)

        # Выделяем фигуры для иллюстрации альфа-штрих и бета-штрих углов + немного текста
        # Select shapes to illustrate alpha stroke and beta stroke corners + some text
        self.play(Write(second_text.shift(RIGHT * 3 + UP)))

        self.play(Create(show_ABC, run_time=1))
        self.play(Uncreate(show_ABC, run_time=1))
        self.play(Create(show_ACD, run_time=1))
        self.play(Uncreate(show_ACD, run_time=1))

        self.play(FadeOut(second_text, run_time=2))
        self.wait(2)

        # Текст и его иллюстрация | Text and illustration
        third_text = MarkupText(f'<i>По-скольку ортогональная проекция угла всегда не превосходит его, '
                                f'из {a}′+{b}′ = {c} получим {a}+{b} ≥ {c}.</i>').scale(0.3)
        self.play(Write(third_text.shift(RIGHT * 3 + UP)))
        self.wait(2)
        self.play(FadeOut(third_text, run_time=2))
        
