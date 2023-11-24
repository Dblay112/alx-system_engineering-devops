# Install Flask from pip3 with version 2.1.0
package { 'Flask':
  ensure => present,
  provider => 'pip3',
  version => '2.1.0',
}
