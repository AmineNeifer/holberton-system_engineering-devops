# execute a command that kill killmenow process
exec { 'pkill killmenow':
    path    => '/usr/bin/',
}
