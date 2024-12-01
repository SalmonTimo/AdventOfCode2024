defmodule AdventOfCodeDay01 do
  def main do
    IO.stream(:stdio, :line)
    |> Stream.map(&String.split/1)
    |> Stream.map(fn [a, b] -> {String.to_integer(a), String.to_integer(b)} end)
    |> Enum.unzip()
    |> Tuple.to_list()
    |> Stream.map(&Enum.sort/1)
    |> Stream.zip()
    |> Stream.map(fn {a, b} -> abs(a - b) end)
    |> Enum.sum()
  end
end

IO.puts(AdventOfCodeDay01.main())
