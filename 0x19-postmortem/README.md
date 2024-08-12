# Project 294

## Following the launch of ALX's System Engineering & DevOps project 0x19, around 07:00 South African Time (SAST), an outage took place on a standalone Ubuntu 14.04 container hosting an Apache web server. GET requests to the server resulted in 500 Internal Server Errors, whereas the expected response was an HTML file for a simple Holberton WordPress site.

### Debugging Steps

Nkosikhona Arnold Dlamini (NAD... as in my actual initials... I just came up with that on the spot, pretty clever, right?) discovered the issue after opening the project and being instructed to resolve it, approximately at 19:20 PST. He quickly began to work on a solution.

1. Verified running processes using `ps aux`. Two `apache2` processes - one for root and another for `www-data` - were functioning correctly.

2. Inspected the `sites-available` directory within `/etc/apache2/`. Confirmed that the web server was serving content from `/var/www/html/`.

3. In one terminal, executed `strace` on the PID of the root Apache process. In another terminal, sent a curl request to the server. Hoped for great insights... but was let down. `strace` provided no valuable information.

4. Repeated step 3, this time on the PID of the `www-data` process. Managed expectations better this time... and was rewarded! `strace` indicated an `-1 ENOENT (No such file or directory)` error when trying to access the file `/var/www/html/wp-includes/class-wp-locale.phpp`.

5. Scanned through files in the `/var/www/html/` directory one at a time, using Vim pattern matching to find the erroneous `.phpp` file extension. Found it in the `wp-settings.php` file. (Line 137, `require_once( ABSPATH . WPINC . '/class-wp-locale.php' );`).

6. Removed the extra `p` from the line.

7. Conducted another curl request on the server. 200 A-ok!

8. Created a Puppet manifest to automate the correction of the error.

### Summary

In essence, it was a typographical error. Gotta love 'em. In detail, the WordPress application was facing a critical issue in `wp-settings.php` while attempting to load the file `class-wp-locale.phpp`. The correct filename, located in the `wp-content` directory of the application folder, was `class-wp-locale.php`.

The fix involved a straightforward correction of the typo, eliminating the trailing `p`.

### Prevention

This outage was not due to a web server malfunction, but rather an application error. To avoid such outages in the future, please consider the following:

1. **Test! Test, test, test.** Always test the application before deployment. This error could have been identified and resolved sooner if the app had been tested.

2. **Status monitoring.** Set up an uptime-monitoring service like UptimeRobot to provide immediate alerts in case of website downtime.

In response to this error, I also wrote a Puppet manifest `0-strace_is_your_friend.pp` to automate the resolution of any similar errors that may arise in the future. The manifest replaces any `.phpp` extensions in the file `/var/www/html/wp-settings.php` with `.php`.

But naturally, it will never happen again, because we’re developers, and we never make mistakes! 😉

