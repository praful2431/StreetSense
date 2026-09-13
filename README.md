# StreetSense

StreetSense is an AI and algorithmic urban-traffic simulation project inspired by games such as Mini Motorways and Mini Metro.

The project explores how cities can be represented as grids and graphs, how road networks can be generated, and how algorithms can be used to efficiently connect buildings while dealing with constraints such as distance, congestion, and limited infrastructure.

The long-term goal is to evolve StreetSense from a simple simulator into an intelligent system capable of analysing and optimizing urban road networks.

---

## Vision

StreetSense aims to answer questions such as:

- What is the shortest way to connect a house to an office?
- How should roads be constructed when multiple buildings need to be connected?
- How does adding a road affect the rest of the network?
- How can congestion and travel time be minimized?
- What is the best road layout under limited resources?
- Can an AI learn to construct or improve a road network by itself?

The project will progressively move from classical algorithms toward optimization and machine learning.

---

## Core Concepts

StreetSense combines several areas of computer science and AI:

- Grid-based simulation
- Graph theory
- Pathfinding
- Shortest-path algorithms
- Procedural generation
- Optimization
- Data structures and algorithms
- Simulation
- Machine learning
- Reinforcement learning

The project is intentionally designed so that each stage builds on the previous one.

---

## Planned Architecture

The simulation represents a city using a grid.

A city can contain:

- Houses
- Offices
- Roads
- Driveways

The grid can be interpreted as a graph, allowing algorithms to reason about movement and connectivity.

A simplified representation is:

```text
House
  │
Driveway
  │
Road Network
  │
Driveway
  │
Office
