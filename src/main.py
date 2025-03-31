def main():
    import sys
    import os
    import json
    from utils import factorial


    if len(sys.argv) < 2:
        print("Error: Please provide a command.")
        sys.exit(1)

    if sys.argv[1] == 'help':
        print("Description: p_dist is a module that allows users to calculate values of probability distributions.\n")
        print("Usage: p_dist <command> <number> <options>\n")
        print("Commands:")
        print("*  fact: Calculate the factorial of a number.")
        print("*  def_prob_dist: Define a probability distribution.")
        print("     -r: Return the probability distribution.")
        print("     -m: Display the mean of the probability distribution.")
        print("     -v: Display the variance of the probability distribution.")
        print("     -s: Display the standard deviation of the probability distribution.")
        print("     -p: Display the probability of a given value.")
        sys.exit(1)

    if sys.argv[1] == 'fact':
        try:
            number = int(sys.argv[2])
            result = factorial(number)
            print(f"The factorial of {number} is {result}")
        except ValueError:
            print("Error: Please enter a valid integer.")
            sys.exit(1)
        
    if sys.argv[1] == 'def_prob_dist':
        """
        This function allows the user to define a probability distribution. The format will be as follows:
        p_dist <def_prob_dist> x_1: p_1, x_2: p_2, ..., x_n: p_n
        where x_i are the values of the random variable and p_i are their corresponding probabilities.
        The probabilities should sum up to 1. As defined by a probability distribution. This script creates a temporary environment variable called prob_dist that contains 
        the probability distribution. It will be a dictionary where the keys are the values of the random variable and the values are their 
        corresponding probabilities. The following tags can be used along with the command: <def_prob_dist>:
            -r: return the probability distribution as on screen
            -m: display the mean of the probability distribution
            -v: display the variance of the probability distribution
            -s: display the standard deviation of the probability distribution
            -p: display the probability of a given value
        """
        try:
            prob_dist = {}
            tag = ""
            for arg in sys.argv[2:]:
                if arg != "-r" and arg != "-m" and arg != "-v" and arg != "-s" and arg != "-p":
                    if ":" not in arg:
                        print("Error: Please enter a valid value with a random variable and its probability seperated by a colon(:).")
                        sys.exit(1)
                    if not arg.split(":")[0].strip().isdigit():
                        print("Error: Please enter a valid integer for the value of the random variable.")
                        sys.exit(1)
                    prob_dist[arg.split(":")[0].strip()] = float(arg.split(":")[1].strip())
                else:
                    tag = arg
                    break
            if sum(prob_dist.values()) != 1:
                print("Error: The probabilities must sum up to 1.")
                sys.exit(1)
            if tag == "-r":
                print("Random Variable | Probability")
                print("----------------|------------")
                for key, value in prob_dist.items():
                    print(f"{key:^15} | {value:^10.4f}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    

if __name__ == "__main__":
    main()