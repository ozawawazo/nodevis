%%main_json.m
%%各々の行列を作成し，それを基に距離行列を作成する
%%ファイル名と欲しい距離行列はこのファイルをいじってください
%%動かすのに

clear all;
close all;

jsondata_load;
for i=1:num
for j=i:num
B(i,j)=distance(i,j,Ad);
B(j,i)=B(i,j);
end
end
make_W; %

X=1/2*W*U*Ad*U.'*W.'; %%計算したい行列に変更してください

%D=zeros(size(X));
%for i=1:size(D,1)
%for j=1:size(D,2)
%D(i,j)=1/(1+X(i,j));
%end
%end

fid=fopen('WAdU.txt','w'); %%保存したいファイル名に変更してください

for i=1:size(X,1);
for j=1:size(X,2);
fprintf(fid,'%f',X(i,j));
if (j<size(X,2)) fprintf(fid,' ');
else fprintf(fid,'; '); end
end
end
fclose(fid);
