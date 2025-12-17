<br />
<div align="center">

<h3 align="center">Le Compte Est Bon</h3>

  <p align="center">
    The program is a solver (or solution finder) for the number game "Le Compte Est Bon" that is seen in the TV show "Des chiffres et des lettres" 
    <br />
    <br />
    The game originates from the French game show Des chiffres et des lettres ("Numbers and Letters"), on which Countdown is based. In the French version, the equivalent numbers segment is specifically known as "Le compte est bon", which translates to "The total is right" or "The count is good"—referring to exactly hitting the target for full points.
    <br />
    <br />
    <a href="https://github.com/Software101DotNet/LeCompteEstBon">View Demo</a>
    ·
    <a href="https://github.com/Software101DotNet/LeCompteEstBon/issues">Report Bug</a>
    ·
    <a href="https://github.com/Software101DotNet/LeCompteEstBon/issues">Request Feature</a>
  </p>
  
</div>


## About The Project

The program is a solver (or solution finder) for the number game "Le Compte Est Bon" that is seen in the TV shows known as Des chiffres et des lettres (France), Count Down and Cat’s Do Count Down (UK), Letters and Numbers (Australia). There may be other TV shows around the world, but the number game seems to be the same in all of them.

Give the program the target number (in the TV game this is a randomlly sellected number between 100 to 999) and six numbers that are randomly selected from the set 1,2,3,4,5,6,7,8,9,10,25,50,75,100 and the program will calculate every possible formula using the operators + - * / and parathasis ( ) with every combination of 1 to all siz number where the formual evaluates to the target number.

## About The Implementation

There are two implementations of the same program. The first version was implemented in Python and the source code is in the subfolder Python. The program was then rewritten in C# for .NET because the Python version took more than 30 seconds to execute. This would be kind of pointless if playing along with the TV show.

Both the Python and C# versions can be run on macOS, Linux, and Windows; however, the Python version takes 9 hours to execute on Apple M4, whereas the C# version constructs and solves the equation combinations in a fraction of the time.





