lessThan 2.
lessThan(1, 2).
lessThan(X, Y + 1) :- lessThan(X, Y).
lessThan(X + 1, Y) :- lessThan(X, Y - 1).
not lessThan(Y, X) :- lessThan(X, Y).

? lessThan(10, 23).
? lessThan(10, 4).