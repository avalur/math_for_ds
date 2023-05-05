from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.azure import AzureService

first_eqn = MathTex( "1", "x", "-", "2", "y", "+", "1", "z", "=", "0")
second_eqn = MathTex("2", "x", "+", "1", "y", "-", "3", "z", "=", "5")
third_eqn = MathTex("-4", "x", "+", "7", "y", "-", "1", "z", "=", "1")
equations_array = [first_eqn, second_eqn, third_eqn]
equations = MobjectMatrix(
    [[first_eqn], [second_eqn], [third_eqn]],
    left_bracket="\\{",
    right_bracket="\\}",
    )
bra = equations.get_brackets()
bra[1].set_color(BLACK) # set background color to exclude the right bracket

for eqn in equations_array:
    eqn.set_color_by_tex_to_color_map({
        "x": RED,
        "y": GREEN,
        "z": BLUE,
    })

equation_matrix_colors = [RED, GREEN, BLUE]
augmented_matrix_colors = [RED, GREEN, BLUE, TEAL]
big_augmented_matrix_colors = [RED, GREEN, BLUE, TEAL, ORANGE]

# ts_service = GTTSService(lang="en", tld="com")
ts_service = AzureService(
                voice="en-US-JennyNeural",
                style="newcast-casual",
            )


def finishScene(self):
    self.play(*[FadeOut(mob) for mob in self.mobjects])

class Start(VoiceoverScene):
    def construct(self):
        title = Tex("Linear Equations")
        VGroup(title, equations).arrange(DOWN)
        
        self.set_speech_service(ts_service)

        with self.voiceover(text="Consider an example with a system of three linear equations. How to find all solutions?") as tracker:
            self.play(
            Write(title),
            FadeIn(equations, shift=UP),
            run_time=tracker.duration
            )
        self.wait()
        finishScene(self)

class Second(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ts_service)

        with self.voiceover(text="Let's solve it using the Gauss-Jordan elimination algorithm") as tracker:
            self.add(equations)
            self.play(equations.animate.scale(0.8).to_corner(corner=UP + LEFT, buff=0.5))
            self.wait(0.5)

        coefficient_matrix = Matrix(
            [("1", "-2", "1", "0"), ("2", "1", "-3", "5"), ("-4", "7", "-1", "1")])
        coefficient_matrix_flat = VGroup(*VGroup(*coefficient_matrix)[0]).copy()
        for i in VGroup(*coefficient_matrix)[1:]:
            self.play(Write(i))
        self.wait()

        toFade = []
        with self.voiceover(text="First of all, we note that from the coefficients of the equations and the right-hand sides, one can compose a three-by-four matrix, which is uniquely defined the entire system.") as tracker:
            for (variable) in range(0,4):
                for (eqnz) in range(0,3):
                    resultant = variable + 4 * eqnz
                    which_eqn = third_eqn
                    if eqnz == 0:
                        which_eqn = first_eqn
                    elif eqnz == 1:
                        which_eqn = second_eqn
                    toFade.append(which_eqn[variable*3].copy())
                    self.play(Transform(toFade[-1], coefficient_matrix_flat[resultant]), **{"run_time":0.75})

        for fade in toFade:
            self.play(FadeOut(fade), **{"run_time":0.01})
        self.play(ApplyMethod(coefficient_matrix.shift, LEFT*3.5))
        separator1 = Line(LEFT*2.1 + UP*1.1, LEFT*2.1 + DOWN*1.1, color=YELLOW)

        self.play(Create(separator1), **{"run_time":0.15})
        for i in range(0,4):
            for j in range(0,3):
                self.play(VGroup(*VGroup(*coefficient_matrix)[0])[i+4*j].animate.set_color(augmented_matrix_colors[i]),**{"run_time": 0.1})
        coefficient_matrix_flat = VGroup(*VGroup(*coefficient_matrix)[0]).copy()

        rref_matrix = Matrix(
            [("1", "-2", "1", "0"), ("0", "5", "-5", "5"), ("0", "-1", "3", "1")])
        rref_matrix_flat = VGroup(*VGroup(*rref_matrix)[0])
        rref_matrix.shift(RIGHT*3)
        
        arrow = Arrow(LEFT*0.9, RIGHT*0.5)

        bottom_text1 = Tex("Apply the first iteration of")
        bottom_text2 = Tex("Gauss-Jordan elimination algorithm")
        bottom_text = VGroup(bottom_text1, bottom_text2).arrange(DOWN, buff=0.2)
        bottom_text.shift(DOWN*2)
        with self.voiceover(text="Apply the first iteration of Gauss-Jordan elimination algorithm") as tracker:
            self.play(Create(arrow), **{"run_time":0.4})

            for i in VGroup(*rref_matrix)[1:]:
                self.play(Write(i))
            self.play(Write(bottom_text), **{"run_time":1})

        row = SurroundingRectangle(coefficient_matrix.get_rows()[0])
        with self.voiceover(text="Using the first equation given by the first row of the matrix, with the elementary transformations of the rows set the first elements of the remaining rows to zero.") as tracker:
            self.play(Create(row), **{"run_time": 1.75})
            for i in range(0,12):
                rref_matrix_flat[i].set_color(augmented_matrix_colors[i%4])
                self.play(Transform(coefficient_matrix_flat[i], rref_matrix_flat[i]), **{"run_time": 0.75})

        self.wait()
        self.play(Create(rref_matrix), **{"run_time": 0.25})
        self.remove(bottom_text)

        for fade in [separator1, row, coefficient_matrix, 
                     coefficient_matrix_flat, arrow]:
            self.play(FadeOut(fade), **{"run_time":0.01})

        rows = SurroundingRectangle(rref_matrix.get_rows()[1:])

        left_matrix = Matrix(
            [("1", "-2", "1", "0"), ("0", "-1", "3", "1"), ("0", "5", "-5", "5")]
        )

        left_matrix.shift(LEFT*3.5)
        for i in VGroup(*left_matrix)[1:]:
            self.play(Write(i))
        left_matrix_flat = VGroup(*VGroup(*left_matrix)[0]).copy()

        with self.voiceover(text="After that, the second and third rows of the matrix are swapped to zero out the second elements of the remaining rows using the second row.") as tracker:
            self.play(Create(rows), **{"run_time": 1.75})
            self.wait(0.5)
            for i in range(0,12):
                if 0 <= i <= 3:
                    left_matrix_flat[i].set_color(augmented_matrix_colors[i%4])
                    self.play(Transform(rref_matrix_flat[i], left_matrix_flat[i]), **{"run_time": 0.75})
                if 4 <= i <= 7:
                    left_matrix_flat[i+4].set_color(augmented_matrix_colors[i%4])
                    self.play(Transform(rref_matrix_flat[i], left_matrix_flat[i+4]), **{"run_time": 0.75})
                if 8 <= i <= 11:
                    left_matrix_flat[i-4].set_color(augmented_matrix_colors[i%4])
                    self.play(Transform(rref_matrix_flat[i], left_matrix_flat[i-4]), **{"run_time": 0.75})

        self.play(FadeOut(rows), **{"run_time":0.01})
           
        self.wait()

        for i in range(0,4):
            for j in range(0,3):
                self.play(VGroup(*VGroup(*left_matrix)[0])[i+4*j].animate.set_color(augmented_matrix_colors[i]),**{"run_time": 0.1})

        self.play(FadeOut(rref_matrix), **{"run_time":0.01})

        bottom_text1 = Tex("Apply the second iteration of")
        bottom_text2 = Tex("Gauss-Jordan elimination algorithm")
        bottom_text = VGroup(bottom_text1, bottom_text2).arrange(DOWN, buff=0.2)
        bottom_text.shift(DOWN*2)
        arrow = Arrow(LEFT*0.9, RIGHT*0.5)
        with self.voiceover(text="Apply the second iteration of Gauss-Jordan elimination algorithm.") as tracker:
            self.play(Create(arrow), **{"run_time":0.4})
            self.play(Write(bottom_text), **{"run_time":1})
            self.wait()

        rref_matrix = Matrix(
            [("1", "-2", "1", "0"), ("0", "-1", "3", "1"), ("0", "0", "10", "10")])
        rref_matrix_flat = VGroup(*VGroup(*rref_matrix)[0])
        rref_matrix.shift(RIGHT*3)
        
        for i in VGroup(*rref_matrix)[1:]:
            self.play(Write(i))

        row = SurroundingRectangle(left_matrix.get_rows()[1])
        with self.voiceover(text="Thus, repeating the described iterations, we bring the initial matrix of the system to the row echelon form matrix.") as tracker:
            self.play(Create(row), **{"run_time": 1.75})

            for i in range(0,12):
                rref_matrix_flat[i].set_color(augmented_matrix_colors[i%4])
                self.play(Transform(left_matrix_flat[i], rref_matrix_flat[i]), **{"run_time": 0.75})

        with self.voiceover(text="After that, we easily solve each equation from the bottom up and find all the solutions.") as tracker:
            for fade in [row, left_matrix, arrow, bottom_text]:
                self.play(FadeOut(fade), **{"run_time":0.01})

        for i in range(2,-1,-1):
            row = SurroundingRectangle(rref_matrix.get_rows()[i])
            if i == 2:
                bottom_text = Tex("z", " = 1")
                bottom_text.set_color_by_tex('z', BLUE)
            elif i == 1:
                bottom_text = Tex("y", " = 2")
                bottom_text.set_color_by_tex('y', GREEN)
            else:
                bottom_text = Tex("x", " = 3")
                bottom_text.set_color_by_tex('x', RED)
            self.play(Create(row), **{"run_time": 1.75})
            bottom_text.shift(DOWN*1.8)
            self.play(Write(bottom_text), **{"run_time": 1.2})
            self.wait()
            self.remove(bottom_text)
            self.remove(row)
        finishScene(self)

class Full(VoiceoverScene):
    def construct(self):
        Start.construct(self)
        Second.construct(self)
