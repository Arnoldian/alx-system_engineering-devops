# Manifest optimizing Nginx config for improved performance
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/etc/nginx/nginx.conf':
  source => 'puppet:///modules/nginx/nginx.conf',
  notify => Service['nginx'],
}

exec { 'increase-open-files':
  command => 'echo "worker_rlimit_nofile 1024;" >> /etc/nginx/nginx.conf',
  unless  => 'grep -q "worker_rlimit_nofile" /etc/nginx/nginx.conf',
  notify  => Service['nginx'],
}

