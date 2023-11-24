#!/usr/bin/pup
# install flaskis

package {'flask':
ensure   => '2.1.0',
provider => 'pip3'
}
