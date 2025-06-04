import random


class GeneticAlgorithm:
    def __init__(self, digits=None, num_digits=100, correct_score=1, power=1):
        if digits is None:
            digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.correct_score = correct_score
        self.power = power
        self.digits = digits
        self.num_digits = num_digits
        self.solution = [random.sample(self.digits, 1)[0] for _ in range(0, self.num_digits)]

    def new_problem(self):
        self.solution = [random.sample(self.digits, 1)[0] for _ in range(0, self.num_digits)]

    def heuristic(self, guess, power=None):
        if power is None:
            power = self.power
        score = 0
        for i in range(0, len(self.solution)):
            if self.solution[i] == guess[i]:
                score = score + self.correct_score
        return score ** power

    def get_max_score(self):
        return self.heuristic(self.solution)

    @staticmethod
    def crossover(s1, s2):
        child = []
        for i in range(0, len(s1)):
            if random.random() < 0.5:
                child.append(s1[i])
            else:
                child.append(s2[i])
        return child

    def mutate(self, s, mutation_chance=0.01):
        return [random.sample(self.digits, 1)[0] if random.random() < mutation_chance else _ for _ in s]

    def run(self, population_size=100, max_generations=100, mutation_chance=0.01):
        population = [[random.sample(self.digits, 1)[0] for _ in range(0, self.num_digits)] for _ in
                      range(0, population_size)]
        scores = []
        for g in range(0, max_generations):
            correct = list(map(lambda p: self.heuristic(p, power=1), population))
            print("generation:", g, "highest correct: ", max(correct), "average correct", sum(correct) / len(correct))
            scores = list(map(lambda p: self.heuristic(p), population))
            for s_i in range(0, len(scores)):
                if scores[s_i] == self.get_max_score():
                    print("solution found:", population[s_i])
                    exit()
            sample_l = random.choices(population, weights=scores, k=population_size)
            sample_r = random.choices(population, weights=scores, k=population_size)
            next_population = []
            for g in range(0, population_size):
                next_population.append(self.mutate(self.crossover(sample_l[g], sample_r[g]), mutation_chance))
            population = next_population
        correct = list(map(lambda p: self.heuristic(p, power=1), population))
        print("final generation", "highest score: ", max(correct), "average score", sum(correct) / len(correct))


random.seed(14124)
gen_alg = GeneticAlgorithm(digits=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], num_digits=100, correct_score=1, power=10)
gen_alg.run(population_size=1000, max_generations=100, mutation_chance=0.01)
