def exo1():
    """
    Compute the combinatorial adjacency matrix |W|.
    ompute edge list.
    ompute the adjacency matrix.
    """
    u = [1 2; 2 3; 3 1; 1 4; 2 4; 3 4]'
    E = faces(u, : ); E = reshape(E, [2 6*size(E, 2)])
    p = size(E, 2)
    W = sparse(E(1, : ), E(2, : ), ones(p, 1))
    W = max(W, W')


