# script to execute a command
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
