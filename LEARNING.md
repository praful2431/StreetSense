# Learning Journey

StreetSense is a practical learning project for building skills in programming, algorithms, mathematics, AI, and optimization.

## 1. Simulation Fundamentals

Learn:

- Python and software architecture
- Object-oriented programming
- Data structures
- Grid representation
- Entity modelling
- Coordinates and state
- Validation and constraints
- Random generation

## 2. Graph Theory

Learn how a city grid becomes a graph.

```text
Grid → Graph → Algorithms
```

Concepts:

- Nodes and edges
- Neighbours
- Connectivity
- Paths
- Weights
- Graph traversal

## 3. Pathfinding

Progress from simple to advanced shortest-path algorithms.

**BFS**

- Queues
- Graph traversal
- Visited sets
- Parent tracking
- Shortest paths

**Dijkstra**

- Weighted graphs
- Edge costs
- Priority queues
- Relaxation
- Weighted shortest paths

**A\***

- Heuristics
- Search efficiency
- Manhattan distance
- Exploration vs guidance

The goal is to understand **why** each algorithm works and when to use it.

## 4. Procedural City Generation

Automatically generate cities using:

- Random generation
- Constraints
- Valid placement
- Spatial relationships
- Reproducibility
- Simulation parameters

Eventually, generation can move from purely random layouts toward realistic patterns.

## 5. Multi-Path Routing

Move from a single route to an entire network.

```text
Many Houses
     ↓
Road Network
     ↓
Many Offices
```

Explore:

- Multiple sources and destinations
- Shared roads
- Competing paths
- Bottlenecks
- Network-wide effects

This is where pathfinding becomes an optimization problem.

## 6. Optimization

Determine what makes a road network good.

**Minimize:**

- Travel distance
- Travel time
- Congestion
- Infrastructure cost

**Maximize:**

- Connectivity
- Accessibility
- Network efficiency

Learn:

- Cost functions
- Objective functions
- Constraints
- Search strategies
- Combinatorial optimization

## 7. Machine Learning

Introduce ML only after building the algorithmic foundation.

Explore:

- Supervised learning
- Learning from algorithm-generated solutions
- Policy learning
- Value-based methods
- Neural networks
- Reinforcement learning

The key question:

> Can a model learn a useful strategy from the simulation?

## 8. Reinforcement Learning

Eventually, the simulator can become an RL environment.

```text
Observe city
    ↓
Choose action
    ↓
Observe result
    ↓
Receive reward
    ↓
Improve strategy
```

Possible rewards:

- Successful connections
- Reduced travel distance
- Reduced congestion
- Lower infrastructure cost
- Better network efficiency

## 9. Real-World Extension

Move beyond an abstract grid toward:

- Geographic data
- Real road networks
- Traffic datasets
- GIS
- OpenStreetMap
- Realistic traffic models
- Dynamic routing

This could turn StreetSense into an experimental platform for transportation problems.

# What I Want to Learn

**Programming** — Build stronger Python and software-engineering skills through a long-running project.

**Algorithms** — Develop a deep understanding of graphs, pathfinding, and optimization.

**Mathematics** — Apply linear algebra, probability, statistics, discrete mathematics, and optimization to practical problems.

**AI** — Understand when machine learning is useful and how it can work alongside classical algorithms.

**Systems Thinking** — Understand how local decisions affect an entire system. A road that is optimal for one house may create a bottleneck for the whole city.

# Final Learning Objective

Learn to approach complex problems like:

> “How should a transportation network be constructed to efficiently serve a changing population?”

through:

```text
Model the problem
      ↓
Represent it mathematically
      ↓
Build an algorithmic solution
      ↓
Measure the solution
      ↓
Optimize it
      ↓
Use ML where appropriate
      ↓
Build an intelligent system
```

StreetSense is the practical environment for developing these skills.
