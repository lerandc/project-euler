%%%%%brute force
clearvars
format long
n = 10; %size1 of grid
n2 = 11; %size2 of grid
pos= [0 0]; % start position
pos = pos + 1; %indices start at 1
grid = zeros(21);
grid(:,1) = 1;
grid(1,:) = 1;
tic
mov1 = movement(pos,n,n2,0);
for n = 1:10
    for n2 = 1:10
        mov = movement(pos,n,n2,0);
        grid(n+1,n2+1) = mov;
    end
end

for i = 12:21
    for j = 2:11
        grid(i,j) = sum(grid(i-1,1:j));
    end
end

for j = 12:21
    for i = 2:21
        grid(i,j) = sum(grid(1:i,j-1));
    end
end
toc

answer = grid(21,21)

function [count] = movement(start,n,n2,count)
    pos = start;
    if pos(1) == n+1 || pos(2) == n2+1
        count = count+1;
        return;
    end
    if pos(1) < n+1
        count = movement([pos(1)+1 pos(2)],n,n2,count);
    end
    if pos(2) < n2+1
        count = movement([pos(1) pos(2)+1],n,n2,count);
    end
end