% facts
delecious(cake).
delecious(chocolate).
delecious(pikles).
sweets(cake).
sour(pikle).
sweets(pastry).
delecious(pastry).


% Rules
likes(priya,Food) :- delecious(Food) , sweets(Food) , write(Food) , nl , fail.