clearvars

list = 100:999;
prod = list.*list';
tic
prod = flip(unique(prod));
toc

pal = 0;
iter = 1;
while(pal ~= 3 && prod(iter) > 99999)
   a = prod(iter);
   b = num2str(a);
   pal = sum(~(b(1:3)-flip(b(4:6))));
   iter = iter+1;
end

if pal == 3
    answer = prod(iter-1) 
else
    answer = 99999
end