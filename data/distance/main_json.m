%%main_json.m
%%�e�X�̍s����쐬���C�������ɋ����s����쐬����
%%�t�@�C�����Ɨ~���������s��͂��̃t�@�C�����������Ă�������
%%�������̂�

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

X=1/2*W*U*Ad*U.'*W.'; %%�v�Z�������s��ɕύX���Ă�������

%D=zeros(size(X));
%for i=1:size(D,1)
%for j=1:size(D,2)
%D(i,j)=1/(1+X(i,j));
%end
%end

fid=fopen('WAdU.txt','w'); %%�ۑ��������t�@�C�����ɕύX���Ă�������

for i=1:size(X,1);
for j=1:size(X,2);
fprintf(fid,'%f',X(i,j));
if (j<size(X,2)) fprintf(fid,' ');
else fprintf(fid,'; '); end
end
end
fclose(fid);
