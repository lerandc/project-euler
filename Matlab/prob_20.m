clearvars

%brute force flowing sum (elementary addition)
digits = zeros(1,200);
digits(1) = 1;
tic
for i = 2:100
    digits = digits*i;
    for j = 1:200
        if digits(j) >= 10
            while (digits(j) >= 10)
                digits(j+1) = digits(j+1)+1;
                digits(j) = digits(j) - 10;
            end
        end
    end
end
answer = sum(digits)
toc