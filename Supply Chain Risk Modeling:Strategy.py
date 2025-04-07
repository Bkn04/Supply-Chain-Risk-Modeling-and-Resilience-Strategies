
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
import pandas as pd
import numpy as np 

# Simulate 1000 historical records: whether an earthquake occurred (1=yes, 0=no),
# and its impact on factory operations and transportation
data = pd.DataFrame({
    'Earthquake': np.random.choice([0, 1], 1000, p=[0.95, 0.05]),  # 5% chance of earthquake
    'Factory_Stop': np.random.choice([0, 1], 1000, p=[0.7, 0.3]),  # 30% chance of factory stop (in case of earthquake)
    'Transport_Delay': np.random.choice([0, 1], 1000, p=[0.5, 0.5])  # 50% chance of transport delay (in case of earthquake)
})

# Define causal relationships: Earthquake affects both Factory_Stop and Transport_Delay
model = BayesianNetwork([
    ('Earthquake', 'Factory_Stop'), 
    ('Earthquake', 'Transport_Delay')
])

# Train the Bayesian Network using Maximum Likelihood Estimation
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Query: What is the probability of the factory stopping given an earthquake?
prob = model.predict_probability(pd.DataFrame({'Earthquake': [1]}))
print(f"Probability of factory shutdown given earthquake: {prob.values[0][1]:.2%}")


# Simulation of the lost after Earthquakes
import numpy as np
def simulate_supply_chain_disruption(num_simulations=1000, backup_supplier=False):
    total_loss = []
    for _ in range(num_simulations):
        # Simulate whether an earthquake occurs (5% chance)
        earthquake = np.random.choice([0, 1], p=[0.95, 0.05])
        
        if earthquake == 1:
            # Simulate whether the main supplier stops production (30% chance)
            main_supplier_stop = np.random.choice([0, 1], p=[0.7, 0.3])
        else:
            main_supplier_stop = 0

        # Determine delivery time based on supplier status
        if main_supplier_stop == 1:
            if backup_supplier:
                delivery_time = 45  # Backup supplier takes 45 days
            else:
                delivery_time = 999  # No delivery possible without backup
        else:
            delivery_time = 30  # Normal delivery time is 30 days
        
        # Check if delivery time exceeds customer tolerance (40 days)
        if delivery_time > 40:
            total_loss.append(10000)  # $10,000 penalty per breach

    # Return average loss per simulation
    return np.mean(total_loss) if total_loss else 0

# Compare two sourcing strategies
loss_single_source = simulate_supply_chain_disruption(backup_supplier=False)
loss_dual_source = simulate_supply_chain_disruption(backup_supplier=True)

print(f"Average loss with single sourcing: ${loss_single_source:.2f} per event")
print(f"Average loss with dual sourcing: ${loss_dual_source:.2f} per event")



