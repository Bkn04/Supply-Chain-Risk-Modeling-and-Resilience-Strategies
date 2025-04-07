
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)

def simulate_supply_chain_disruption(num_simulations=1000, backup_supplier=False):
    total_loss = []
    for _ in range(num_simulations):
        earthquake = np.random.choice([0, 1], p=[0.95, 0.05])
        
        if earthquake == 1:
            main_supplier_stop = np.random.choice([0, 1], p=[0.7, 0.3])
        else:
            main_supplier_stop = 0

        if main_supplier_stop == 1:
            if backup_supplier:
                delivery_time = 45  # backup kicks in (slow, but possible)
            else:
                delivery_time = 999  # no delivery
        else:
            delivery_time = 30  # normal delivery

        # Loss rules
        if delivery_time > 50:
            loss = 10000  # Total breach
        elif delivery_time > 40:
            loss = 5000   # Minor breach
        else:
            loss = 0

        total_loss.append(loss)

    return np.mean(total_loss)

# Run 1000 simulations for each strategy
repetitions = 1000
results_single = [simulate_supply_chain_disruption(backup_supplier=False) for _ in range(repetitions)]
results_dual = [simulate_supply_chain_disruption(backup_supplier=True) for _ in range(repetitions)]

avg_loss_single = np.mean(results_single)
avg_loss_dual = np.mean(results_dual)

print(f"Average loss (1000 runs) with single sourcing: ${avg_loss_single:.2f}")
print(f"Average loss (1000 runs) with dual sourcing:   ${avg_loss_dual:.2f}")

# Visualization
plt.figure(figsize=(8, 5))
plt.hist(results_single, bins=20, alpha=0.7, label='Single Sourcing', color='red', edgecolor='black')
plt.hist(results_dual, bins=20, alpha=0.7, label='Dual Sourcing', color='green', edgecolor='black')
plt.axvline(avg_loss_single, color='red', linestyle='dashed', linewidth=1.5)
plt.axvline(avg_loss_dual, color='green', linestyle='dashed', linewidth=1.5)
plt.title('Distribution of Average Losses over 1000 Simulations')
plt.xlabel('Average Loss per Simulation ($)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


