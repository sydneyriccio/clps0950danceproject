# Dance Memory Trainer 
A Cognitive Pyschology-Based Game built in Python
Created by McKenzie Green, Sydney Riccio, and Victoria Valdes for CLPS 0950. 

**Note**: Again, we struggled a lot with understanding Git. We were all working together collaboratively throughout this project. Logged all of our edits so just pushed everything at the end and tried to simulate the order in which we did it (hours or order may not be completely accurate but we tried to replicate it as best as we could). 

## Overview 

**Dance Memory Trainer** is a terminal-based memory grame that simulates the role of working memory in dancers by presenting users with sequences of dance instructions that increases in length over time. As dancers ourselves, we thought it was significant to bring attention to the talents of dancers in terms of cognitive ability. Because of this, we decided instead of having users memorize numbers or words, players have to memorize sequences of **dance-inspired movement cues** that truly represent the abilities of a dancer in real time. The goal is to see how long a user can correctly recall moves in order before making a mistake, modeling cognitive load and memory span. Overall, the game simulates the experience of learning choreography while dancing cognitive psychology concepts like **Miller's Law**, **chunking**, and **memory capacity**. 

## How to Play

1. **Run the Python script** ('dance_memory_trainer.py').
2. Memorize the dance moves shown in each round.
3. When prompted, type the sequences back using spaces between moves!
4. Advance through as many rounds without many a mistake! You got this!
5. After the game ends, view your performance graph to understand your statistics. Thanks for playing!!

## Pyschology Connection 

This game reflects key principles of cognitive psychology:
- **Working Memory Capacity**: Tracking how many items can be held and recalled.
- **Cognitive Load**: Observing how increased sequence length challenges memory. 
- **Chunking**: Encouraging players to form meaningful groups of moves (like dancers to).
- **Embodied Cognition**: Using physical movement terms to enhance memory encoding.

## Features

- Interactive play mode (user types responses)
- Simulated player mode (to test working memory limits)
- Visualized performance using a bar graph (`matplotlib`)
- Round-by-round tracking of memory accuracy
- Cognitive load analysis: average recall span and failure point
- Modular code structure using classes and functions

## Requirements

- Python 3.x
- 'matplotlib' library

If you do not have 'matplotlib' installed, run":

''bash
pip install matplotlib 