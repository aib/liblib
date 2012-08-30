module Slice
    (sliceRange, slice)
  where

sliceRange :: Integral a => a -> a -> [(a, a)]
sliceRange r n = map ranges [0..n-1]
  where
    ranges x = (x*d + min m x, x*d + (d-1) + min m (x+1))
    (d,m) = r `divMod` n

slice :: [a] -> Int -> [[a]]
slice xs = map (map (xs !!) . uncurry enumFromTo) . sliceRange (length xs)
