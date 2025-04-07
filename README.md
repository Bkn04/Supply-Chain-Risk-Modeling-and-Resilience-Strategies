# Supply Chain Risk Modeling and Resilience Strategies

Using a Bayesian Network to simulate and evaluate resilience strategies for reducing production risk in the face of unexpected disruptions.

---

## Project Background & Core Problem

### Why is Supply Chain Risk Management Important?

Imagine you run a smartphone manufacturing company, and all your chips are sourced from a factory in Southeast Asia. Suddenly, an earthquake strikes the region — the factory shuts down, roads are damaged, and chips can’t be transported. Your production line is forced to halt, causing millions of dollars in daily losses.

This is what supply chain risk looks like: **unexpected events disrupting the supply of critical components, directly impacting business operations**.

---

## Limitations of Traditional Approaches

Most companies rely on past experience to guide their strategies (e.g., increasing safety stock), but these methods:

- Cannot **quantify the probability** of risk events (e.g., likelihood of an earthquake)
- Struggle to **evaluate the effectiveness** of alternative strategies (e.g., dual sourcing vs. higher inventory)

---

## Project Objectives

1. **Model** the occurrence and impact of disruptive events (e.g., earthquakes, pandemics) using Bayesian Networks.
2. **Simulate** and compare different resilience strategies such as:
   - Backup suppliers
   - Safety stock via dual sourcing
3. **Identify** the most cost-effective and reliable strategy under uncertain conditions.

---

## Step 1: Identify Key Risk Events

Supply chain risks can stem from natural disasters (e.g., earthquakes, typhoons), human-related incidents (e.g., strikes, wars), or market volatility (e.g., raw material price surges). It is critical to first focus on risks that are both high in frequency and significant in impact.

### Example Scenarios for simulation (could be changed based on real cases)

- **Earthquake probability in Southeast Asia:** Historical data suggests one major earthquake every 10 years (approximate probability: 5%).
- **Probability of factory shutdown due to earthquake:** 30% (due to limited earthquake resistance).
- **Probability of transport delay due to earthquake:** 50% (caused by road or port damage).

---

## Step 2: Construct a Bayesian Network

### What is a Bayesian Network?

A Bayesian Network is a graphical model used to represent probabilistic relationships among variables. For example, an "Earthquake" may lead to both "Factory Shutdown" and "Transport Delay," which can ultimately cause "Supply Chain Disruption."

### How to Build a Bayesian Network

1. **Define nodes:** Represent each risk event or outcome as a node (e.g., Earthquake, Factory Shutdown, Transport Delay, Supply Chain Disruption).
2. **Draw directed edges:** Use arrows to illustrate causal relationships between events  
   (e.g., `Earthquake → Factory Shutdown`, `Earthquake → Transport Delay`).
3. **Assign probabilities:** Estimate conditional probabilities based on historical data or expert judgment, indicating the likelihood of each event given its dependencies.
4. **Simulated output:** Run the attached Bayesian Network.py code to make simulations and visualize them, getting the output like below:

![output](https://github.com/user-attachments/assets/15e9da36-0ee1-43f9-8814-4387393c54a6)

## Step 3: Design Resilience Strategies

### What is a Resilience Strategy?

Resilience strategies refer to proactive contingency plans designed to mitigate the impact of supply chain disruptions. Common examples include:

- **Dual sourcing:** Procure raw materials from suppliers in different regions to reduce geographic risk.
- **Safety stock:** Maintain emergency inventory to buffer against supply interruptions.
- **Dynamic logistics routes:** Pre-plan alternative transportation paths in case of disruptions.

### Example: Dual Sourcing Strategy (could be changed based on real cases):

- **Primary Supplier:** Southeast Asia factory – lower cost but higher earthquake risk.
- **Backup Supplier:** Mexico factory – 20% more expensive but with lower risk exposure.

## Step 4: Simulate Strategy Effectiveness

After modeling an earthquake event, simulate how the dual sourcing strategy can reduce potential financial losses.
This step involves implementing code-based simulations to quantify the effectiveness of each strategy, and the results of average 1000 runs are posted below:

![截屏2025-04-07 11 02 47](https://github.com/user-attachments/assets/68977793-ad18-4b93-9694-91a7372e372e)

From the result we could see that: dual sourcing outperforms single sourcing by nearly 50%

## Technical Workflow

This project follows a structured process to address supply chain disruptions, consisting of five main steps:

1. **Risk Identification**  
   Identify key disruptive events (e.g., earthquakes, strikes, raw material price surges) and assess their likelihood.

2. **Bayesian Network Modeling**  
   Construct a Bayesian Network to represent causal relationships and probabilities between events (e.g., Earthquake → Factory Shutdown).

3. **Resilience Strategy Design**  
   Propose mitigation strategies—such as dual sourcing, safety stock, or backup transportation routes—to reduce potential losses.

4. **Monte Carlo Simulation**  
   Run repeated randomized simulations to evaluate how each strategy performs under different risk scenarios.

5. **Strategy Outcome Comparison**  
   Compare simulation results across strategies (e.g., single sourcing vs. dual sourcing) to identify the optimal approach.



