from manim import *

class BubbleSortVisualization(Scene):
    def construct(self):
        java_code_title = Text("Java Code:", font_size=24)
        java_code_title.to_edge(UL, buff=0.75)
        self.play(Write(java_code_title))
        java_code = ''' 
        public void bubbleSort(int[] arr) {
            int n = arr.length;
            for (int i = 0; i < n-1; i++) {
                for (int j = 0; j < n-i-1; j++) {
                    if (arr[j] > arr[j+1]) {
                        int temp = arr[j];
                        arr[j] = arr[j+1];
                        arr[j+1] = temp;
                    }
                }
            }
        }
        '''
        java_code_display = Code(
            code=java_code,
            language="java",
            font_size=20,
            insert_line_no=False,
            background="window",
        )
        java_code_display.to_edge(UP)
        self.play(Write(java_code_display))
        array = [5, 3, 4, 1, 2]
        array_visual = VGroup(*[Square().set_fill(BLUE, opacity=0.5).set_stroke(BLACK).scale(0.75) for _ in array])
        array_labels = VGroup(*[Text(str(num)).scale(0.75) for num in array])
        for square, label in zip(array_visual, array_labels):
            label.move_to(square)
        array_group = VGroup(*[VGroup(square, label) for square, label in zip(array_visual, array_labels)])
        array_group.arrange(RIGHT, buff=1.0)
        array_group.shift(DOWN * 2)
        visualization_title = Text("Visualization of Bubble Sorting").scale(0.75)
        visualization_title.next_to(array_group, DOWN, buff=0.5)
        self.play(FadeIn(array_group))
        self.play(Write(visualization_title))
        n = len(array)
        for i in range(n-1):
            for j in range(n-i-1):
                self.play(array_visual[j].animate.set_fill(YELLOW, opacity=0.8),
                          array_visual[j+1].animate.set_fill(YELLOW, opacity=0.8))

                if array[j] > array[j+1]:
                    self.play(
                        array_visual[j].animate.move_to(array_visual[j+1].get_center()),
                        array_visual[j+1].animate.move_to(array_visual[j].get_center()),
                        array_labels[j].animate.move_to(array_labels[j+1].get_center()),
                        array_labels[j+1].animate.move_to(array_labels[j].get_center()),
                    )
                    array[j], array[j+1] = array[j+1], array[j]
                    array_visual[j], array_visual[j+1] = array_visual[j+1], array_visual[j]
                    array_labels[j], array_labels[j+1] = array_labels[j+1], array_labels[j]
                self.play(array_visual[j].animate.set_fill(BLUE, opacity=0.5),
                          array_visual[j+1].animate.set_fill(BLUE, opacity=0.5))
        self.play(FadeOut(java_code_display))
        self.play(Indicate(array_visual))
        self.wait()