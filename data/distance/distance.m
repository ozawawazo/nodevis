%%distance.m
%%2�̃m�[�h�̋����𒲂ׂ�֐�
%%���D��T����p���Čv�Z
%%�אڃm�[�h�̋�����1�̂Ƃ��̂ݗL��

function length = distance(S,G,A) %�X�^�[�gS����S�[��G�܂ł̋���
				  %A�͗אڍs��

if S==G length=0; return; end 	  %S=G�Ȃ狗��0
dim=size(A,1);			  %�אڍs��̎���
d=zeros(1,dim);			  %S����̋���
stock=struct('node',[],'parent',[]); %�אڃm�[�h�̊m��
check=zeros(dim); 		  %���łɒ��ׂ����ۂ�

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