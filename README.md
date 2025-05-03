# clps0950danceproject
%% Step 1: Setup - Import Libraries and Define Dance_Moves
import random % helps to shuffle random dance moves in each round
import matplotlib.pyplot as plt % used to create a graph of the player's performance after the game
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
%% Step 2: Define Game Class