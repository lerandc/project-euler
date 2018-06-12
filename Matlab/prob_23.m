clearvars
tic
abundants = [];
for i = 1:28123
    if i < divisor_sum(i)
        abundants(end+1) = i;
    end
end

abundants = abundants';
poss_ints = pair_wise_sum(abundants);

poss_ints(poss_ints>28123) = [];

answer = 0;
for i = 1:28123
    if isempty(find(poss_ints == i))
        answer = answer + i;
    end
end

answer 
toc

function sum = divisor_sum(N)
    sum = 0;
    for i = 1:N-1
        if ~mod(N,i)
            sum = sum + i;
        end
    end
end

function sums = pair_wise_sum(abundants)
    len = length(abundants);
    sums = zeros(len,1);
    count = 1;
    for i = 1:len
        for j = i:len
            sums(count) = abundants(i)+abundants(j);
            count = count+1;
        end
    end
    
    sums = unique(sums);
end