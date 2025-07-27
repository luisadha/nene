PREFIX := /data/data/com.termux/files/usr
MANDIR := $(PREFIX)/share/man

BIN    := nene


install:
	@mkdir -p $(PREFIX)/bin
	@mkdir -p $(MANDIR)/man1

	@cp -p bin/$(BIN)   $(PREFIX)/bin/
	@cp -p man/$(BIN).1 $(MANDIR)/man1/ 
	@install -Dm755 libexec/nene "$PREFIX/bin/nene"

 	@chmod 755 $(PREFIX)/bin/$(BIN)


uninstall:
	@rm -rf $(PREFIX)/bin/$(BIN)
	@rm -rf $(MANDIR)/man1/$(BIN).1*
	@rm -rf 
