timesequals 3.
prime 1.

timesequals(1, 1, 1).

timesequals(X + 1, Y, Z + Y) :- timesequals(X, Y, Z).
timesequals(X, Y + 1, Z + X) :- timesequals(X, Y, Z).
not timesequals(X, Y, Z + 1) :- timesequals(X, Y, Z).

not prime(X) :- timesequals(A + 1, B + 1, X).


? timesequals(3, 9, 27).
? timesequals(8, 3, 25).
? prime(4).
? prime(7).