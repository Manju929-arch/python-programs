class Human:

    def __init__(self):
        self.heart = self.Heart()
        self.brain = self.Brain()

    class Heart:
        def beat(self):
            print("Heart is beating")

    class Brain:
        def think(self):
            print("Brain is thinking")



h = Human()


h.heart.beat()
h.brain.think()