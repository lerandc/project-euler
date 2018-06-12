clearvars

%%%prime sieve
num = 600851475143;
% % tic
% % list = (1:800000)';
% % logs = ~~ones(800000,1);
% % for i = 1:sqrt(list(end))
% %     logs(i*i) = 0;
% % end
% % 
% % 
% % for i = 1:sqrt(list(end))
% %     if logs(i)
% %         logs = sieve(list,logs,i);
% %     end
% % end
% % 
% % 
% % b = list(logs);
% % while(mod(num,b(end)))
% %     %b(end)
% %     b(end) = [];
% % end
% % 
% % answer = b(end);
% % toc
%%%prime sieve 2
tic
list = (1:8000)';
logs = ~~(ones(8000,1));
i = 1:sqrt(list(end));
logs(i.^2) = 0;
for i = 1:sqrt(list(end))    
    if logs(i)
        logs = sieve2(list,logs,i);
    end 
end


 b = list(logs);
% while(mod(num,b(end)))
%     b(end) = [];
% end
% answer2 = b(end);
% toc
% 
% tic

number = num;
iter = 1;
factors  = [];
while (number>1)
    if ~mod(number,b(iter))
        factors = [factors; b(iter)];
        while ~mod(number,b(iter))
            number = number/b(iter);
        end
    end
    iter = iter + 1;
end
answer3 = b(iter-1);
toc
%%%prime factorization
divisor = 2;
number = 8;
tic
while(number >1)
    if(~mod(number, divisor))
        number = number/divisor;
        divisor = divisor - 1;
    end
    divisor = divisor + 1;
end
toc


function logs = sieve(list,logs,check)
    for j = 1:800000
        if (~mod(list(j),check)) && (list(j) ~= check)
           logs(j) = 0; 
        end
    end

end

function logs = sieve2(list,logs,check)
    hold = logs(check);
    new = ~mod(list(logs),check);
    logs(logs == 1) = logs(logs==1) - new;
    logs(logs < 0) = 0;
    logs(check) = hold;
end
