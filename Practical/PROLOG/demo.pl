% Greater elements
%  Query formate  ?( 5,6, X)

max(X,Y,X):-X>=Y.
max(X,Y,Y):-X<Y .

% factorial 
%  Query formate  ?( 5, X)

% fact 
fact(0,1).
% Rule
fact(N,Result):- 
    N>0 ,
    N1 is N-1 , 
    fact(N1,R1) ,
    Result is N*R1.

% Summation of n numbers

%  Query formate  ?( 5, X)
% facts
sum(0,0).

% Rules
sum(N,Result):-
    N>0,
    N1 is N-1,
    sum(N1,R1),
    Result is N+R1.

% Fibonacci sum

% Facts
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

print_fibo(N):-
    fibo(N,Result),
    write('The fibonacci of '), write(N), write(' is '), write(Result), nl.