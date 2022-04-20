# Speed comparison of programming languages 

This project compares the speed of different programming/scripting languages.

It calculates prime and composite numbers with a very basic algorithm and an more advanced one, from any given interval to do this comparisom.<br>
All languages use the same algorithms.
<!-- and it uses an implementation of the [Leibniz formula for π](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80) to do the comparison. -->


<!-- Here is a video which explains how it works: [Calculating π by hand](https://www.youtube.com/watch?v=HrRMnzANHHs) -->
---

# Preview

<div align="center">

![plot](https://cdn.discordapp.com/attachments/795277227423301643/963231527649558578/unknown.png "Speed comparison of programming languages")
![table](https://cdn.discordapp.com/attachments/795277227423301643/963231677004517406/unknown.png "Table") 

![lines](https://img.shields.io/tokei/lines/github/lucascompython/speed-comparison)
<p>
  <a href="https://github.com/lucascompython/speed-comparison/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/lucascompython/speed-comparison" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/lucascompython/speed-comparison" alt="last update" />
  </a>
  <a href="https://github.com/lucascompython/speed-comparison/network/members">
    <img src="https://img.shields.io/github/forks/lucascompython/speed-comparison" alt="forks" />
  </a>
  <a href="https://github.com/lucascompython/speed-comparison/stargazers">
    <img src="https://img.shields.io/github/stars/lucascompython/speed-comparison" alt="stars" />
  </a>
  <a href="https://github.com/lucascompython/speed-comparison/issues/">
    <img src="https://img.shields.io/github/issues/lucascompython/speed-comparison" alt="open issues" />
  </a>
  <a href="https://github.com/lucascompython/speed-comparison/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/lucascompython/speed-comparison.svg" alt="license" />
  </a>
</p>

</div>

---





## Methods

The code below is a Python code snippet of the not optimal but not bad algorithm used for counting prime and composite numbers to a given range, that is used for the different languages.

```python
for num in range(rounds):
    ctr = 0

    for i in range(2, num // 2):
        if num % i == 0:
            ctr += 1
            composites += 1
            break

    if ctr == 0 and num != 1:
        primes += 1
```

The code below is an implemation of the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) in Python

```python
primes = [True for _ in range(rounds + 1)]

for i in range(2, round(sqrt(rounds)) + 1):
    if primes[i]:
        for j in range(i ** 2, rounds, i):
            primes[j] = False

total = 0
for k in range(2, rounds):
    if primes[k]:
        total += 1
composites = rounds - total
```


## Disclaimer

I'm no expert in all these languages, so take my results with a grain of salt.<br>
The speed of the language does not determine its quality.
<!-- Also the findings just show how good the languages can handle floating point operations, which is only one aspect of a programming language. -->

You are also more than welcome to contribute and help me.

## Languages used in this comparison


- [Python](https://www.python.org/) - interpreted
- [C++](https://isocpp.org/) - compiled
- [JavaScript](https://www.ecma-international.org/publications-and-standards/standards/ecma-402/) using [Node](https://nodejs.org/en/) - interpreted; JIT
- [TypeScript](https://www.typescriptlang.org) using [Deno](https://deno.land) - interpreted; JIT
- [Java](http://www.oracle.com/technetwork/java/index.html) - compiled, VM
- [C#](https://docs.microsoft.com/en-us/dotnet/csharp/) - compiled, VM
- [Lua](https://www.lua.org) - interpreted, JIT
- [PHP](https://www.php.net) - interpreted, JIT
- [Ruby](www.ruby-lang.org) - interpreted
- [Go](https://golang.org/) - compiled
- [Rust](https://www.rust-lang.org/) - compiled
- [Powershell](https://docs.microsoft.com/en-us/powershell/) - interpreted
<!---

- [Javascript](https://www.ecma-international.org/publications/standards/Ecma-402.htm) using [Node.js](https://nodejs.org/) - interpreted, JIT
--->



## Features

- Graphs
- Tables
- Advanced but simple command line integration with multiple options for comparing (E.g: choosing with languages to compare and changing the values of the iterations).
- All languages will read from a txt file.
- The program will get and display the memory usage.
- It also has two modes, one for running native and other for running inside a docker container.
- Various ways of comparing the languages.
- Can choose to run in sequence or in parallel.
- Saves results in various formats.
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
Everything can be ran inside a Docker container.

### Requirements

- `Docker`
- `Makefile` support

### Instalation and Execution

```bash
git clone https://github.com/lucascompython/speed-comparison.git
cd speed-comparison
make run-native #to run natively must have all requirements, to run inside docker use make build && make run-docker 
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
- [X] Finish adding an optimized version for each language using compiler optimizations and using the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [X] Add an option to run the comparisons in parallel
- [X] Add an option to run natively 
- [X] Add C#
- [X] Add Lua
- [X] Add Php
- [X] Add Ruby
- [X] Add Golang
- [X] Add Rust
- [X] Add Terminal graphs
- [ ] Add other methods of comparing E.g: [Leibniz formula for π](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80) to compare the floating point operations
- [ ] Add full Docker Support
- [ ] Add Kotlin
- [ ] Add Swift
- [ ] Add F#
- [ ] Add Haskell
- [ ] Add Scala
- [ ] Add Bash
- [ ] Add Powershell
- [ ] Add Nix
- [ ] Add V
- [ ] Add R
- [ ] Add R plots instead of MatPlotLib
- [ ] Add Julia
- [ ] Add Elixir
- [ ] Add Raku (Perl6)
- [ ] Add Nim
- [ ] And many others...



## Know Bugs (Because im too lazy to fix them...)

* For the first time running the comparison you might need to to run it twice because deno shows some extra information at the first compilation of a file.
* Docker doesn't support graphical graphs for now. 

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