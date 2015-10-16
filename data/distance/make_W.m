%make_W.m

W=dlmread('weight.csv',',');
for i=1:size(W,2)
x=sum(W)(i);
We(:,i)=W(:,i)/x;
end