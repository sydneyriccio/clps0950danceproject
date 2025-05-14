# clps0950danceproject
# Step 1: Setup - Import Libraries and Define Dance_Moves

# We use the random module to shuffle and extend the dance sequence each round.
# We learned how to use random.choice() from Python documentation and examples online! 
import random; # helps to shuffle random dance moves in each round

# matplotlib is a library we looked up and learned to use visualizing performance data
import matplotlib.pyplot as plt; % used to create a graph of the player's performance after the game
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