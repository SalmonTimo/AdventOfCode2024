defmodule AdventOfCodeDay01 do
  def main do
    {left, right} = IO.stream(:stdio, :line)
    |> Stream.map(&String.split/1)
    |> Stream.map(&List.to_tuple/1)
    |> Enum.unzip()

    left_set = MapSet.new(left)
    Stream.filter(right, &MapSet.member?(left_set, &1))
    |> Stream.map(&String.to_integer/1)
    |> Enum.sum()
  end
end

IO.puts(AdventOfCodeDay01.main())
