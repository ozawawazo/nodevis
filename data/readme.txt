1
	nodevis/data　にjsonデータをコピー
2
	python nodevis/makesentence.py
		※directory = 'pen'←ここを変えたいディレクトリの名前に変更

3
	/usr/bin/python morphological3.py
		※directory = 'pen'←ここを変えたいディレクトリの名前に変更

4
	python nodevis/admatrix.py
		※directory = 'pen'←ここを変えたいディレクトリの名前に変更
	
5
	emacs tacs/nodevis.js
		※directory = 'pen'←ここを変えたいディレクトリの名前に変更

6
	emacs egm-nlp.js
		※'data/pen/data.json' /pen/←ここを変えたいディレクトリの名前に変更
	
7
	python makesentence.py
	/usr/bin/python morphological3.py
	python admatrix.py