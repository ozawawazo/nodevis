%%jsondata_load.m
%%JSON�t�@�C����ǂݍ��݁C�אڍs��Ad�C�d�ݍs��U�C
%%�ŒZ�����̍s��B�@�̓��ꕨ�C�d�ݍs��U��2���Us�C�����
%%JSON�t�@�C���̓ǂݏo���ɁCjsonlab�@���g�p�D

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