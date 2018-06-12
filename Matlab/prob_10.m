clearvars
tic
list = (1:2e6)';
logs = ~~(ones(2e6,1));
i = 1:sqrt(list(end));
logs(i.^2) = 0;
for i = 1:sqrt(list(end))    
    if logs(i)
        logs = sieve2(list,logs,i);
    end 
end

primes = list(logs);
answer = sum(primes)
toc

function logs = sieve2(list,logs,check)
    hold = logs(check);
    new = ~mod(list(logs),check);
    logs(logs == 1) = logs(logs==1) - new;
    logs(logs < 0) = 0;
    logs(check) = hold;
end