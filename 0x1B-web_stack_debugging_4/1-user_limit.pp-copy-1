# Manifest modifying user limits for holberton user
exec { 'change-os-configuration-for-holberton-user':
  command => 'ulimit -n 4096 && su - holberton',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

