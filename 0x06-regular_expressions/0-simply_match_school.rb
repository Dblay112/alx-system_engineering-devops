#!/usr/bin/env ruby
regex = /School/i
input_command = ARGV[0]
match = regex.match(input_command)
if match
  puts match[0]
else
  puts "No match found"
end
