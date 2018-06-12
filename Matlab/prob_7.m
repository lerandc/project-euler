clearvars

checksum = 0;
N = 104800;
while(checksum < 10001)
    list = (1:N)';
    logs = ~~(ones(N,1));
    i = 1:sqrt(list(end));
    logs(i.^2) = 0;
    for i = 1:sqrt(list(end))    
        if logs(i)
            logs = sieve2(list,logs,i);
        end 
    end
    
    checksum = sum(logs)
%    N = N + 100
end

b = list(logs);
answer = b(10001)
function logs = sieve2(list,logs,check)
    hold = logs(check);
    new = ~mod(list(logs),check);
    logs(logs == 1) = logs(logs==1) - new;
    logs(logs < 0) = 0;
    logs(check) = hold;
end