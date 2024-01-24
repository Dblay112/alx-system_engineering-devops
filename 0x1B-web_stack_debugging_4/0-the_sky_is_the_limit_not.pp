# puppet sctipt to increase the amount of traffic an Nginx server can handle.

# puppet script to increase the ULIMIT of the default file
exec { 'fix-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
