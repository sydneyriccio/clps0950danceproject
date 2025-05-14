# clps0950danceproject
# Step 1: Setup - Import Libraries and Define Dance_Moves

# We use the random module to shuffle and extend the dance sequence each round.
# We learned how to use random.choice() from Python documentation and examples online!
import random  # helps to shuffle random dance moves in each round

# matplotlib is a library we looked up and learned to use for visualizing performance data
import matplotlib.pyplot as plt  # used to create a graph of the player's performance after the game

Dance_Moves = [
    "spin - turn to your right", 
    "pop - sharp chest movement", 
    "slide left - slide to the left", 
    "slide right - slide to the right",
    "lock - freeze your arms in place",
    "wave - ripple your arms",
    "jump - quick hop in place",
    "clap - clap your hands",
    "snap - snap your fingers on dominate hand",
    "kick right - kick right leg",
    "kick left - kick left leg",
    "dip - bend knees quickly"
]

# Step 2: Define Game Class
class DanceMemoryGame:  # Class used to keep game logic organized and scalable
    def __init__(self, mode="interactive", memory_limit=5):
        self.mode = mode  # "interactive" or "simulate"
        self.memory_limit = memory_limit  # used only in simulate mode 
        self.sequence = []  # Stores the dance sequence
        self.round = 1
        self.performance = []
        self.detailed_results = []  # Analyzing memory patterns 

    # Step 3: Show the sequence to the player
    def show_sequence(self):
        print(f"\nRound {self.round}:")
        for move in self.sequence:
            print(move)
        input("\nPress Enter when you are ready to repeat the sequence...")

    # Step 4: Get player or simulated input 
    def get_player_input(self): 
        if self.mode == "simulate":
            # Simulates a player with a fixed memory limit
            # We wrote this to model cognitive overload and working memory limits in psychology.
            if len(self.sequence) <= self.memory_limit:
                return self.sequence.copy()
            else:
                # We intentionally add an incorrect final move to simulate a recall failure
                return self.sequence[:self.memory_limit - 1] + ["wrong"]
        else:
            print("\nType the sequence of moves (separated by spaces!):")
            return input("> ").strip().lower().split()

    # Step 5: Play a single round
    def play_round(self):
        # Adds a new random move each round, making the sequence longer and harder to remember
        new_move = random.choice(Dance_Moves)
        self.sequence.append(new_move)

        self.show_sequence()
        player_input = self.get_player_input()

        # Check whether the player input matches the full sequence exactly 
        correct = player_input == self.sequence

        # Save round data for future analysis
        self.detailed_results.append({
            "round": self.round,
            "sequence": self.sequence.copy(),
            "input": player_input,
            "correct": correct
        })

        if correct:
            print("✅ Correct! Moving to the next round.")
            self.performance.append(len(self.sequence))
            self.round += 1
            return True
        else:
            print("\n❌ Incorrect!")
            print(f"The correct sequence was: {' '.join(self.sequence)}")
            return False

    # Step 6: Run the game loop
    def play_game(self):
        print("🎵 Welcome to the Dance Memory Trainer 🎵")
        print("Try to memorize and repeat the growing sequence of dance moves!\n")

        while True:
            if not self.play_round():
                break

        print(f"\nGame over! You reached Round {self.round}.")
        print("Your performance per round:")
        for i, moves in enumerate(self.performance, 1):
            print(f"Round {i}: {moves} moves")

    # Step 7: Plot performance graph
    def plot_performance(self):
        # Looked up how to use matplotlib to make a basic bar chart in Python
        # This visualizes how far the player got before making a mistake!
        plt.bar(range(1, len(self.performance) + 1), self.performance)
        plt.xlabel('Round')
        plt.ylabel('Number of Moves Correct')
        plt.title('Dance Memory Trainer Performance')
        plt.show()

    # Step 8: Analyze memory performance
    def analyze_performance(self):
        print("\n--- Cognitive Load Analysis ---")
        if self.performance:
            avg = sum(self.performance) / len(self.performance)
            print(f"Average moves recalled: {avg:.2f}")
        else:
            print("No data to analyze.")

        # Find the first round where the player failed and made a mistake
        fail_rounds = [r['round'] for r in self.detailed_results if not r['correct']]
        if fail_rounds:
            print(f"First failure occurred at Round {fail_rounds[0]}")
        else:
            print("Perfect performance!")

        # This interpretation connects the project back to psychology
        print("This simulates how dancers or learners struggle with increasing memory load.")
        print("As the sequence grows, it gets harder to hold all items in working memory.")
        print("This mirrors real-world memory breakdowns and the importance of chunking or rehearsal.")

# Step 9: Run the full program
def main():
    # You can switch to simulate mode if you want to test memory limit behavior too!
    # game = DanceMemoryGame(mode="simulate", memory_limit=6)

    # Interactive mode allows the player to type responses manually!
    game = DanceMemoryGame(mode="interactive")
    game.play_game()
    game.plot_performance()
    game.analyze_performance()

# Standard Python convention to run the game only if this file is executed directly
if __name__ == "__main__":
    main()