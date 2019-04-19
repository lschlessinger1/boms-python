class ModelSelector:

    def __init__(self, problem, model_space, fitness_function, strategy, callback):
        self.problem = problem
        self.model_space = model_space
        self.fitness_function = fitness_function
        self.strategy = strategy
        self.callback = callback
        self.time = None

    def run(self):
        pass

    def initialization(self):
        raise NotImplementedError
