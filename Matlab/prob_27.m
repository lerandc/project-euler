clearvars

max_n = 0;
for a = -999%:1:999
    for b = 61%-1000:1:1000
        for n = 0:10000
            r = isprime(quadratic(a,b,n));
            if ~r
                if n > max_n
                    max_n = n;
                    max_a = a;
                    max_b = b;
                end
                break
            end
        end
    end
end

answer = max_a*max_b

function check = isprime(N)
   if N < 4
       check = 1;
   elseif ~mod(sqrt(N),1)
       check = 0;
   elseif ~mod(N,2)
       check = 0;
   else
       list = 2:sqrt(N);
       check = ~any(~mod(N,list));
   end
end

function output = quadratic(a,b,n)
    output = n.^2+a.*n+b;
end