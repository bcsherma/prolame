timesequals 3.
timesequals(1, 1, 1).
timesequals(X + 1, Y, Z + Y) :- timesequals(X, Y, Z).
timesequals(X, Y + 1, Z + X) :- timesequals(X, Y, Z).
not timesequals(X, Y, Z + 1) :- timesequals(X, Y, Z).
? timesequals(3, 9, 27).
? timesequals(8, 3, 25).
