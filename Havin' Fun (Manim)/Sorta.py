from manim import *
import random

def parametric_heart(t):
    return np.array([
        16 * np.sin(t)**3,
        13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t),
        0
    ]) * 0.025

class TextExample(Scene):
    def construct(self):
        text =  Text("Imagine a set of constraints", font_size=30)
        bform = MathTex(r"\Phi = (x_1 \lor x_2) \land (\neg x_2 \lor x_3) \land (\neg x_3 \lor x_4) \land (\neg x_1 \lor x_4)")
        text1 = Text("Can we assign values (true/false) to variables to satisfy them all?", font_size=25)
        #text.to_edge(UP)
        bform.next_to(text, DOWN)
        text1.next_to(bform, DOWN)
        text2 = Text("Brute Force!", font_size= 45, color=RED)
        text3 = Text("Try ALL possible combinations:", font_size=25, t2c={"ALL":RED}).next_to(bform, UP)
        
        self.play(Write(text))
        self.play(text.animate.shift(UP))
        self.play(FadeIn(bform))
        self.play(bform.animate.shift(UP))
        self.play(FadeIn(text1))
        self.wait()
        self.wait()
        text2.next_to(text1, DOWN) 
        self.play(Write(text2))
        self.wait()
        self.play(FadeOut(text2, text1, text))
        text3.next_to(bform, UP) 
        self.play(Write(text3))
        self.play(text3.animate.shift(UP))
        self.play(bform.animate.shift(UP))
        self.wait()

        newform = MathTex(r"\Phi = (F \lor x_2) \land (\neg x_2 \lor x_3) \land (\neg x_3 \lor x_4) \land (T \lor x_4)").next_to(text3, DOWN)
        assign1 = MathTex(r"x_1 = F", color=BLUE)
        self.play(Transform(bform, newform), run_time=0.5)
        assign1.next_to(bform, DOWN)
        self.play(Write(assign1))
        newform = MathTex(r"\Phi = (F \lor F) \land (T \lor x_3) \land (\neg x_3 \lor x_4) \land (T \lor x_4)",
                          substrings_to_isolate="F" ).next_to(text3, DOWN)
        newform.set_color_by_tex(r"(F \lor F)", RED)
        self.play(Transform(bform, newform), run_time=0.5)
        assign2 = MathTex(r"x_2 = F", color=BLUE)
        assign2.next_to(assign1, DOWN)
        self.play(Write(assign2))
        res = Text("UNSAT :(", color=RED)
        res.next_to(assign2, DOWN) 
        self.play(Write(res))
        self.wait()
        
        bform1 = MathTex(r"\Phi = (x_1 \lor x_2) \land (\neg x_2 \lor x_3) \land (\neg x_3 \lor x_4) \land (\neg x_1 \lor x_4)").next_to(text3, DOWN)
        self.play(FadeOut(res, assign1, assign2))
        self.play(Transform(bform, bform1), run_time=0.5)

        newform = MathTex(r"\Phi = (T \lor x_2) \land (\neg x_2 \lor x_3) \land (\neg x_3 \lor x_4) \land (F \lor x_4)").next_to(text3, DOWN)
        assign1 = MathTex(r"x_1 = T", color=BLUE)

        self.play(Transform(bform, newform), run_time=0.5)
        assign1.next_to(bform, DOWN)
        self.play(Write(assign1))

        newform = MathTex(r"\Phi =  (T \lor F) \land (T \lor x_3) \land (\neg x_3 \lor x_4) \land (F \lor x_4)").next_to(text3, DOWN)
        self.play(Transform(bform, newform), run_time=0.5)
        assign2 = MathTex(r"x_2 = F", color=BLUE)
        assign2.next_to(assign1, DOWN)
        self.play(Write(assign2))


        newform = MathTex(r"\Phi =  (T \lor F) \land (T \lor T) \land (F \lor x_4) \land (F \lor x_4)").next_to(text3, DOWN)
        self.play(Transform(bform, newform), run_time=0.5)
        assign3 = MathTex(r"x_3 = T", color=BLUE)
        assign3.next_to(assign2, DOWN)
        self.play(Write(assign3))

        newform = MathTex(r"\Phi =  (T \lor F) \land (T \lor T) \land (F \lor F) \land (F \lor F)").next_to(text3, DOWN)
        self.play(Transform(bform, newform), run_time=0.5)
        assign4 = MathTex(r"x_4 = F", color=BLUE)
        assign4.next_to(assign3, DOWN)
        self.play(Write(assign4))

        res = Text("UNSAT :(", color=RED)
        res.next_to(assign4, DOWN) 
        self.play(Write(res))
        self.wait()

        bform1 = MathTex(r"\Phi = (x_1 \lor x_2) \land (\neg x_2 \lor x_3) \land (\neg x_3 \lor x_4) \land (\neg x_1 \lor x_4)").next_to(text3, DOWN)
        self.play(FadeOut(res, assign1, assign2, assign3, assign4))
        self.play(Transform(bform, bform1), run_time=0.5)

        newform = MathTex(r"\Phi = (T \lor x_2) \land (\neg x_2 \lor x_3) \land (\neg x_3 \lor x_4) \land (F \lor x_4)").next_to(text3, DOWN)
        assign1 = MathTex(r"x_1 = T", color=BLUE)

        self.play(Transform(bform, newform), run_time=0.5)
        assign1.next_to(bform, DOWN)
        self.play(Write(assign1))

        newform = MathTex(r"\Phi =  (T \lor T) \land (F \lor x_3) \land (\neg x_3 \lor x_4) \land (F \lor x_4)").next_to(text3, DOWN)
        self.play(Transform(bform, newform), run_time=0.5)
        assign2 = MathTex(r"x_2 = T", color=BLUE)
        assign2.next_to(assign1, DOWN)
        self.play(Write(assign2))


        newform = MathTex(r"\Phi =  (T \lor T) \land (F \lor T) \land (F \lor x_4) \land (F \lor x_4)").next_to(text3, DOWN)
        self.play(Transform(bform, newform), run_time=0.5)
        assign3 = MathTex(r"x_3 = T", color=BLUE)
        assign3.next_to(assign2, DOWN)
        self.play(Write(assign3))

        newform = MathTex(r"\Phi =  (T \lor F) \land (T \lor T) \land (F \lor T) \land (F \lor T)").next_to(text3, DOWN)
        self.play(Transform(bform, newform), run_time=0.5)
        assign4 = MathTex(r"x_4 = T", color=BLUE)
        assign4.next_to(assign3, DOWN)
        self.play(Write(assign4))

        res = Text("SAT !!", color=RED)
        res.next_to(assign4, DOWN) 
        self.play(Write(res))
        self.wait()
        #self.play(FadeOut(bform, newform, assign1, assign2, assign3, assign4, res, text3))
        title = Text("The Boolean Satisfiability Problem")
        title.move_to(DOWN * 6) 
        woo = VGroup (bform, newform, assign1, assign2, assign3, assign4, res, text3)

        self.play(
            woo.animate.shift(UP * 10),
            title.animate.move_to(ORIGIN), 
            run_time=1.5
        )
        title2 = Text("The Boolean Satisfiability Problem", t2c={"Sat":YELLOW}, t2w={"Sat":BOLD})
        self.play(Transform(title, title2))
        self.remove(title)
        self.play(title2.animate.shift(UP*2))

        defn = Text("SAT Problem: Given a formula in CNF, determine if there is an assignment that satisfies it.",
                    font_size=20,
                    t2w={"SAT Problem":BOLD}).next_to(title2, DOWN)
        self.play(Write(defn)) 
        self.wait()

        boova = MathTex(r"\text{Boolean Variables: } 0, 1", font_size = 30)
        lit = MathTex(r"\text{Literals: a variable }(x)\text{, its negation }(\neg x)", font_size = 30).next_to(boova, DOWN)
        claw = MathTex(r"\text{Clauses: a disjunction }(\lor)\text{ of literals}", font_size = 30).next_to(lit, DOWN)
        frm = MathTex(r"\text{CNF: a conjunction }(\land)\text{ of clauses}", font_size = 30).next_to(claw, DOWN)

        self.wait()
        
        frmdef = VGroup (boova, lit, claw, frm)
        self.play(Write(frmdef))
        self.wait()
        colc = VGroup(title2, defn, frmdef)
        pst1 = Text("SAT lies at the intersection of logic, graph theory and computer science with critical applications in", font_size=20)
        pst2 = Text("Machine Learning, Circuit Verification as well as scheduling!", 
                    font_size=20,
                    t2c = {"Machine Learning":PURPLE_D, "Circuit Verification":PURPLE_C, "scheduling":PURPLE_E}).next_to(pst1, DOWN)
        pst = VGroup(pst1, pst2)
        pst.move_to(DOWN*5)

        self.play(
            colc.animate.shift(UP * 3),
            pst.animate.move_to(DOWN * 0.5), 
            run_time=1.5
        )
        heart = ParametricFunction(parametric_heart, t_range=[0, TAU], color=PINK).move_to(LEFT * 6 + UP * 0.6).rotate(0.7)
        self.play(Create(heart), run_time=3)
        self.wait(1)

        funk = Text("Although . . .", font_size= 25).to_edge(DOWN)
        self.play(Write(funk))
        self.wait()
        self.play(FadeOut(*self.mobjects))

        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height
        )
        background.set_fill(BLACK, opacity=1)
        background.set_stroke(width=0)
        self.add(background)
        self.wait()

        prob = Text("Trying all possible combinations of the variables is tedious and inefficient", 
                    font_size= 25, t2c= {"tedious":RED, "inefficient":RED}).to_edge(UP)
        funk2 = Text("Is there an efficient way of finding such assignments?", font_size=25).next_to(prob, DOWN)
        self.play(Write(prob))
        self.play(Write(funk2))
        self.wait()
        img = ImageMobject("pnp.png")
        img.set_height(4) 
        img.move_to(LEFT * 2 + DOWN)
        imgtxt = Text("We don't know? :'(", font_size= 25)
        imgtxt.next_to(img, RIGHT, buff=0.5)
        self.play(FadeIn(img))
        self.play(Write(imgtxt))
        bof = Group(prob, funk2, img, imgtxt)
        self.wait()
        shise1 = Text("In fact, there is no known SAT solver whose worst-case complexity is better than", 
                      font_size=24, t2s = {"known":ITALIC})
        shise1.move_to(DOWN * 5)
        shise2 = Text("expoential for general Boolean Satisfiability problems.", font_size=24).next_to(shise1, DOWN)
        shise = Group(shise1, shise2)
        self.play(
            bof.animate.shift(UP * 3),
            shise.animate.move_to(DOWN), 
            run_time=1.5
        )
        self.play(FadeOut(bof))
        self.play(shise.animate.shift(UP * 3))

        txs1 = Text("Any deterministic algorithm for solving SAT might need to explore both assignment",
                   font_size=24, t2c = {"deterministic":YELLOW}).next_to(shise, DOWN)
        txs2 = Text("on hard instances.",
                   font_size=24).next_to(txs1, DOWN)
        txs = VGroup(txs1, txs2)
        self.play(Write(txs))
        self.wait()
        
        axes = Axes(x_range=[-1, 5.5], y_range=[0, 40]).scale(0.5).to_corner(DL)
        graph = axes.plot(lambda x: 2**x, color=BLUE)

        vals = MathTex(r"f(n) = \Theta(2^n)", font_size = 30).next_to(axes, UP)
        self.play(Write(vals))
        self.play(Create(axes), Create(graph))
        self.wait()

        caus = MathTex(r"\text{If a supercomputer processes }10^{12}\text{ ops/s", font_size = 30).move_to(RIGHT * 3 + DOWN)
        caus2 = MathTex(r"\text{It would need more than the age of the universe } ( ~10^{17} )", font_size=30).next_to(caus, DOWN)
        cause4 = MathTex(r"\text{for an input size of }100", font_size=30).next_to(caus2, DOWN)
        caus3 = VGroup(caus, caus2, cause4)
        self.play(Write(caus3))

        self.wait(3)

        bye = Group (caus3, axes, graph, vals, shise, txs)
        ff=Text("We can still improve regardless of the Worst Case.", font_size=10).move_to(DOWN*5)
        
        """self.play(
            bye.animate.shift(UP * 10),
            ff.animate.move_to(DOWN), 
            run_time = 1 
        )
        self.wait(2)
        self.play(FadeOut(bye, ff))""" ###########

        how = Text("How").move_to(DOWN * 5) 
        very = Text("very").move_to(DOWN * 5)
        tragic = Text("TRAGIC!!1!").move_to(DOWN * 5)
        self.play(
            bye.animate.shift(UP * 10),
            how.animate.move_to(DOWN), 
            run_time = 1 
        )
        self.play(
            how.animate.shift(UP * 10),
            very.animate.move_to(DOWN),
            run_time=1
        )

        self.play(
            very.animate.shift(UP * 10),
            tragic.animate.move_to(DOWN),
            run_time=1
        )
        alpha = ValueTracker(0)
        def update_background_and_text(mob):
            alpha_value = alpha.get_value()
            new_bg_color = interpolate_color(BLACK, WHITE, alpha_value)
            new_text_color = interpolate_color(WHITE, BLACK, alpha_value)

            background.set_fill(new_bg_color, opacity=1)
            tragic.set_color(new_text_color)

        background.add_updater(update_background_and_text)
        self.play(alpha.animate.set_value(1), run_time=2, rate_func=smooth)
        background.clear_updaters()
        texs = Text("not reeeally", font_size=20, color=BLACK).next_to(tragic, DOWN, buff=0.05)
        self.play(Write(texs))

        self.play(FadeOut(tragic, texs))
        
        hp1 = Text("By 2007, heuristic SAT solvers had achieved remarkable performance, capable of handling",
                   font_size=24, color=BLACK).to_edge(UP)
        hp2 = Text("tens of thousands of variables and millions of clauses.", font_size=24, color=BLACK).next_to(hp1, DOWN)
        hp = VGroup(hp1, hp2)
        self.play(Write(hp))
        self.wait()

        hp3 = Text("Using techniques like clause learning, variable selection heuristics, restarts",
                   font_size=24, color=BLACK,
                   t2c={"clause learning": RED, "variable selection heuristics": BLUE, "restarts": GREEN})
        hp4 = Text("symmetry breaking and many more", font_size=24, color=BLACK,
                   t2c={"symmetry breaking": PURPLE}).next_to(hp3, DOWN)
        hp5 = VGroup(hp3, hp4)
        self.play(Write(hp5))

        ends = Text("So although the worst case complexity is exponentially hard, real-world problems often have",
                    font_size=24, color=BLACK)
        ends2 = Text("hidden structure and if exploited, solutions can be found in seconds or minutes.",
                     font_size=24, color=BLACK).next_to(ends, DOWN)
        ends3 = VGroup(ends, ends2).to_edge(DOWN)
        self.play(Write(ends3))

        self.wait(1)
        self.play(FadeOut(hp, ends3, hp5))


        alpha.set_value(1)
        background.add_updater(lambda mob: mob.set_fill(interpolate_color(BLACK, WHITE, alpha.get_value()), opacity=1))
        self.play(alpha.animate.set_value(0), run_time=1, rate_func=smooth)
        background.clear_updaters()
        self.wait(2)

        name1 = Text("DPLL")
        name2 = Text("Davis Putnam Logemann Loveland", t2c={"D":RED, "P":RED, "L":RED})

        self.play(Write(name1))
        self.wait()
        #self.play(name1.animate.set_color(RED))
        self.play(Transform(name1, name2))
        self.play(name1.animate.shift(UP*2))
        text = Text("a complete backtracking-based search algorithm",  font_size=25, color=GRAY)
        text.next_to(name1, DOWN)
        self.play(Write(text))
        self.wait()
        #self.play(FadeOut(name1, text))
        
        img1 = ImageMobject("Martin_Davis2.jpg")
        img2 = ImageMobject("Putnam2.jpg")
        img1.set_height(2) 
        img2.set_height(2)
        images = Group(img1, img2).arrange(RIGHT, buff=0.3)
        images.to_edge(DL, buff=0.5)
        self.play(FadeIn(images))

        pixExp = Text ("The Davis-Putnam algorithm was developed by Martin Davis and Hilary Putnam for checking validity \nof a first-order logic formula using a resolution-based decision procedure.", font_size=15, color=GRAY)
        picExp2 = Text ("Later in the 60s, the algorithm was refined alongside George Logemann and Donald Loveland.", font_size=15, color=LIGHT_GRAY)
        pixExp.next_to(images, RIGHT, buff=0.5)

        picExp2.next_to(pixExp, DOWN, buff=0.2).align_to(pixExp, LEFT)
        self.play(FadeIn(pixExp))
        self.play(FadeIn(picExp2))
        self.wait(3)
        self.play(FadeOut(images, picExp2, pixExp))

        expla = Text("DPLL uses many techniques to reduce the brute force search space e.g.", 
                     font_size=25,
                     t2c = {"reduce the brute force search space":BLUE})
        self.play(Write(expla))

        UnP = Text("Unit Propagation",font_size=30).next_to(expla, DOWN)
        self.play(Write(UnP))
        PLE = Text("Pure Literal Elimination",font_size=30).next_to(UnP, DOWN)
        self.play(Write(PLE))
        Bk = Text("Backtracking",font_size=30).next_to(PLE, DOWN)
        self.play(Write(Bk))
        self.wait()
        g1 = Group(name1, text, expla)
        g2 = Group( PLE, Bk)
        self.play(
            g1.animate.shift(UP * 10),
            g2.animate.shift(DOWN*10), 
            UnP.animate.shift(UP * 3),
            run_time = 1
        )
        txd = Text("Assume you have the following CNF:", font_size=26).next_to(UnP, DOWN)
        self.play(Write(txd))
        eq = MathTex (r"\Phi = x_1 \land (x_1 \lor x_2) \land (\neg x_2 \lor x_3) \land (\neg x_1 \lor x_4) \land (\neg x_1 \lor x_4)").next_to(txd, DOWN)
        self.play(Write(eq))
        txd1 = MathTex(r"\text{We have a clause containing }x_1{  only.}")
        self.play(Write(txd1))
        self.wait()
        self.play(FadeOut(txd1))
        txd1 = MathTex(r"\text{To satisfy it, you must assume }x_1 = T\text{ then simplify.}")
        self.play(Write(txd1))
        self.wait()
        self.play(FadeOut(txd1))
        eq1 = MathTex (r"\Phi = T \land (T \lor x_2) \land (\neg x_2 \lor x_3) \land (F \lor x_4) \land (F \lor x_4)")
        ftnt = Text("Simplify : If clause contains:\n1. Literal : Ignore Clause.\n2. Its Negation : Ignore Literal.", font_size = 15).to_corner(DL)
        self.play(Write(eq1))
        self.play(Write(ftnt))
        eq2 = MathTex (r"\Phi = (T \lor x_2) \land (\neg x_2 \lor x_3) \land (F \lor x_4) \land (F \lor x_4)")
        self.play(ReplacementTransform(eq1, eq2))
        ##self.remove(eq1)
        self.wait()
        eq3 = MathTex (r"\Phi = (\neg x_2 \lor x_3) \land (F \lor x_4) \land (F \lor x_4)")
        self.play(ReplacementTransform(eq2, eq3))
        #self.remove(eq2)
        self.wait()
        eq4 = MathTex (r"\Phi = (\neg x_2 \lor x_3) \land (x_4) \land (F \lor x_4)")
        self.play(ReplacementTransform(eq3, eq4))
        #self.remove(eq3)
        self.wait()
        eq5 = MathTex (r"\Phi = (\neg x_2 \lor x_3) \land (x_4) \land (x_4)")
        self.play(ReplacementTransform(eq4, eq5))
        #self.remove(eq4)
        self.wait()
        self.play(ReplacementTransform(eq, eq5))
        #self.remove(eq)
        self.play(FadeOut(txd, eq5, ftnt))
        self.play(
            g1.animate.shift(DOWN * 10),
            g2.animate.shift( UP * 10),
            UnP.animate.shift(DOWN * 3),
            run_time = 1
        )
        self.wait()

        g1 = Group(name1, text, expla)
        g2 = Group( UnP, Bk)
        self.play(
            g1.animate.shift(UP * 10),
            g2.animate.shift(DOWN*10), 
            PLE.animate.shift(UP * 3),
            run_time = 1
        )
        txd = Text("Assume you have the following CNF:", font_size=26).next_to(PLE, DOWN)
        self.play(Write(txd))
        eq = MathTex (r"\Phi = (\neg x_1 \lor x_2) \land (\neg x_2 \lor x_3) \land (\neg x_1 \lor x_4) \land (\neg x_1 \lor x_4)").next_to(txd, DOWN)
        self.play(Write(eq))
        txd1 = MathTex(r"\text{All clauses contains one polarity of }x_1").next_to(eq, DOWN)
        self.play(Write(txd1))
        self.wait()
        self.play(FadeOut(txd1))
        txd1 = MathTex(r"\text{To satisfy it, you must assume }x_1 = F\text{ then simplify.}").next_to(eq, DOWN)
        self.play(Write(txd1))
        self.wait()
        self.play(FadeOut(txd1))
        eq1 = MathTex (r"\Phi = (T \lor x_2) \land (\neg x_2 \lor x_3) \land (T \lor x_4) \land (T \lor x_4)").next_to(eq, DOWN)
        self.play(Write(eq1))
        eq2 = MathTex (r"\Phi = (\neg x_2 \lor x_3)").next_to(eq, DOWN)
        self.play(ReplacementTransform(eq1, eq2))
        self.wait()
        self.play(ReplacementTransform(eq, eq2))
        self.play(FadeOut(txd, eq2))
        self.play(
            g1.animate.shift(DOWN * 10),
            g2.animate.shift( UP * 10),
            PLE.animate.shift(DOWN * 3),
            run_time = 1
        )
        self.wait()

        g1 = Group(name1, text, expla)
        g2 = Group( UnP, PLE)
        self.play(
            g1.animate.shift(UP * 10),
            g2.animate.shift(DOWN*10), 
            Bk.animate.shift(UP * 3),
            run_time = 1
        )
        txd = Text("Jump back to the level of contradiction one level at a time.", font_size=26).next_to(Bk, DOWN)
        self.play(Write(txd))
        txd1 = Text("(Chronological)", font_size=26).next_to(txd, DOWN)
        self.play(Write(txd1))
        self.play(FadeOut(txd, txd1))
        self.play(
            g1.animate.shift(DOWN * 10),
            g2.animate.shift( UP * 10),
            Bk.animate.shift(DOWN * 3),
            run_time = 1
        )

        self.wait(1)  
        self.play(FadeOut(*self.mobjects))     

        timeline = Line(start=LEFT * 5, end=RIGHT * 5, color=WHITE)
        years = ["1960", "1970", "1980", "1990", "2000"]
        events = [
            "DPLL",
            "NP-Complete",
            "Tseitin Encoding",
            "1st SAT Competition",
            "CDCL"
        ]
        event_positions = [LEFT * 5 + RIGHT * (i * 2.5) for i in range(len(years))]
        dots = [Dot(point=pos, color=RED) for pos in event_positions]
        year_labels = [Text(year, font_size=24).next_to(dot, DOWN, buff=0.3) for year, dot in zip(years, dots)]
        descriptions = [Text(event, font_size=17).next_to(dot, UP, buff=0.7) for event, dot in zip(events, dots)]
        self.play(Create(timeline))
        self.wait(1)
        cursor = Triangle().scale(0.2).rotate(PI/2).move_to(dots[0].get_top() + UP * 0.3)
        self.play(FadeIn(cursor))
        for i in range(len(years)):
            
            self.play(FadeIn(dots[i]), FadeIn(year_labels[i]))
            self.play(Write(descriptions[i]))

            if i < len(years) - 1:
                self.play(cursor.animate.move_to(dots[i + 1].get_top() + UP * 0.3), run_time=1)
                self.wait(0.5)

        self.wait(2)
        framebox1 = SurroundingRectangle(descriptions[1], buff = 0.1)
        framebox2 = SurroundingRectangle(descriptions[2], buff = 0.1)
        framebox3 = SurroundingRectangle(descriptions[3], buff = 0.1)
        textf1 = Text("SAT was the first problem known to be NP-complete, as proved by \nStephen Cook in 1971 and independently by Leonid Levin in 1973.", 
                      font_size=15, 
                      t2c={"Stephen Cook":YELLOW, "Leonid Levin":YELLOW})
        textf1.next_to(framebox1, UP)

        textf2 = Text("Tseitin transformation takes as input an arbitrary combinatorial logic circuit \nand produces an equisatisfiable boolean formula in conjunctive normal form (CNF).", 
                      font_size=15, 
                      t2c={"arbitrary combinatorial logic":YELLOW, "conjunctive normal form (CNF)":YELLOW})
        textf2.next_to(framebox2, UP)

        textf3 = Text("to identify new challenging benchmarks and to promote new solvers \nfor SAT as well as to compare them with state-of-the-art solvers.", 
                      font_size=15, 
                      t2c={"benchmarks":YELLOW, "promote new solvers":YELLOW})
        textf3.next_to(framebox3, UP)

        self.play(Create(framebox1))
        self.play(Write(textf1))
        self.wait(3)
        self.play(FadeOut(textf1))
        self.play(ReplacementTransform(framebox1, framebox2))
        self.play(Write(textf2))
        self.wait(3)
        self.play(FadeOut(textf2))
        self.play(ReplacementTransform(framebox2, framebox3))
        self.play(Write(textf3))
        self.wait(3)
        self.play(FadeOut(textf3, framebox3))
        self.wait()
        #self.play(self.camera.frame.animate.set(width=4).move_to(descriptions[4]))
        self.play(FadeOut(timeline, *dots, *year_labels, descriptions[0], descriptions[1], descriptions[2], descriptions[3], cursor))

        name1 = Text("CDCL")
        #self.add(name1)
        self.play(Transform(descriptions[4], name1))  
        self.remove(descriptions[4])  
        name2 = Text("Conflict-Driven Clause Learning", t2c={"C": RED, "D": RED, "L": RED})
        self.play(Transform(name1, name2))  
        self.remove(name1) 
        self.play(name2.animate.shift(UP * 2))
        self.wait()
        text = Text("DPLL with Conflict Analysis and Non-Chronological Backjumping",  font_size=25, color=GRAY)
        text.next_to(name2, DOWN)
        self.play(Write(text))
        self.wait()
        exp = Text("Traced using an implication graph <3", font_size= 25).move_to(DOWN)
        self.play(Write(exp))
        self.wait(2)
        self.play(FadeOut(name2, text, exp))

        
        #ImpcForm = MathTex (r"\Delta = \begin{cases} (A \lor B) \\ (B \lor C) \\ (\neg A \lor \neg X \lor Y) \\ (\neg A \lor X \lor Y) \\ (\neg A \lor \neg Y \lor Z) \\ (\neg A \lor X \lor \neg Z) \\ (\neg A \lor Y \lor \neg Z) \end{cases}", font_size = 20 )
        #ImpcForm.to_corner(UL)
        
        c1 = MathTex(r"(A \lor B) \\ ", font_size=20).align_to(UP + LEFT)
        c2 = MathTex(r"(B \lor C) \\ ", font_size=20).next_to(c1, DOWN)
        c3 = MathTex(r"(\neg A \lor \neg X \lor Y) \\ " , font_size=20).next_to(c2, DOWN)
        c4 = MathTex(r"(\neg A \lor X \lor Y) \\ ", font_size=20).next_to(c3, DOWN)
        c5 = MathTex(r"(\neg A \lor \neg Y \lor Z) \\ ", font_size=20).next_to(c4, DOWN)
        c6 = MathTex(r"(\neg A \lor X \lor \neg Z) \\ ", font_size=20).next_to(c5, DOWN)
        c7 = MathTex(r"(\neg A \lor \neg Y \lor \neg Z) ", font_size=20).next_to(c6, DOWN)
        equation = VGroup(c1, c2, c3, c4, c5, c6, c7)
        equation.to_corner(UL)
        self.play(Write(equation))

        nodes = ["A", "B", "C", "X", "Y", "Z", "P"]
        edges = [
            ("A", "Y", 3, True),  # Clockwise (true)
            ("X", "Y", 3, False), # Counter-clockwise (false)
            ("A", "Z", 5, True),  
            ("Y", "Z", 5, False), 
            ("A", "P", 7, True), 
            ("Z", "P", 7, True), 
            ("Y", "P", 7, False)  
        ]
        positions = {
            "A": LEFT * 3 + UP * 2,
            "B": LEFT * 3 + UP * 1,
            "C": LEFT * 3,
            "X": LEFT * 3 + DOWN * 1,
            "Y": LEFT  + DOWN * 0.3,
            "Z": UP * 0.5 + RIGHT,
            "P": RIGHT * 3.5 + UP * 0.70
        }
        graph = Graph(
            nodes, [], layout=positions, labels=True, layout_scale=3
        )
        for node in nodes:
            graph[node].set_opacity(0)

        self.play(Create(graph))
        for node in nodes:
            self.play(
                graph[node].animate.set_opacity(1).scale(1.2),
                run_time=0.5
            )
            self.play(
                graph[node].animate.scale(1/1.2),
                run_time=0.2
            )
            text = Text(f"{node} = T", font_size=15)
            text.next_to(graph[node], LEFT, buff = 0.07)
            if node == "P":
                text = Text("{}", font_size=15)
                text.next_to(graph[node], RIGHT, buff = 0.07)
            self.play(FadeIn(text))
            #self.wait(1)
            #self.play(FadeOut(text))
            edge_mobjects = []
            for edge in edges:
                src, dest, weight, clockwise = edge
                if dest == node:
                    start_point = graph[src].get_center()
                    end_point = graph[dest].get_edge_center(graph[src].get_top()) if clockwise else graph[dest].get_edge_center(graph[src].get_bottom())
                    if (src == "Z" and dest == "P"):
                        end_point = graph[dest].get_left() 
                    angle = -PI/4 if clockwise else PI/4  
                    curved_edge = CurvedArrow(start_point, end_point, angle=angle, color=WHITE, stroke_width=1.5, tip_length=0.15)
                    edge_mobjects.append(curved_edge)
                    self.play(Create(curved_edge), run_time=1)
            if node == "X":
                decisions = ["A", "B", "C", "X"]
                for d in decisions:
                    self.play(graph[d].animate.set_color(BLUE_E), run_time=0.5)
                text = Text("Decisions", font_size=13, color= BLUE_E)
                text.next_to(graph[node], DOWN)
                self.play(Write(text))
                for d in decisions:
                    self.play(graph[d].animate.set_color(WHITE), run_time=0.5)
            if node == "Y":
                text = Text("Implication", font_size=13, color= GREEN)
                text.next_to(graph[node], DOWN)
                self.play(graph[node].animate.set_color(GREEN_E), run_time=0.5)
                self.play(Write(text))
                arrow = Arrow(
                    start=graph[node].get_center(),
                    end=c3,
                    buff=0.2,
                    color=GREEN_E,
                    #stroke_width=1.5,
                    tip_length=0.15
                )
                framebox = SurroundingRectangle(c3, color=GREEN_E, buff = 0.05)
                self.play(Create(framebox))
                self.play(Create(arrow))
                self.wait()
                self.play(FadeOut(arrow, framebox))
                self.play(graph[node].animate.set_color(WHITE), run_time=0.5)
            if node == "Z":
                text = Text("Implication", font_size=13, color= GREEN)
                text.next_to(graph[node], DOWN)
                self.play(graph[node].animate.set_color(GREEN_E), run_time=0.5)
                self.play(Write(text))
                arrow = Arrow(
                    start=graph[node].get_center(),
                    end=c5,
                    buff=0.2,
                    color=GREEN_E,
                    #stroke_width=1.5,
                    tip_length=0.15
                )
                framebox = SurroundingRectangle(c5, color=GREEN_E, buff = 0.05)
                self.play(Create(framebox))
                self.play(Create(arrow))
                self.wait()
                self.play(FadeOut(arrow, framebox))
                self.play(graph[node].animate.set_color(WHITE), run_time=0.5)
            if node == "P":
                text = Text("CONTRADICTION", font_size=13, color= RED_E)
                text.next_to(graph[node], DOWN, buff = 0.5)
                self.play(graph[node].animate.set_color(RED_E), run_time=0.5)
                self.play(Write(text))
                arrow = Arrow(
                    start=graph[node].get_center(),
                    end=c7,
                    buff=0.2,
                    color=RED_E,
                    #stroke_width=1.5,
                    tip_length=0.15
                )
                framebox = SurroundingRectangle(c7, color=RED_E, buff = 0.05)
                self.play(Create(framebox))
                self.play(Create(arrow))
                self.wait()
                self.play(FadeOut(arrow, framebox))
                self.play(graph[node].animate.set_color(WHITE), run_time=0.5)
        
        razon = Text("Find out the decision levels of every node.", font_size=20,
                     t2c = {"decision":PURPLE_E}).to_corner(UR)
        self.play(Write(razon))
        level = 0
        for node in nodes:
            if node == "Y" or node == "Z" or node == "P":
                self.play(Write(Text("3/", font_size=15, color=PURPLE).next_to(graph[node], UP, buff = 0.05)))
            else:
                text = Text(f"{level}/", font_size= 15, color=PURPLE)
                text.next_to(graph[node], UP, buff=0.05)
                self.play(Write(text))
                level = level + 1
        self.play(FadeOut(razon))
        
        razon = Text("Identify the Unique Implication Points (UIP)",
                     font_size=20,
                     t2c = {"Unique Implication Points":GREEN_E}).to_corner(DR)
        razonexp = Text("(via cut property)", font_size=20).next_to(razon, DOWN, buff = 0.05)
        self.wait()
        self.play(Write(razon))
        self.play(Write(razonexp))

        tex = Text("  Nodes that must be passed in the path from the latest decision \nvariable to the conflict node.",
                    font_size=15).next_to(graph["Y"], DOWN + RIGHT)
        self.play(Write(tex))
        for node in nodes:
            if node == "X" or node == "Y" or node == "P":
                self.play(graph[node].animate.set_color(BLUE_E), run_time=0.5)
        self.wait()
        self.play(FadeOut(tex))
        for node in nodes:
            if node == "X" or node == "Y" or node == "P":
                self.play(graph[node].animate.set_color(WHITE), run_time=0.5)

        tex = Text("Finding the Possible Cuts.",
                    font_size=20).to_edge(DR)
        uhm = VGroup(razon , razonexp)
        self.play(Transform(uhm, tex))
        
        arch1 = CubicBezier(
            start_anchor=LEFT * 1.5 + DOWN * 2.5, 
            start_handle=LEFT * 2.5 + DOWN * 1.25, 
            end_handle=LEFT * 2.5 + UP * 1.5, 
            end_anchor=LEFT * 1.5 + UP * 3, 
            color=GREEN, 
            stroke_width=5
        )
        self.play(Create(arch1))
        tx1 = Text("A=T\nX=T", font_size=15, color=GREEN).next_to(arch1.get_end_anchors(), UP, buff = 0.05)
        self.play(Write(tx1))
        self.wait()

        arch2 = CubicBezier(
            start_anchor=DOWN * 1.3, 
            start_handle=LEFT * 0.7 + DOWN * 0.3, 
            end_handle=LEFT * 0.3 + UP * 1, 
            end_anchor=RIGHT + UP * 2.7, 
            color=GREEN, 
            stroke_width=5
        )
        tx2 = Text("A=T\nY=T", font_size=15, color=GREEN).next_to(arch2.get_end_anchors(), UP, buff = 0.05)
        self.play(Create(arch2))
        self.play(Write(tx2))
        self.wait(1)

        arch3 = CubicBezier(
            start_anchor=RIGHT * 2 + DOWN * 0.6, 
            start_handle=RIGHT * 1.5 + UP * 0.2 , 
            end_handle=RIGHT * 2 + UP * 1, 
            end_anchor=RIGHT * 3 + UP * 2, 
            color=GREEN, 
            stroke_width=5
        )

        self.play(Create(arch3))
        tx3 = Text("A=T\nY=T\nZ=T", font_size=15, color=GREEN).next_to(arch3.get_end_anchors(), UP, buff = 0.05)
        self.play(Write(tx3))
        self.wait(1)
        self.play(FadeOut(uhm))
        
        razon = Text("Determine the 1-UIP Cut i.e.", font_size=20, t2c={"1-UIP Cut": PURPLE_E}).to_edge(DOWN)
        rax = Text("The first UIP encountered on the path leading from the conflict node to the desicion variable.", font_size=15).next_to(razon, DOWN, buff = 0.05)
        
        self.play(Write(razon))
        self.play(Write(rax))
        self.wait()
        self.play(FadeOut(arch1, arch3, tx1, tx3))
        uhm = VGroup(arch2, tx2)
        #self.play(arch2.animate.set_color(PURPLE_E), run_time=0.5)
        #self.play(tx2.animate.set_color(PURPLE_E), run_time=0.5)
        self.play(uhm.animate.set_color(PURPLE_E), run_time=0.5)
        learned = MathTex(r"(\neg A \lor \neg Y)", font_size=20, color=RED_B).next_to(equation, DOWN)
        self.play(Write(learned))
        
        shtuf = Text("The learned clause is learned from the cut and appended to the CNF.", font_size=20).next_to(razon, UP)
        self.play(Write(shtuf))
        self.wait()
        self.play(FadeOut(shtuf, razon, rax))

        razon = Text("Backtrack to the Second-Highest Level in the Learned Clause.", font_size=20, t2c={"Second-Highest": BLUE_A}).to_edge(DOWN)
        self.play(Write(razon))
        self.play(graph["A"].animate.set_color(BLUE_E), run_time=0.5)

        learned_white = MathTex(r"(\neg A \lor \neg Y)", font_size=20, color=WHITE).next_to(equation, DOWN)
        updated_equation = VGroup(*equation, learned_white) 
        self.wait(3)

        
        self.play(FadeOut(*self.mobjects, equation))   
        self.wait() 
        final = Text("Backtracking and Clause Learning significantly bounds the search space.", font_size = 20).shift(UP)
        self.play(Write(final))
        final2 = Text("Suppose clause learning prunes a polynomial amound of branches at each level, the running time:", font_size = 20).next_to(final, DOWN)
        self.play(Write(final2))
        comx = MathTex(r"O(2^{cn}*poly(n))", font_size = 30)
        self.play(Write(comx))
        final3 = MathTex(r"\text{where } c \approx 0.3 - 0.7 \text{ shrinking exponentially!} ", font_size = 30).next_to(comx, DOWN)
        self.play(Write(final3))
        self.wait()

        self.play(FadeOut(final, final2, final3, comx))
        tx1 = Text("With all the advances and reductions for SAT, solving SAT efficiently might", font_size = 24)
        tx2 = Text("just break the internet (literally)", font_size = 24, t2c = {"break the internet": RED}).next_to(tx1, DOWN)
        tx = VGroup(tx1, tx2)
        self.play(Write(tx))
        fun = Text("fun, no?", font_size=24).next_to(tx, DOWN)
        self.play(Write(fun))  
    
        self.wait(4)
        self.play(FadeOut(fun, tx))
    