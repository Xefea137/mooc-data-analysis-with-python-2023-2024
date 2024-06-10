#!/usr/bin/python3
import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):
    A = np.array([[a1, -1],
                  [a2, -1]])
    B = np.array([-b1, -b2])
    
    try:
        result = np.linalg.solve(A, B)
        tf = True
    except np.linalg.LinAlgError:
        result = np.linalg.lstsq(A, B)[0]
        tf = False
    
    return [result, tf]

    x, residuals, rank, s = np.linalg.lstsq(A, b)
    exact = rank==2
    return x, bool(exact)

def main():
    a1=1
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()