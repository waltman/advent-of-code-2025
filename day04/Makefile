C = /usr/bin/cc
CPP = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -Wall -O3 $(INCLDIRS)
CPPFLAGS = -std=c++23 -Wall -O3 $(INCLDIRS)
CPPOBJECTS = printing_dept.o

all: printing_dept

%.o: %.cpp
	$(CPP) $(CPPFLAGS) -c $<

%.o: %.c
	$(C) $(CFLAGS) -c $<

printing_dept: $(CPPOBJECTS)
	$(CPP) -o $@ $(CPPOBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f printing_dept
