import System.IO
import Data.List (sort, foldl')
import qualified Data.Set as S

tupleToList :: (a, a) -> [a]
tupleToList (x, y) = [x, y]

main :: IO ()
main = do
    input <- readFile "input.txt"
    let ls = lines input
    let pair_lines = map words ls
    let parsed_lists = map (map (read :: String -> Integer)) pair_lines
    let parsed_pairs = map (\[x, y] -> (x, y)) parsed_lists
    let unzipped = (tupleToList . unzip) parsed_pairs
    print $ solvePart1 unzipped
    print $ solvePart2 unzipped


solvePart1 :: (Ord a, Num a) => [[a]] -> a
solvePart1 unzipped =
    let sorted = map sort unzipped
        rezipped = zip (head sorted) ((head . tail) sorted)
        diffs = map (\(x, y) -> abs (x - y)) rezipped
    in foldl' (+) 0 diffs

solvePart2 :: (Ord a, Num a) => [[a]] -> a
solvePart2 unzipped =
    let left_set = S.fromList (head unzipped)
        allowed = filter (`S.member` left_set) ((head . tail) unzipped)
    in foldl' (+) 0 allowed