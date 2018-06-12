
max_terms = 0;
for i = 1:1e6
    terms = 1;
    next_term = collatz(i);
    while(next_term ~= 1)
       next_term = collatz(next_term); 
       terms = terms + 1;
    end
    
    if terms > max_terms
        max_terms = terms;
        start = i;
    end
end

function next_term = collatz(n)
    if ~mod(n,2)
        next_term = n/2;
    else
        next_term = 3*n+1;
    end
end