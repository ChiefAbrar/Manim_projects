from manim import *

class SimplePendulum(Scene):
    def construct(self):
        rod_length = 3
        bob_radius = 0.2
        pivot = ORIGIN
        rod = Line(pivot, pivot + DOWN * rod_length, color=WHITE)
        bob = Dot(pivot + DOWN * rod_length, radius=bob_radius, color=BLUE)
        pendulum = VGroup(rod, bob)
        amplitude = 0.5
        frequency = 1.5
        def update_pendulum(obj, alpha):
            angle = amplitude * np.sin(2 * np.pi * frequency * alpha)
            obj[0].put_start_and_end_on(pivot, pivot + DOWN * rod_length * np.cos(angle) + RIGHT * rod_length * np.sin(angle))
            obj[1].move_to(pivot + DOWN * rod_length * np.cos(angle) + RIGHT * rod_length * np.sin(angle))
        self.play(UpdateFromAlphaFunc(pendulum, update_pendulum, run_time=6, rate_func=linear))
        self.wait(1)
        final_angle = amplitude
        pendulum_angle_position = pivot + DOWN * rod_length * np.cos(final_angle) + RIGHT * rod_length * np.sin(final_angle)
        bob.move_to(pendulum_angle_position)
        rod.put_start_and_end_on(pivot, pendulum_angle_position)
        vertical_line = DashedLine(start=pivot, end=pivot+DOWN, color=GRAY)
        self.play(Create(vertical_line))
        angle_arc = Arc(radius=0.5, start_angle=-PI/2, angle=final_angle, color=YELLOW)
        theta_label = MathTex("\\theta", color=YELLOW).next_to(angle_arc, RIGHT)
        tension_force = Arrow(start=bob.get_center(), end=pivot, buff=0.1, color=YELLOW)
        mg_force = Arrow(start=bob.get_center(), end=bob.get_center() + DOWN * rod_length / 4, color=WHITE)
        tension_direction = bob.get_center() - pivot
        mg_cos_theta2 = Arrow(start=bob.get_center(), end=bob.get_center() + 0.5 * tension_direction / np.linalg.norm(tension_direction), color=RED)
        mg_sin_theta1 = Arrow(start=bob.get_center(), end=bob.get_center() + LEFT * rod_length / 4, color=BLUE)
        mg_label = MathTex("mg", color=WHITE).next_to(mg_force, DOWN)
        mg_cos_theta_label1 = MathTex("mg \\cos \\theta", color=RED).next_to(mg_cos_theta2, RIGHT)
        mg_sin_theta_label2 = MathTex("mg \\sin \\theta", color=BLUE).next_to(mg_sin_theta1, LEFT)
        tension_label = MathTex("T", color=YELLOW).next_to(tension_force, UP)
        self.play(Create(tension_force), Create(mg_force), Create(mg_cos_theta2), Create(mg_sin_theta1))
        self.play(Write(tension_label), Write(mg_label), Write(mg_cos_theta_label1), Write(mg_sin_theta_label2))
        self.play(Create(angle_arc), Write(theta_label))
        equation1 = MathTex("Non-Linear: \\theta''(t) + \\frac{g}{L} \\sin(\\theta) = 0", color=WHITE).to_edge(UP)
        self.play(Write(equation1))
        equation2 = MathTex("Linearized: \\theta''(t) + \\frac{g}{L} \\theta = 0 \\ ; when \\ \\theta \\sim 0 \\ sin\\theta\\sim0", color=WHITE)
        equation2.next_to(equation1, DOWN, buff=0.5)
        self.play(Write(equation2))
        self.wait(3)