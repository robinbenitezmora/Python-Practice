# Compute IoU

## Problem Statement

Given two rectangles, determine the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
  "top_left": (1, 4),
  "dimensions": (3, 3) # width, height
}

and

{
  "top_left": (0, 5),
  "dimensions" (4, 3) # width, height
}

{
  "top_left": (0, 5),
  "dimensions" (4, 3) # width, height
}

return 6.

## Function Signature

```python
def compute_iou(rect1: Dict[str, Tuple[int, int]], rect2: Dict[str, Tuple[int, int]]) -> int:
```

## Input

The input parameters are two dictionaries, `rect1` and `rect2`, each containing the following keys:

- `top_left`: a tuple of two integers representing the top-left corner of the rectangle

- `dimensions`: a tuple of two integers representing the width and height of the rectangle

## Output

The function must return an integer representing the area of the intersection of the two rectangles.

## Constraints

- The coordinates of the rectangles are non-negative integers.

- The width and height of the rectangles are positive integers.

- The rectangles are axis-aligned.

- The rectangles are not rotated.

- The rectangles are not empty.

- The rectangles are not degenerate.

- The rectangles are not equal.

- The rectangles are not adjacent.

- The rectangles are not contained in each other.

- The rectangles are not overlapping.

- The rectangles are not touching.

- The rectangles are not intersecting at a single point.

- The rectangles are not intersecting at a single line.

- The rectangles are not intersecting at a single corner.

- The rectangles are not intersecting at a single edge.

- The rectangles are not intersecting at a single vertex.

- The rectangles are not intersecting at a single face.

- The rectangles are not intersecting at a single side.

- The rectangles are not intersecting at a single surface.
