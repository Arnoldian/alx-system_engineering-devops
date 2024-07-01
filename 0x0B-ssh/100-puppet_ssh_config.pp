# configure ssh for priv key no passw

# Ensure SSH client config file exists
file { '/etc/ssh/ssh_config':
  ensure => present,
}

# Configure SSH to use private key ~/.ssh/school
file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
}

# Configure SSH to refuse password authentication
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}

