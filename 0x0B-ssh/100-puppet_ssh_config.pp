# Configure SSH client to use private key
file { '/etc/ssh/ssh_config':
  ensure => present,
  content => "Host *\n\
               IdentityFile ~/.ssh/school\n\
               PubkeyAuthentication yes\n\
               PasswordAuthentication no\n"
}
