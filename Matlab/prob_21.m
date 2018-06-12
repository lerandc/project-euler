clearvars
sums = zeros(9999,1);

for i = 2:9999
    sums(i) = divisor_sum(i);
end

pairs = [];
for i = 2:9999
    if sums(i) < 10000
        if (sums(sums(i)) == i) && (sums(i) ~= i)
           pairs = [pairs; sums(i) i];
        end 
    end
end

numbs = unique(pairs);
answer = sum(numbs)

function sum = divisor_sum(N)
    sum = 0;
    for i = 1:N-1
        if ~mod(N,i)
            sum = sum + i;
        end
    end
end