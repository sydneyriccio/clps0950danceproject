# clps0950danceproject
# Step 1: Setup - Import Libraries and Define Dance_Moves

# We use the random module to shuffle and extend the dance sequence each round.
# We learned how to use random.choice() from Python documentation and examples online! 
import random; # helps to shuffle random dance moves in each round

# matplotlib is a library we looked up and learned to use visualizing performance data
import matplotlib.pyplot as plt; # used to create a graph of the player's performance after the game
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
class DanceMemoryGame: # Class used to keep game logic organized and scalable
    def __init__(self,mode="interactive", memory_limit=5):
        self.mode = mode # "interactive" or "simulate"
        self.mode_limit = memory_limit # used only in simulate mode 
        self.sequence = [] # Stores the dance sequence
        self.round = 1
        self.performance = []
        self.detailed_results = [] # Analyzing memory patterns 

# Step 3: Show the sequence to the player
def show_sequence(self):
    print(f"\nRound {self.round}:")
    for move in self.sequence:
        print(move)
    input("\nPress Enter when you are ready to repeat the sequence...")

# Step 4: Get player or simulated input 
def get_player_input(self): 
    if self.mode == "simulate": #Simulates a player with a fixed memory limit: wrote this to model cognitive overload and working memory limits in psychology. 
        if len(self.sequence) <= self.memory_limit:
            return self.sequence.copy()
        else:
            # We intentionally add an incorrect final move to simulate a recall failure
            return self.sequence[:self.memory_limit -1] + ["wrong"]
    else:
        print("'\nType the sequence of moves (separated by spaces!):")
        return input (">").strip().lower().split()
    
# Step 5: Play a single round
def play_round(self):
    # Adds a new random move each round, making the sequence longer and harder to remember
    new_move = random.choice(DANCE_MOVES)
    self.sequence.append(new_move)

    self.show_sequence()
    player_input = self.get_player_input ()