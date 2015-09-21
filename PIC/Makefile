CPU=18f4550
CC=sdcc
CFLAGS=--use-non-free -mpic16 -p$(CPU)
LDLIBS=libc18f.lib
PK2FLAGS=-PPIC$(CPU)

program: main.hex
	pk2cmd $(PK2FLAGS) -Fmain.hex -M

main.hex: $(patsubst %.c, %.o, $(wildcard *.c))
	$(CC) $(CFLAGS) -o $@ $^ $(LDLIBS)

.PHONY: pon
pon:
	pk2cmd $(PK2FLAGS) -T -R

.PHONY: poff
poff:
	pk2cmd $(PK2FLAGS) -W

.PHONY: ptest
ptest:
	pk2cmd $(PK2FLAGS) -I

.PHONY: clean
clean:
	$(RM) *.asm *.cod *.lst *.o

.PHONY: distclean
distclean: clean
	$(RM) *.hex
