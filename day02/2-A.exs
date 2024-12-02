defmodule AdventOfCodeDay01 do
  def in_range(x) do
    x > 0 and x <= 3
  end

  def main do
    IO.stream(:stdio, :line)
    |> Stream.map(&String.split/1)
    |> Stream.map(fn l ->
      l
      |> Enum.map(&String.to_integer/1)
      |> Enum.chunk_every(2, 1, :discard)
      |> Enum.map(&List.to_tuple/1)
      |> Enum.map(fn {a, b} -> b - a end)
      |> Enum.map(fn a -> {in_range(a), in_range(-a)} end)
      |> Enum.reduce({true, true}, fn {a, b}, {acc_a, acc_b} ->
        {a and acc_a, b and acc_b}
      end)
    end)
    |> Enum.count(fn {a, b} -> a or b end)
  end
end

IO.puts(AdventOfCodeDay01.main())
