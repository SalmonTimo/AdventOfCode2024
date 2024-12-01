defmodule AdventOfCodeDay01 do
  def main do
    IO.stream(:stdio, :line)
    |> Stream.map(&String.split/1)
    |> Stream.map(&List.to_tuple/1)
    |> Enum.unzip()
    |> Tuple.to_list()
    |> Stream.map(&Enum.sort/1)
    |> Stream.zip()
    |> Stream.map(fn x -> abs(String.to_integer(elem(x, 0)) - String.to_integer(elem(x, 1))) end)
    |> Enum.reduce(fn y, acc -> y + acc end)
  end
end

IO.puts(AdventOfCodeDay01.main())
