#!/bin/ruby

#
# Complete the getTotalX function below.
#
def getTotalX(a, b)
    #
    # Write your code here.
    #

end

fp = File.open(ENV['OUTPUT_PATH'], 'w')

nm = gets.rstrip.split

n = nm[0].to_i

m = nm[1].to_i

a = gets.rstrip.split(' ').map(&:to_i)

b = gets.rstrip.split(' ').map(&:to_i)

total = getTotalX a, b

fp.write total
fp.write "\n"

fp.close()
