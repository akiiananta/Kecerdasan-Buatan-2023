import random

# Pembentukan Chromosome
def generate_chromosome():
    a = random.randint(0, 30)
    b = random.randint(0, 10)
    c = random.randint(0, 10)
    d = random.randint(0, 10)
    return [a, b, c, d]

# Inisialisasi Populasi
def initialize_population(population_size):
    population = []
    for _ in range(population_size):
        chromosome = generate_chromosome()
        population.append(chromosome)
    return population

# Evaluasi Chromosome
def fitness_function(chromosome):
    a, b, c, d = chromosome
    equation_result = a + 4 * b + 2 * c + 3 * d
    return abs(equation_result - 30)

# Seleksi Chromosome
def selection(population):
    fitness_values = [1 / (1 + fitness_function(chromosome)) for chromosome in population]
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    
    selected_population = []
    for _ in range(len(population)):
        random_number = random.random()
        for i in range(len(cumulative_probabilities)):
            if random_number <= cumulative_probabilities[i]:
                selected_population.append(population[i])
                break
    
    return selected_population

# Reproduksi (Crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

# Mutasi
def mutation(chromosome, mutation_rate):
    mutated_chromosome = chromosome.copy()
    for i in range(len(mutated_chromosome)):
        if random.random() < mutation_rate:
            mutated_chromosome[i] = generate_chromosome()[i]
    return mutated_chromosome

# Algoritma Genetika
def genetic_algorithm(population_size, num_generations, mutation_rate):
    population = initialize_population(population_size)
    
    for generation in range(num_generations):
        print("Generation:", generation+1)
        
        # Evaluasi populasi
        evaluated_population = [(chromosome, fitness_function(chromosome)) for chromosome in population]
        evaluated_population.sort(key=lambda x: x[1])
        
        best_chromosome = evaluated_population[0][0]
        best_fitness = evaluated_population[0][1]
        print("Best Solution:", best_chromosome)
        print("Best Fitness:", best_fitness)
        print()
        
        # Seleksi populasi
        selected_population = selection([chromosome for chromosome, _ in evaluated_population])
        
        # Reproduksi (Crossover)
        offspring_population = []
        while len(offspring_population) < population_size:
            parent1, parent2 = random.choices(selected_population, k=2)
            offspring1, offspring2 = crossover(parent1, parent2)
            offspring_population.append(offspring1)
            offspring_population.append(offspring2)
        
        # Mutasi
        mutated_population = [mutation(chromosome, mutation_rate) for chromosome in offspring_population]
        
        population = mutated_population
    
    return best_chromosome

# Main program
population_size = 6
num_generations = 10
mutation_rate = 0.1

best_solution = genetic_algorithm(population_size, num_generations, mutation_rate)
print("Final Solution:", best_solution)
