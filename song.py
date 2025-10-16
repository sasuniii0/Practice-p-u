import time
import sys

lyrics = [
    "I wanna da-, I wanna dance in the lights",
    "I wanna ro-, I wanna rock your body",
    "I wanna go, I wanna go for a ride",
    "Hop in the music and rock your body right",
    "Rock that body, come on, come on, rock that body (rock your body)",
    "Rock that body, come on, come on, rock that body",
    "Rock that body, come on, come on, rock that body (rock your body)",
    "Rock that body, come on, come on, rock that body"
]

# Function to simulate karaoke-style text
def sing(line, delay=0.05):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # move to next line
    time.sleep(0.8)  # pause between lines

time.sleep(1)

for line in lyrics:
    sing(line)

# End of the song