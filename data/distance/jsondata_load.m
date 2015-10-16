%%jsondata_load.m
%%JSONファイルを読み込み，隣接行列Ad，重み行列U，
%%最短距離の行列B　の入れ物，重み行列Uの2乗のUs，を作る
%%JSONファイルの読み出しに，jsonlab　を使用．

data=loadjson('data.json');
num=size(data.nodes,2);
U=zeros(num);
Ad=zeros(num);
B=zeros(num);

for i=1:num
U(i,i)=data.nodes{1,i}.weight;
end

Us=U*U;

link=size(data.links,2);

for i=1:link
a=data.links{1,i}.source+1;
b=data.links{1,i}.target+1;
Ad(a,b)=1;
Ad(b,a)=1;
end