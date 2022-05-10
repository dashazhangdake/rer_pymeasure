# rer_pymeasure: Modernized legacy codes for RER scientific measurements 
A repo of RER codes implemented on the top of [pymeasure](https://pymeasure.readthedocs.io/en/latest/). We made necessary modifications to vanilla Pymeasure code to fit the needs RER experiments
# Repo Overview:
Currently, this repo includes the following:
## Notebooks
* **```B1505DevMemo:```** 
  * An overview of command mappings between B1505 mannual and Pymeasure
  * An memo of pymeasure base class implementation
* **```agilent1505Top_interactive:```**
  * An interactive example for a "simple" **staircase sweep measurments experiment**
  * Currently, running this notebook allows users to measure ```Vg, Ig, Id```. 
   * ```Vg``` is the primary sweeping source(0v to 3v with a step of 0.33v); Vd sweeps from 1v to 3v with a step of 1v
## Source Codes
* **```agilent1505.py:```**
  * A b1505a instrument class. This class inherits most features of the Pymeasure ```AgilentB1500``` class.
  * We made a few adjustments get the modfied B1500 work with B1505A.
## Learn Python
* **Python fundamentals for Pymeasure**
  * A memo for weird syntax we met when studying the source of vanilla Pymeasure
* We strongly recommend learning some python fundamentals (from commonly used basic data structure to basic OOP) before using this repo. Even you are a EE student.
  * [UCB CS61A](https://cs61a.org/)
  * [Mynotes of CS61A S22](https://github.com/dashazhangdake/my_cs61a)
