%%distance.m
%%2つのノードの距離を調べる関数
%%幅優先探索を用いて計算
%%隣接ノードの距離が1のときのみ有効

function length = distance(S,G,A) %スタートSからゴールGまでの距離
				  %Aは隣接行列

if S==G length=0; return; end 	  %S=Gなら距離0
dim=size(A,1);			  %隣接行列の次元
d=zeros(1,dim);			  %Sからの距離
stock=struct('node',[],'parent',[]); %隣接ノードの確保
check=zeros(dim); 		  %すでに調べたか否か

for i=1:dim
  if i!=S
    d(i)=inf;
  end
end

stock(1).node=S; stock(1).parent=S;
check(S)=1;
j=2;
for i=1:dim
  if A(S,i)==1
    stock(j).node=i;
    stock(j).parent=S;
    j++;
  end
end

k=2;
while 1
  x=stock(k);
  if isempty(x.node)
    break; end;

  if check(x.node)!=0 k++; continue; end

  d(x.node)=d(x.parent)+1;
  if x.node==G; break;
  end
  check(x.node)=1;

  for i=1:dim
    if A(x.node,i)==1
      if check(i)!=1
        stock(j).node=i;
        stock(j).parent=x.node;
        j++;
      end
    end
  end
  k++;
end

length=d(G);
end