# %%
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(100)

# Function to simulate and calculate conditional probability
def simulate_and_estimate():
    data = pd.DataFrame({
        'Earthquake': np.random.choice([0, 1], 1000, p=[0.95, 0.05]),
        'Factory_Stop': np.random.choice([0, 1], 1000, p=[0.7, 0.3]),
        'Transport_Delay': np.random.choice([0, 1], 1000, p=[0.5, 0.5])
    })

    model = BayesianNetwork([
        ('Earthquake', 'Factory_Stop'),
        ('Earthquake', 'Transport_Delay')
    ])
    model.fit(data, estimator=MaximumLikelihoodEstimator)

    # Get conditional probability of factory stop given Earthquake=1
    prob = model.predict_probability(pd.DataFrame({'Earthquake': [1]}))
    return prob.values[0][1]

# Run 100 simulations and collect probabilities
shutdown_probs = [simulate_and_estimate() for _ in range(100)]

# Compute average probability
avg_shutdown_prob = np.mean(shutdown_probs)
print(f"Average probability of factory shutdown given earthquake (over 100 simulations): {avg_shutdown_prob:.2%}")

# Visualization
plt.figure(figsize=(8, 5))
plt.hist(shutdown_probs, bins=15, edgecolor='black')
plt.axvline(avg_shutdown_prob, color='red', linestyle='dashed', linewidth=1.5, label=f'Average: {avg_shutdown_prob:.2%}')
plt.title('Distribution of P(Factory_Stop | Earthquake=1) over 100 Simulations')
plt.xlabel('Conditional Probability')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



