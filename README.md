# nene (Nightly)
## Summary

Nene is both a static site and a set of Bash tools you can run straight from your terminal.

<p align="center">
  <img src="./nene_chibi.png" alt="welcome">
</p>

## Descriptions

Not Echo, Not True is a network-based Bash script collection tool that uses the concept of process substitution with the help of the curl tool to run scripts from the internet directly inside the Terminal, with a pattern like `Source <(curl-L URL)'. Although the implementation uses source, the project name is inspired by the Bash idiom Echo <(True). The pun "Not-echo not-true" represents a transition from the basic Bash syntax that can create a more dynamic execution model, a new standard in running scripts that is more modern, distributed, and still understandable - breaking the comfort of classic shell games with the innovation of static web-based execution.

The app will execute any /endpoints from the luisadha.github.io site with a curl sourced from bash.

## List Contents

Path == myApps

See https://luisadha.github.io/ {myApps} Change {myApps} to route each of my curl-based applications and follow each page's instructions on how to run those curl-based scripts (see: Usage in bold) or simply use this nene script to collect them

Exclusion site https://alrc.luisadha.my.id This subdomain will be always for Alrc Installer project
## Options
```sh
Nene is both a static site and a set of Bash tools you can run straight from your terminal
Usage:
  -a    --api-termux    Install nene-ak47.sh into ~/bin for Run nene\'s app via Android Share
  -u    --select-url    Select and open the link.
  -s    --select=[apps] Execute the explicitly specified application.
  -m    --mode=[online] Select and run through the link.
  -v    --version       Print version script.
  -h    --help          Print this message.
```
## API Intructions
API Instructions

To start using the API, you must fully install the Nene script via Basher.
[See how to instalations](#install)

Once installed, run:
```sh
nene -a
```
This command will install additional features, the nene-ak47.sh script.

Then, to replace your current termux-url-opener, use the following command:
```sh
nene -s=wuoy
```
This will display an interactive fuzzy search dialog.
Select nene-ak47 to enable the "Share to Termux" button feature on supported web apps.

## Run
```sh
nene
```
## Install 
```sh
basher install luisadha/nene
```
## Update
```sh
basher upgrade luisadha/nene
```
## Uninstall
```
basher uninstall luisadha/nene
```

## Licenses

This project is licensed under the [MIT License](LICENSE).

![Nene Casual Chibi](https://sekaipedia.org/w/images/7/7a/Nene_Casual_chibi.png)  
*Gambar oleh [YBamY](https://sekaipedia.org/wiki/User:YBamY), tersedia di [Sekaipedia](https://sekaipedia.org/wiki/Main_Page) di bawah lisensi [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
