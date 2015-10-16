# コンパイラの指定
CC= g++



CFLAGS= -g -Wall -O2 #-I/usr/include/octave-3.8.2 \
#`pkg-config --cflags opencv`
LIBS= #-L/lib/octave/3.8.2 -loctave -lcruft -L/lib -lreadline -ldl -lfftw3 \
#`pkg-config --libs opencv` -lm
INCLUDES=

#プログラムファイル名を変更する場合はここを変更してください。この場合、test.cという名前であればコンパイルが通ります。
# if xxxx.c , you should change as OBJECTS=xxxx.o and TARGET=xxxx
OBJECTS=weight.o
TARGET=weight


# プログラム作成
all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(TARGET) $(LIBS)

# Clean
clean:
	rm -f *.[o]
	rm $(TARGET)
	rm *~

# オブジェクトファイル生成ルール
.cc.o:
	$(CC) $(INCLUDES) $(CFLAGS) -c $<

