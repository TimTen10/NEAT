class GA:

    def __init__(self, initial_population):
        self.population = [(individual, 0) for individual in initial_population]

    def _selection(self):
        pass

    def _crossover(self):
        # Determines the genotype with higher fitness, then calls .crossover(#2 highest) on it
        pass

    def _mutation(self):
        # Should return all the different mutations of that generation
        pass

    def run(self):
        # TODO: there is more data needed to run each of the individuals and get a fitness value
        # TODO: an evaluate function is needed as some point, probably remove run() from the class
        # Loops through: fitness -> selection, crossover, mutation -> fitness -> repeat
        pass
