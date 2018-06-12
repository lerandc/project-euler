%go from right end, track over flow of digits for each place
clearvars

A = textread('prob_13.txt','%1n');

B = zeros(100,50);
for i = 1:100
    for j = 1:50
        B(i,j) = A((i-1)*50+j);
    end
end


C = [0 0 0 0 sum(B)];

for i = 54:-1:2
    while(C(i) >= 10)
        C(i) = C(i) - 10;
        C(i-1) = C(i-1)+1;
    end
end