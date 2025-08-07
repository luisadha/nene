PREFIX  := /data/data/com.termux/files/usr
MANDIR  := $(PREFIX)/share/man
BINDIR  := $(PREFIX)/bin
LIBEXEC := $(PREFIX)/libexec
ETC	:= $(PREFIX)/usr/etc

COMPLET	:= 
BIN     := nene
LIBPY   := not-echo-not-true.py

install:
	@mkdir -p $(BINDIR)
	@mkdir -p $(MANDIR)/man1
	@mkdir -p $(LIBEXEC)
	@mkdir -p $(ETC)

	@install -m644 completion/$(COMPLET)	$(ETC)/bash_completion.d/
	@install -m755 bin/$(BIN)		$(BINDIR)/
	@install -m644 man/$(BIN).1		$(MANDIR)/man1/
	@install -m755 libexec/$(LIBPY)		$(LIBEXEC)/
	@echo "✅ Successfully installed to $(PREFIX)"

uninstall:
	@rm -f $(ETC)/$(COMPLET)
	@rm -f $(BINDIR)/$(BIN)
	@rm -f $(MANDIR)/man1/$(BIN).1
	@rm -f $(LIBEXEC)/$(LIBPY)
	@echo "✅ Successfully uninstall"
