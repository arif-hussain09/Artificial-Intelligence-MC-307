% [apple, banana, cherry]     % a list of atoms
% [1, 2, 3, 4, 5]             % a list of numbers
% [X, Y, Z]                   % a list of variables
% []                           % an empty list

% facts using list 

fruites([apple,banana,pineapple,grapes]).
numbers([1,2,3,4,5,6,7]).


% Summation
% Queary formate ?sum([1,2,....,3],X)

% fact
sum([],0).
% Rules
sum([H|T],Result):-
        sum(T,R1),
        Result is H+R1.


% Length of a list 
% Quary ? Len([1,2,3,.....,5],X)

% fact
len([],0).
% Rules
len([H|T],N):- 
    len(T,N1), %yh so here tail become the new list and so on until it reaches the base case
    N is N1+1.


% Member or not 
% Query Formate ? member([1,2,3,4],3)

% fact
member([X|_],X). % X is head 
% Rules 
member([_|T],X):- member(T,X). % X in tail

% Fibonacci sum
%Query ?Fibo([N,X) -> it will print the numbers and also in last give the sum

%facts
fibo(0,0).
fibo(1,1).
% Rules
fibo(N,Result):-
    N>1,
    N1 is N-1,
    N2 is N-2,
    fibo(N1,R1),
    fibo(N2,R2),
    Result is R1+R2.

% Concatination of Two list 
% Query ?Concat(L1,L2,L_concat)


% Reversing a list 
% Finding the last element 
