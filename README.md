# Preview
![plot](https://raw.github.com/niklas-heer/speed-comparison/master/.github/plot_v1.4.png "Speed comparison of programming languages")

---
![lines](https://img.shields.io/tokei/lines/github/lucascompython/Languages-speed-comparison)
# Speed comparison of programming languages 

This projects compares the speed of different programming/scripting languages.

It calculates prime and composite numbers with a very basic algorithm from any given interval to do this comparisom.<br>
All languages use the same algorithm.
<!-- and it uses an implementation of the [Leibniz formula for π](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80) to do the comparison. -->


<!-- Here is a video which explains how it works: [Calculating π by hand](https://www.youtube.com/watch?v=HrRMnzANHHs) -->





## Methods
The code below is a C++ code snippet of the not optimal but not bad algorithm used for counting prime and composite numbers to a given range, that is used for the different languages.

```c++
for(num = lower; num <= upper; num++){
        ctr = 0;

        for(i = 2; i <= num / 2; i++){
            if(num % i == 0){
                ctr++;
                composite++;
                break;
        }
    }
    
        if(ctr == 0 && num != 1){
        prime++;
    }
} 
```



## Disclaimer

I'm no expert in all these languages, so take my results with a grain of salt.<br>
The speed of the language does not determine its quality.
<!-- Also the findings just show how good the languages can handle floating point operations, which is only one aspect of a programming language. -->
I'm not doing any optomization in these tests.

You are also welcome to contribute and help me make fix my possible misuse of some languages(pwease don't try to kill me for my possible mistakes :disappointed_relieved:). :smile:
## Languages used in this comparison


- [Python](https://www.python.org/) - interpreted
- [C++](https://isocpp.org/) - compiled
- [C#](https://docs.microsoft.com/en-us/dotnet/csharp/) - compiled
- [Java](http://www.oracle.com/technetwork/java/index.html) - compiled, VM
- [Javascript](https://www.ecma-international.org/publications/standards/Ecma-402.htm) using [Node.js](https://nodejs.org/) - interpreted, JIT
- [Go](https://golang.org/) - compiled
- [Rust](https://www.rust-lang.org/) - compiled


## Features

- ![Graphs](http://imagem.com)
- ![Table](https://imagem.com)
- Advanced but simple command line integration with multiple options for comparing (E.g: choosing with languages to compare and changing the values of the iterations).
- ![CLI](https://imagem.com)
- All languages will support command line argument parser(positional arguments).
- The program will get and display your pc's status.
- Install all the requirements by itself.

<!-- ## Results
asdd -->
## Run it yourself

Everything is run by a Docker container and a bash script which envokes the programs.

To measure the execution time, in each language is implemented a timer.
The plots are made with [MatPlotLib](https://matplotlib.org).

### Requirements

- `Docker`
- `Makefile` support

### Instalation and Execution

    git clone https://github.com/lucascompython/Languages-speed-comparison
    cd Languages-speed-comparison
    make

## FAQ

> Does it work on Windows?

Yes it does normie, its a docker container it runs everywhere. Who the fuck uses Windows anyways...

> Are the compile/interpret times included in the comparison?

No they are not included yet, im going to compare those too.

## TODO


- [x] Add Rust
- [x] Add Golang
- [ ] Add TypeScript with [Deno](https://deno.land)
- [ ] Add Kotlin
- [ ] Add Swift
- [ ] Add F#
- [ ] Add Haskell
- [ ] Add Lua
- [ ] Add Scala
- [ ] Add Bash
- [ ] Add Powershell
- [ ] Add Php
- [ ] Add R
- [ ] Add R plots instead of MatPlotLib
- [ ] Add Julia
- [ ] Add CSV files and graphs
- [ ] Add other methods of comparing E.g: [Leibniz formula for π](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80)
- [ ] Elixir
- [ ] Ruby
- [ ] Raku (Perl6)
- [ ] Nix


<details>
  <summary>Super top Secret :shushing_face:</summary>
  
<!--START_SECTION:activity-->
1. **Most** languages are good, use whatever you want.
2. Execpt HTML
3. Fuck HTML
<!--END_SECTION:activity-->

</details>

<!-- - [ ] Add [Php 5.6](https://aur.archlinux.org/packages/php56/)
- [ ] Add phpv8js
- [ ] Add python2
- [ ] Add Smalltalk
- [ ] Add C#
- [ ] Add Raku (Perl6)
- [ ] Add Kotlin
- [ ] Add Haskell
- [ ] Add Elixir
- [ ] Add Lisp
- [ ] Add Ada
- [ ] Add COBOL -->
<!-- 
## Thanks

This projects takes inspiration from [Thomas](https://www.thomaschristlieb.de) who did a similar comparison [on his blog](https://www.thomaschristlieb.de/performance-vergleich-zwischen-verschiedenen-programmiersprachen-und-systemen/). -->