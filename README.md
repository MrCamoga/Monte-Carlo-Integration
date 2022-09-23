# Monte Carlo Integration

A simple program to compute the volume defined by inequalities on any dimension.

## Usage

```
montecarlo(dim, fs, rang, count)
```
`dim` &rarr; dimension of the shape.

`fs` &rarr; lambda expression of list of inequalities.

`rang` &rarr; range of coordinates to generate random points.

`count` &rarr; number of points to generate. If -1, run indefinitely.

## Examples
```
montecarlo(10, lambda x: [x.dot(x) < 1], (-1,1)) # hypervolume of an unit 10-ball: pi^5/5! = 2.55016...
montecarlo(2, lambda x: [x.dot(x)<1], (-1,1)) # Area of an unit circle: pi = 3.14159...
montecarlo(3, lambda x: [(3-sqrt(x[0]**2+x[1]**2))**2+x[2]**2 < 1], (-4,4)) # Volume of torus with radii 3 and 1: 6pi^2 = 59.21762...
montecarlo(3, lambda x: [x[0]**2+x[1]**2<1,x[0]**2+x[2]**2<1,x[1]**2+x[2]**2<1], (-1,1)) # Volume of intersection of three orthogonal cylinders: 8(2-sqrt(2)) = 4.68629...
```