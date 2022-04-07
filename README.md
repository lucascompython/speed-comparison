# Speed comparison of programming languages 

This project compares the speed of different programming/scripting languages.

It calculates prime and composite numbers with a very basic algorithm from any given interval to do this comparisom.<br>
All languages use the same algorithm.
<!-- and it uses an implementation of the [Leibniz formula for π](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80) to do the comparison. -->


<!-- Here is a video which explains how it works: [Calculating π by hand](https://www.youtube.com/watch?v=HrRMnzANHHs) -->
---

# Preview

<div align="center">

![plot](https://cdn.discordapp.com/attachments/795277227423301643/961753951261302814/unknown.png "Speed comparison of programming languages")
![table](https://cdn.discordapp.com/attachments/795277227423301643/961754032744038450/unknown.png "Table") 

![lines](https://img.shields.io/tokei/lines/github/lucascompython/speed-comparison)


</div>

---





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
I'm not doing any optomization in these tests YET I will add an optimized version for each language.

You are also more than welcome to contribute and help me make fix my possible misuse of some languages.
## Languages used in this comparison


- [Python](https://www.python.org/) - interpreted
- [C++](https://isocpp.org/) - compiled
- [JavaScript](https://www.ecma-international.org/publications-and-standards/standards/ecma-402/) using [Node](https://nodejs.org/en/) - interpreted; JIT
- [TypeScript](https://www.typescriptlang.org) using [Deno](https://deno.land) - interpreted; JIT
- [Java](http://www.oracle.com/technetwork/java/index.html) - compiled, VM
<!---

- [C#](https://docs.microsoft.com/en-us/dotnet/csharp/) - compiled
- [Javascript](https://www.ecma-international.org/publications/standards/Ecma-402.htm) using [Node.js](https://nodejs.org/) - interpreted, JIT
- [Go](https://golang.org/) - compiled
- [Rust](https://www.rust-lang.org/) - compiled
--->



## Features

- Graphs
- Tables
- Advanced but simple command line integration with multiple options for comparing (E.g: choosing with languages to compare and changing the values of the iterations).
- All languages will read from a txt file.
- The program will get and display the memory usage.
- It also has two modes, one for running native and other for running inside a docker container.
<!---- Install all the requirements by itself.
-->

<!-- ## Results
asdd -->
## Run it yourself
<!--
Everything is run by a Docker container and a bash script which envokes the programs.
-->

To measure the execution time, in each language is implemented a timer.
To measure the compilation / interpretation time and peak memory usage, before each measurement the GNU time command is invoked. 
The plots are made with [MatPlotLib](https://matplotlib.org).
Everything in ran by a Docker container. 

### Requirements

- `Docker`
- `Makefile` support

### Instalation and Execution

```bash
git clone https://github.com/lucascompython/speed-comparison.git
cd speed-comparison
make
```

## FAQ

> Does it work on Windows?

Yes, I think... 

> Are the compile/interpret times included in the comparison?

Yes, they are measured by the GNU time command!

> Why do you also count reading a file and printing the ouput?

Because I think this is a more realistic scenario to compare speeds.

## TODO (Mostly by Order)


- [X] Add TypeScript with [Deno](https://deno.land)
- [X] Add JavaScript with [Node](https://nodejs.org)
- [X] Add Java
- [ ] Add full Docker Support
- [ ] Add Terminal graphs
- [ ] Add an option to run the comparisons in parallel
- [ ] Add other methods of comparing E.g: [Leibniz formula for π](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80) to compare the floating point operations
- [ ] Add an optimized version for each language using compiler optimizations and using the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [ ] Add an option to run natively 
- [ ] Add C#
- [ ] Add Rust
- [ ] Add Golang
- [ ] Add Kotlin
- [ ] Add Swift
- [ ] Add F#
- [ ] Add Haskell
- [ ] Add Lua
- [ ] Add Scala
- [ ] Add Bash
- [ ] Add Powershell
- [ ] Add Nix
- [ ] Add Php
- [ ] Add R
- [ ] Add R plots instead of MatPlotLib
- [ ] Add Julia
- [ ] Add Elixir
- [ ] Add Ruby
- [ ] Add Raku (Perl6)
- [ ] Add Nim
- [ ] And many others...


<details>
  <summary>Super top Secret :shushing_face:</summary>
  
<!--START_SECTION:activity-->
1. **Most** languages are good, use whatever you want.
2. Execpt HTML
3. Fuck HTML
<!--END_SECTION:activity-->

</details>

<!-- 
## Thanks

This projects takes inspiration from [Thomas](https://www.thomaschristlieb.de) who did a similar comparison [on his blog](https://www.thomaschristlieb.de/performance-vergleich-zwischen-verschiedenen-programmiersprachen-und-systemen/). -->