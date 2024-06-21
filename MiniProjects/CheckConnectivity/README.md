# Check Website Connectivity

## Problem Statement

You are given a list of websites and their connectivity status. The websites are connected to each other in a network. If a website is connected to another website, it is said to be connected. If a website is not connected to another website, it is said to be disconnected. You have to find the number of connected components in the network.

## Input

python
websites = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
    'D': ['E'],
    'E': ['D']
}

## Output

python
2

## Explanation

The websites 'A', 'B', and 'C' are connected to each other. The websites 'D' and 'E' are connected to each other. So, there are two connected components in the network.

## Hints

1. Use Depth First Search (DFS) to find the connected components in the network.
2. Create a helper function that takes a website and a set of visited websites as input and returns the connected component of the website.
3. Iterate through all the websites and find the connected components of each website. Count the number of connected components in the network.

## Solution

```python
def connected_components(websites):
    visited = set()
    components = 0

    def dfs(website):
        visited.add(website)
        for neighbor in websites[website]:
            if neighbor not in visited:
                dfs(neighbor)

    for website in websites:
        if website not in visited:
            dfs(website)
            components += 1

    return components

websites = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
    'D': ['E'],
    'E': ['D']
}

print(connected_components(websites))
