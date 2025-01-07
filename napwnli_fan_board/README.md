# Napwnli fan board

**Author**: napwnli

**Difficulty**: ★☆☆☆☆

**Categories**: Web

Napwnli Fan Board is a service for sharing random feeds with other users. By refreshing the homepage, the site randomly picks a stored feed and displays it on the homepage. Every user must sign up to publish their feed. If the feed contains the tag ```!hidden!```, it will not be shown on the homepage to preserve users' privacy.


## Flag stores
The flags are stored into:
- Users' password
- Users' hidden feeds

## Flag Ids
The game server must provide:
- Victims' usernames

## Vulnerabilities

### Database is exposed with default credentials
The database is exposed to the outside with default credentials. An attacker could connect to the database and steal users' passwords (flag store).

To fix this, you should both change the default credentials and ensure the database is not exposed to the outside.

### SQL Injection
The service's login route does not properly sanitize input. Attackers can easily log in as any user if they know the username. This gives access to the victim's feed (flag store).

To fix this, you can:
- Use prepared statements
- Improve the sanification

### Unsafe session
The user's session stores both the username and password. The token is encoded in Base64, which can be easily decoded using tools like CyberChef. This means that if an attacker gains access to the session, they can easily retrieve and exploit the stored password.

To fix this you should modify the way the server creates the user's session in the login route.

### Session forgery


### Path traversal
