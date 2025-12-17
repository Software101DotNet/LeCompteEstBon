/* 
# Copyright (C) 2025 Anthony Ransley
# https://github.com/Software101DotNet/LeCompteEstBon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>. 
*/

using System.Collections.Generic;
using System.Linq;
using System.Data;

namespace LeCompteEstBon;

public class Program
{
	enum ExitCode : int { Success = 0, CmdLineError = 1, Exception = 2 };

	static int Main(string[] args)
	{
		var exitCode = ExitCode.Success;

		try
		{
			// var dt = new DataTable();
			// var result = dt.Compute("(10 + 5) * 3", "");
			// Console.WriteLine(result);

			var numberSet = new List<double> { 50, 4, 6, 9, 3, 8 };
			int targetValue = 532;

			Console.WriteLine($"\nCalculating possible solutions for {targetValue} using the set of numbers [{string.Join(", ", numberSet)}]:\n");

			var solutions = PossibleGameSolutions(numberSet);

			Console.WriteLine($"Evaluating {solutions.Count} possible solutions...\n");

			int index = 0;
			foreach (var expr in solutions)
			{
				double result = EvalExpression(expr);
				Console.WriteLine($"{index,5}  {expr} = {result}");
				index++;
			}

		}
		catch (Exception e)
		{
			Console.WriteLine($"{e.Message}");

			if (e.InnerException != null)
				Console.WriteLine(e.InnerException.Message);

			exitCode = ExitCode.Exception;
		}

		return (int)exitCode; // Application exit code for use with commandline chaining or scripting
	}


	static readonly char[] Ops = { '+', '-', '*', '/' };

	static SortedSet<string> PossibleGameSolutions(List<double> numbers)
	{
		var results = new SortedSet<string>();

		void BuildExpr(List<double> nums, List<string> exprs)
		{
			if (nums.Count == 1)
			{
				results.Add(exprs[0]);
				return;
			}

			for (int i = 0; i < nums.Count; i++)
			{
				for (int j = 0; j < nums.Count; j++)
				{
					if (i == j) continue;

					double a = nums[i];
					double b = nums[j];
					string ea = exprs[i];
					string eb = exprs[j];

					var remainingNums = new List<double>();
					var remainingExprs = new List<string>();

					for (int k = 0; k < nums.Count; k++)
					{
						if (k != i && k != j)
						{
							remainingNums.Add(nums[k]);
							remainingExprs.Add(exprs[k]);
						}
					}

					foreach (char op in Ops)
					{
						if (op == '/' && b == 0)
							continue;

						double val;
						try
						{
							val = op switch
							{
								'+' => a + b,
								'-' => a - b,
								'*' => a * b,
								'/' => a / b,
								_ => throw new InvalidOperationException()
							};
						}
						catch
						{
							continue;
						}

						string newExpr = $"({ea}{op}{eb})";

						var newNums = new List<double>(remainingNums) { val };
						var newExprs = new List<string>(remainingExprs) { newExpr };

						BuildExpr(newNums, newExprs);
					}
				}
			}
		}

		// subsets of size >= 2
		for (int r = 2; r <= numbers.Count; r++)
		{
			foreach (var subset in Combinations(numbers, r))
			{
				foreach (var perm in Permutations(subset))
				{
					BuildExpr(
						perm.Select(x => (double)x).ToList(),
						perm.Select(x => x.ToString()).ToList()
					);
				}
			}
		}

		return results;
	}

	static IEnumerable<List<T>> Combinations<T>(List<T> list, int length)
	{
		if (length == 1)
			return list.Select(t => new List<T> { t });

		return Combinations(list, length - 1)
			.SelectMany(
				t => list.Skip(list.IndexOf(t.Last()) + 1),
				(t, e) =>
				{
					var newList = new List<T>(t) { e };
					return newList;
				});
	}

	static IEnumerable<List<T>> Permutations<T>(List<T> list)
	{
		if (list.Count == 1)
			return new List<List<T>> { new List<T>(list) };

		return list.SelectMany((e, i) =>
			Permutations(list.Where((_, j) => j != i).ToList())
			.Select(p =>
			{
				var newList = new List<T> { e };
				newList.AddRange(p);
				return newList;
			}));
	}

	static double EvalExpression(string expr)
	{
		var table = new DataTable();
		return Convert.ToDouble(table.Compute(expr, ""));
	}
}