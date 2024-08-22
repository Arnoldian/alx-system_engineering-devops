# Manifest modifying user limits for holberton user
exec { 'change-os-configuration-for-holberton-user':
  command => 'ulimit -n 1024',
  user    => 'holberton',
}

