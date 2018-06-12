clearvars

%brute force flowing sum (elementary addition)
digits = zeros(1,400);
digits(1) = 2;
tic
for i = 2:1000
    digits = digits+digits;
    for j = 1:400
        if digits(j) >= 10
            digits(j+1) = digits(j+1)+1;
            digits(j) = mod(digits(j),10);
        end
    end
end
answer = sum(digits)
toc