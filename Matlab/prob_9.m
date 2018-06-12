%%%%solve
clearvars
tic
a = (1:500);
b = (1:500)';
a = a.^2;
b = b.^2;
c = sqrt(a + b);
c(~~mod(c,1)) = 0;

[A,B,C] = find(c);

sums = (A+B+C==1000);
index = find(sums,1,'first');

answer1a = [A(index) B(index) C(index)]
answer2a = A(index) * B(index) * C(index)
toc
%%%%%%%%%%%brute force
%bounds a^2 + b^2 = c^2
%       c < a + b
% a <= b < c
% a + b + c = 1000
tic
for i = 1:500
    for j = 1:500
        for k = 1:500
            if (i+j+k) == 1000
                if (i^2+j^2) == k^2
                    answer1 = [i j k];
                    answer2 = i*j*k;
                    toc
                    return
                end
            end
        end
    end
end


