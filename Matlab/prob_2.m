clearvars
seq = [0 1 1]';

while(seq(end) <= 4e6)
    seq(end+1) = seq(end)+seq(end-1);
end

evens = ~(mod(seq,2));

answer = sum(seq.*evens)