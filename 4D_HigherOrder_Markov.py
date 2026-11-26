from collections import defaultdict, Counter
import numpy as np

# Step 1: Historical weather observations
weather = [
    "Sunny", "Cloudy", "Rainy", "Rainy",
    "Cloudy", "Sunny", "Cloudy", "Rainy",
    "Sunny", "Sunny", "Cloudy", "Rainy",
    "Rainy", "Cloudy", "Sunny", "Cloudy"
]

# Step 2: Count transitions based on previous TWO states
transition_counts = defaultdict(Counter)

for i in range(2, len(weather)):
    previous_two = (weather[i - 2], weather[i - 1])
    next_state = weather[i]
    transition_counts[previous_two][next_state] += 1

# Step 3: Convert counts into probabilities
transition_probabilities = {}

for pair, counts in transition_counts.items():
    total = sum(counts.values())

    transition_probabilities[pair] = {
        state: count / total
        for state, count in counts.items()
    }

# Display the learned probabilities
print("Learned transition probabilities:")

for pair, probs in transition_probabilities.items():
    print(f"\n{pair} ->")

    for state, probability in probs.items():
        print(f"  {state}: {probability:.2%}")

# Step 4: Predict the next state
current_pair = (weather[-2], weather[-1])

if current_pair in transition_probabilities:
    probs = transition_probabilities[current_pair]

    states = list(probs.keys())
    probabilities = list(probs.values())

    rng = np.random.default_rng(42)
    prediction = rng.choice(states, p=probabilities)

    print("\nPrevious two states:", current_pair)
    print("Predicted next state:", prediction)
else:
    print("Insufficient data for this pair.")
