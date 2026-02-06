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

This is the first implementation of the program, which uses the BODMAS rules of mathematical expression evaluation, with the limitation that it can only find all the solutions that do not require parentheses in the formula. i.e. the ODMAS rules have been implemented, with the B to be implemented in the next version. 

An example, given the number set [9,7,2,4,9,25] and the target value of 667, This version will find the solutions such as 9 * 9 * 7 + 4 * 25 = 667, but it will not find the other solution that requires parathasis of the form ((9*4)-7)*(25-2)=667.

The following implementation will also consider parathasis ( ) and will consequently find the complete set of possible solutions of a given number set to reach a given target number.








