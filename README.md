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
4. **Simulated output:** Run the attached code to make simulations, 




