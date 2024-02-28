#!/usr/bin/env ruby
# Ruby script to match the regular expression

regex = /School/  # Define the regular expression to match "School"

input = ARGV[0]   # Get the input argument passed to the script

if input.match?(regex)  # Check if the input matches the regular expression
  puts input.gsub(regex, 'School') + '$'  # Output the matched string with a "$" at the end
else
  puts '$'  # Output "$" if there is no match
end

